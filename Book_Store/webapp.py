from . import app
from flask import request
from . import DUMMY_RESPONSE_JSON


@app.route('/books/<category>', methods=['GET'])
def get_book_list(category):
    return DUMMY_RESPONSE_JSON['get_book_list']


@app.route('/books/<book_id>', methods=['GET'])
def get_book(book_id):
    return DUMMY_RESPONSE_JSON['get_book']


@app.route('/basket/<user_id>/<basket_id>', methods=['GET'])
def get_basket(user_id, basket_id):
    return DUMMY_RESPONSE_JSON['get_basket']


@app.route('/basket/<user_id>', methods=['POST'])
def create_basket(user_id):
    return DUMMY_RESPONSE_JSON['add_to_basket']


@app.route('/basket/<user_id>/<basket_id>', methods=['PUT'])
def update_basket(user_id, basket_id):
    return DUMMY_RESPONSE_JSON['update_basket']


@app.route('/basket/<user_id>/<basket_id>', methods=['DELETE'])
def delete_basket_items(user_id, basket_id):
    return DUMMY_RESPONSE_JSON['delete_basket_items']


@app.route('/orders/<user_id>/<basket_id>', methods=['POST'])
def place_order(user_id, basket_id):
    return DUMMY_RESPONSE_JSON['place_order']
