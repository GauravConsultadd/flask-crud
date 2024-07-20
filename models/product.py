from db import db
from sqlalchemy import Column, Integer, String

class Product(db.Model):
    __tablename__ = 'products'  # Optional: Define the table name

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    price = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<Product id={self.id} name={self.name} price={self.price}>'