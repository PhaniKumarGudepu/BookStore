from sqlalchemy import Column,String,Integer,ForeignKey,Float,Boolean
from sqlalchemy.orm import relationship
from Book_Store import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    baskets = relationship('Basket', back_populates = 'user')
    orders = relationship('Order', back_populates = 'user')

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    price = Column(Float)
    description = Column(String)
    author = Column(String)
    publisher = Column(String)
    category = Column(String)
    is_available = Column(Boolean)

class Basket(Base):
    __tablename__ = "basket"
    id = Column(Integer, primary_key = True)
    total_price = Column(Float)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User",back_populates = 'basket')
    order = relationship("Order",back_populates = 'basket',uselist = False)

class BasketBookAssociation(Base):
    __tablename__ = 'basket_book_association'
    book_id = Column(Integer, ForeignKey('book.id'), primary_key = True)
    basket_id = Column(Integer, ForeignKey('basket.id'), primary_key = True)
    books = relationship("Book",back_populates = 'book')
    baskets = relationship("Basket",back_populates = 'basket')

class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    basket_id = Column(Integer, ForeignKey('basket.id'))
    user = relationship("User",back_populates = 'order')
    basket = relationship("Basket",back_populates = 'order')

