from flask_restful import Resource, reqparse
from models.product import Product
from db import db

class ProductResource(Resource):
    def get(self, product_id):
        product = Product.query.get(product_id)
        if not product:
            return {'message': 'Product not found'}, 404
        return {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description
        }
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Name cannot be blank')
        parser.add_argument('price', type=float, required=True, help='Price cannot be blank')
        parser.add_argument('description', type=str)
        args = parser.parse_args()
        
        product = Product(
            name=args['name'],
            price=args['price'],
            description=args.get('description')
        )
        db.session.add(product)
        db.session.commit()
        return {'message': 'Product created', 'id': product.id}, 201

    def put(self, product_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('price', type=float)
        parser.add_argument('description', type=str)
        args = parser.parse_args()
        
        product = Product.query.get(product_id)
        if not product:
            return {'message': 'Product not found'}, 404
        
        if args['name']:
            product.name = args['name']
        if args['price']:
            product.price = args['price']
        if args['description']:
            product.description = args['description']
        
        db.session.commit()
        return {'message': 'Product updated'}
    
    def delete(self, product_id):
        product = Product.query.get(product_id)
        if not product:
            return {'message': 'Product not found'}, 404
        
        db.session.delete(product)
        db.session.commit()
        return {'message': 'Product deleted'}
