from flask import Flask, render_template, request
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os
app = Flask(__name__)

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_businesses(location, params):
    auth = Oauth1Authenticator(
        consumer_key=os.environ.get('CONSUMER_KEY'),
        consumer_secret=os.environ.get('CONSUMER_SECRET'),
        token=os.environ.get('TOKEN'),
        token_secret=os.environ.get('TOKEN_SECRET')
        )

    client = Client(auth)

    response = client.search(location, params)
    businesses = []


    for business in response.businesses:
        businesses.append({
            "name": business.name,
            "rating": business.rating,
            "phone": business.display_phone
        })

    return businesses

    def print_businesses(businesses):
        for business in businesses:
            print(business.name)
            print(business.rating)
            print(business.phone)
            print("\n ")

    businesses = print_businesses(businesses)


@app.route('/')
def index():
    location = request.values.get('location')
    params = request.values.get('params')
    businesses = None
    if location:
        businesses = get_businesses(location, params)
        return render_template('index.html', businesses=businesses)
    else:
        return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
