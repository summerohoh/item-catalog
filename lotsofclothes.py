from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from catalog_dbsetup import Category, Base, Item

engine = create_engine('sqlite:///clothingcatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

category1 = Category(name="Tshirt")
session.add(category1)
session.commit()

category2 = Category(name="Jackets")
session.add(category2)
session.commit()

category3 = Category(name="Dress")
session.add(category3)
session.commit()

item1 = Item(name="BASIC STUSSY TEE", img="https://d2zrsppk7u9t1b.cloudfront.net/store/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/2/9/2902934_DURO_1.jpg",
	brand = "Stussy", shopURL="view-source:https://www.stussy.com/us/basic-stussy-tee-101220?color_item=632", price="$30.00", category=category1)

session.add(item1)
session.commit()

item2 = Item(name="Solid BB T-shirt", img="https://d2zrsppk7u9t1b.cloudfront.net/store/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/2/9/2902934_DURO_1.jpg",
	brand = "Stussy", shopURL="https://www.graffitishop.net/T-shirts-Streetwear?jsvpd-130398", price="$30.00", category=category1)

session.add(item2)
session.commit()

item3 = Item(name="90's Vintage Tee", img="https://d2zrsppk7u9t1b.cloudfront.net/store/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/2/9/2902934_DURO_1.jpg",
	brand = "Stussy", shopURL="view-source:https://www.stussy.com/us/basic-stussy-tee-101220?color_item=632", price="$30.00", category=category1)

session.add(item3)
session.commit()

item4 = Item(name="BASIC STUSSY TEE", img="https://d2zrsppk7u9t1b.cloudfront.net/store/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/2/9/2902934_DURO_1.jpg",
	brand = "Stussy", shopURL="view-source:https://www.stussy.com/us/basic-stussy-tee-101220?color_item=632", price="$30.00", category=category1)

session.add(item4)
session.commit()

item5 = Item(name="Solid BB T-shirt", img="https://d2zrsppk7u9t1b.cloudfront.net/store/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/2/9/2902934_DURO_1.jpg",
	brand = "Stussy", shopURL="https://www.graffitishop.net/T-shirts-Streetwear?jsvpd-130398", price="$30.00", category=category1)

session.add(item5)
session.commit()

item6 = Item(name="90's Vintage Tee", img="https://d2zrsppk7u9t1b.cloudfront.net/store/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/2/9/2902934_DURO_1.jpg",
	brand = "Stussy", shopURL="", price="$30.00", category=category1)

session.add(item6)
session.commit()
