from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	email = Column(String(250), nullable=False)
	picture = Column(String(250))


class Category(Base):
	__tablename__ = 'category'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
		#returns objecto data in easily serializeable format
		return{
			'name': self.name,
			'id': self.id
		}

class Item(Base):
	__tablename__ = 'item'

	id = Column(Integer, primary_key=True)
	name = Column(String(80), nullable=False)
	img= Column(String(250))
	brand = Column(String(250))
	shopURL= Column(String(250))
	price = Column(String(8))
	category_id = Column(Integer, ForeignKey('category.id'))
	category = relationship(Category)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
		#returns object data in easily serializeable format
		return{
			'id': self.id,
			'name': self.name,
			'img':self.img,
			'brand':self.brand,
			'price': self.price
		}


engine = create_engine('sqlite:///clothingcatalog.db')
Base.metadata.create_all(engine)