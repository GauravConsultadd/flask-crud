from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from db import db
import os
from models.product import Product

load_dotenv()
app = Flask(__name__)
api  = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://Gaurav:password@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print(os.getenv("DATABASE_URI") + "--------------------------------------  ")
db.init_app(app)

with app.app_context():
    db.create_all()

from controllers.product_controller import ProductResource

api.add_resource(ProductResource, '/products/<int:product_id>', '/products')

if __name__ == "__main__":
    app.run(debug=True)