import datetime
import json
import logging
from flask import Flask
from flask import request
from flask import jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from api.controllers.default import calculate_total, delivery_price


class JSONEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, datetime.datetime):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


def get_fees(fees):
    delivery_fees = []
    for f in fees:
        delivery_fees.append(
            (
                f['eligible_transaction_volume']['min_price'],
                f['eligible_transaction_volume']['max_price'],
                f['price']
            )
        )

    # return a list of tuples
    return delivery_fees


def create_app(config=None):
    app = Flask(__name__)
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/joyjet'
    mongo = PyMongo(app)
    app.json_encoder = JSONEncoder
    if config == 'TEST':
        app.config['TEST'] = True

    @app.route('/cart_checkout', methods=['POST'])
    def cart_checkout():

        # Parse request data as JSON
        data = request.get_json()

        logging.info(
            "API got a new request with data: {0}".format(json.dumps(data))
            )

        # get articles, discounts, carts and delivery_fees from json
        articles = data.get('articles', None)
        carts = data.get('carts', None)
        discounts = data.get('discounts', None)
        fees = data.get('delivery_fees', None)

        if carts is None:
            return jsonify(msg="Bad Request: carts can't be empty"), 400

        elif articles is None:
            return jsonify(msg="Bad Request: articles can't be empty"), 400

        articles_dict = {}
        for i in articles:
            articles_dict[i['id']] = {'name': i['name'], 'price': i['price']}

        if discounts is not None:
            discounts = {
                i['article_id']: {
                    'type': i['type'], 'value': i['value']
                    }

                for i in discounts
            }

        # Apply calculate_total function to all values in cart
        logging.info("Start to calculate checkout price")
        cart_total = []
        for c in carts:
            cart_total.append(
                {
                    'id': c['id'],
                    'total': calculate_total(
                        c['items'], articles_dict, discounts
                        ),
                }
            )

        if fees is not None:
            delivery_fees = get_fees(fees)
            cart_total = [
                    {
                        **cart,
                        'total': cart['total']
                        + delivery_price(cart['total'], delivery_fees),
                    }
                    for cart in cart_total
                ]

        logging.info(
            "Finish calculation, result: {0}".format(json.dumps(cart_total))
            )

        checkout_id = mongo.db.cart_checkout.insert_one(
            {"carts": cart_total}
            ).inserted_id

        if checkout_id:
            logging.info(
                "Data inserted successfully, ID: {0}".format(checkout_id)
                )

        return jsonify({"carts": cart_total}), 200

    return app
