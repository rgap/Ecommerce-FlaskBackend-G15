from app.db import db
from app.models.product import Product
from flask import Blueprint, request
from utils import response_error, response_success

product_route = Blueprint("product_route", __name__)


@product_route.route("/product", methods=["GET"])
def get_product():
    try:
        product = Product.query.first()
        price = product.price if product else None
        return response_success({"price": price})
    except Exception as e:
        return response_error(str(e), 500)


@product_route.route("/product", methods=["POST"])
def update_product():
    try:
        new_price = request.json.get("price")
        product = Product.query.first()
        if product:
            product.update_price(new_price)
        else:
            product = Product(price=new_price)
            db.session.add(product)
        db.session.commit()
        return response_success({"message": "Price updated successfully"})
    except Exception as e:
        return response_error(str(e), 500)
