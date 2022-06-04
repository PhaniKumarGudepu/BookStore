from . import app                                        
from flask import request                                        
from . import DUMMY_RESPONSE_JSON

@app.route('/books',methods=['GET'])                                                 
def get_book_list():                                                 
	return DUMMY_RESPONSE_JSON['get_book_list']

@app.route('/books/<book_id>',methods=['GET'])                                                 
def get_book(book_id):                                                 
	return DUMMY_RESPONSE_JSON['get_book']

@app.route('/basket/<basket_id>',methods=['GET'])                                                 
def get_basket(basket_id):                                                 
	return DUMMY_RESPONSE_JSON['get_basket']

@app.route('/basket',methods=['POST'])                                                 
def add_to_basket():                                                 
	return DUMMY_RESPONSE_JSON['add_to_basket']

@app.route('/basket/<basket_id>',methods=['PUT'])                                                 
def update_basket(basket_id):                                                 
	return DUMMY_RESPONSE_JSON['update_basket']

@app.route('/basket/<basket_id>',methods=['DELETE'])                                                 
def delete_basket_items(basket_id):                                                 
	return DUMMY_RESPONSE_JSON['delete_basket_items']

@app.route('/orders',methods=['POST'])                                                 
def place_order():                                                 
	return DUMMY_RESPONSE_JSON['place_order']

