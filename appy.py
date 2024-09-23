from flask import Flask, jsonify, render_template, request
import pandas as pd
import tensorflow as tf
import numpy as np
import requests
from bs4 import BeautifulSoup
import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Example product data
products = [
    {"id": 1, "name": "Product 1", "description": "Description of Product 1", "price": 100},
    {"id": 2, "name": "Product 2", "description": "Description of Product 2", "price": 200},
    {"id": 3, "name": "Product 3", "description": "Description of Product 3", "price": 300},
    {"id": 4, "name": "Product 4", "description": "Description of Product 4", "price": 400},
    {"id": 5, "name": "Product 5", "description": "Description of Product 5", "price": 500}
]

# Example user data
users = [
    {"id": 1, "name": "User 1", "email": "user1@example.com"},
    {"id": 2, "name": "User 2", "email": "user2@example.com"},
    {"id": 3, "name": "User 3", "email": "user3@example.com"},
    {"id": 4, "name": "User 4", "email": "user4@example.com"},
    {"id": 5, "name": "User 5", "email": "user5@example.com"}
]

# Example recommendations
recommendations = [
    {"title": "Recommendation 1", "description": "Description of Recommendation 1"},
    {"title": "Recommendation 2", "description": "Description of Recommendation 2"},
    {"title": "Recommendation 3", "description": "Description of Recommendation 3"},
    {"title": "Recommendation 4", "description": "Description of Recommendation 4"},
    {"title": "Recommendation 5", "description": "Description of Recommendation 5"}
]

@app.route('/')
def index():
    return render_template('About.html')

@app.route('/product', methods=['GET'])
def get_product():
    product_id = request.args.get('id')
    product = next((product for product in products if product['id'] == int(product_id)), None)
    return jsonify(product) if product else jsonify({"error": "Product not found"}), 404

@app.route('/search', methods=['GET'])
def search_products():
    search_term = request.args.get('search')
    matching_products = [product for product in products if search_term.lower() in product['name'].lower()]
    return jsonify(matching_products)

@app.route('/user', methods=['GET'])
def get_user():
    user_id = request.args.get('id')
    user = next((user for user in users if user['id'] == int(user_id)), None)
    return jsonify(user) if user else jsonify({"error": "User not found"}), 404

@app.route('/user-recommendations', methods=['GET'])
def get_user_recommendations():
    user_id = request.args.get('id')
    user = next((user for user in users if user['id'] == int(user_id)), None)
    if user:
        # Example recommendations based on user's past purchases
        past_purchases = [1, 2, 3, 4, 5]
        purchase_descriptions = ["Description 1", "Description 2", "Description 3", "Description 4", "Description 5"]
        recommendations = []
        for i, purchase_id in enumerate(past_purchases):
            product = next((product for product in products if product['id'] == purchase_id), None)
            if product:
                recommendations.append({
                    "title": f"Recommendation for User {user['id']}",
                    "description": f"Based on your purchase: {purchase_descriptions[i]}"
                })
        return jsonify(recommendations) 
    return jsonify({"error": "User not found"}), 404

@app.route('/best-selling-products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/contact', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/conclusion', methods=['GET'])
def get_recommendations():
    # Example recommendations logic
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
