from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Restaurant, Base, MenuItem

import json
 
engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Open File
with open('menu.json') as in_file:
    data = json.load(in_file)

# Read File
for restaurant in data['restaurants']:
	venue = Restaurant(name = restaurant["name"])
	session.add(venue)
	session.commit()
	for item in restaurant["menu"]:
		menuItem = MenuItem(name = item["name"], description = item["description"], price = item["price"], course = item["course"], restaurant = venue)
		session.add(menuItem)
		session.commit()

print ("added menu items!")