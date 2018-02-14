from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from catalog_dbsetup import Base, Category, Item
from flask import session as login_session
import random, string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
	open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Clothing Catalog"

engine = create_engine('sqlite:///clothingcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/login')
def showLogin():
	state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
	login_session['state'] = state
	return render_template('login.html', STATE = state)

@app.route('/gconnect', methods=['POST'])
def gconnect():
	if request.args.get('state') != login_session['state']:
		response = make_response(json.dumps('Invalid state parameter'), 401)
		response.headers['Content-Type'] = 'application/json'
		return response
	code = request.data

	try:
		oauth_flow = flow_from_clientsecrets('client_secrets.json', scope= '')
		oauth_flow.redirect_uri = 'postmessage'
		credentials = oauth_flow.step2_exchange(code)
	except FlowExchangeError:
		response = make_response(json.dumps('Failed to upgrade the authorization code'), 401)
		response.headers['Content-Type'] = 'application/json'
		return response

	#check if access token in valid
	access_token = credentials.access_token
	url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' %access_token)
	#create json GET request containing url & access token
	h = httplib2.Http()
	result = json.loads(h.request(url, 'GET')[1])
	# if there is an error, abort.
	if result.get('error') is not None:
		response = make_response(json.dumps(result.get('error')), 500)
		response.headers['Content-Type'] = 'application/json'
		return response

	#verify access token is used for the intended use
	gplus_id = credentials.id_token['sub']
	if result['user_id'] != gplus_id:
		response = make_response(
			json.dumps("Token's user ID does not match given user ID.", 401))
		response.headers['Content-Type'] = 'application/json'
		return response
	#verify access token is valid for the app
	if result['issued_to'] != CLIENT_ID:
		response = make_response(json.dumps("Token's client ID does not match app's.", 401))
		print "Token's client ID does not match app's."
		response.headers['Content-Type'] = 'application/json'
		return response

	#cheked if user is already logged in
	stored_access_token = login_session.get('access_token')
	stored_gplus_id = login_session.get('gplus_id')
	if stored_access_token is not None and gplus_id == stored_gplus_id:
		response = make_response(json.dumps('Current user is already connected'), 200)
		response.headers['Content-Type'] = 'application/json'
		return response

	#store the access token in the session for later use
	login_session['access_token'] = credentials.access_token
	login_session['gplus_id'] = gplus_id

	# Get user info
	userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
	params = {'access_token': credentials.access_token, 'alt': 'json'}
	answer = requests.get(userinfo_url, params=params)

	data = answer.json()

	login_session['username'] = data['name']
	login_session['picture'] = data['picture']
	login_session['email'] = data['email']
	output = ''
	output += 'Welcome, '
	output += login_session['username']
	output += '!'
	output += '<img src="'
	output += login_session['picture']
	output += ' " style = "width: 100px; height: 100px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
	flash("you are now logged in as %s" % login_session['username'])
	print "done!"
	return output

#DISCONNECT
@app.route('/gdisconnect')
def gdisconnect():
	access_token = login_session.get('access_token')
	print 'In gdisconnect access token is %s', access_token
	print 'User name is: '
	print login_session.get('username')
	if access_token is None:
		print 'Access Token is None'
		response = make_response(json.dumps('Current user not connected.'), 401)
		response.headers['Content-Type'] = 'application/json'
		return response
	url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
	h = httplib2.Http()
	result = h.request(url, 'GET')[0]
	print 'result is '
	print result
	if result['status'] == '200':
		del login_session['access_token']
		del login_session['gplus_id']
		del login_session['username']
		del login_session['email']
		del login_session['picture']
		response = make_response(json.dumps('Successfully disconnected.'), 200)
		response.headers['Content-Type'] = 'application/json'
		return response
	else:
		response = make_response(json.dumps('Failed to revoke token for given user.', 400))
		response.headers['Content-Type'] = 'application/json'
		return response


@app.route('/')
@app.route('/catalog/')
def showCategory():
	categories = session.query(Category).all()
	return render_template('index.html', categories = categories)

@app.route('/catalog/new')
def newCategory():
	if 'username' not in login_session:
		return redirect('/login')
	return render_template('newCategory.html')

@app.route('/catalog/<int:category_id>/edit')
def editCategory(category_id):
	if 'username' not in login_session:
		return redirect('/login')
	return render_template('editCategory.html', category_id=category_id)

@app.route('/catalog/<int:category_id>/delete')
def deleteCategory(category_id):
	if 'username' not in login_session:
		return redirect('/login')
	return render_template('deleteCategory.html', category_id=category_id)

@app.route('/catalog/<int:category_id>/')
def showItems(category_id):
	categories = session.query(Category).all()
	category = session.query(Category).get(category_id)
	items = session.query(Item).filter_by(category_id=category_id).all()
	return render_template('items.html', categories=categories, category=category, items = items)

@app.route('/catalog/<int:category_id>/new/', methods = ['GET','POST'])
def newItem(category_id):
	if 'username' not in login_session:
		return redirect('/login')
	if request.method == 'POST':
		newItem = Item(name = request.form['name'], category_id=category_id)
		session.add(newItem)
		session.commit()
		flash("New item was added!")
		return redirect(url_for('showItems',category_id=category_id))
	else:
		return render_template('newItem.html', category_id=category_id)


@app.route('/catalog/<int:category_id>/<int:item_id>/edit/', methods = ['GET','POST'])
def editItem(category_id, item_id):
	if 'username' not in login_session:
		return redirect('/login')
	item = session.query(Item).filter_by(id = item_id).first()
	if request.method == 'POST':
		item.name	= request.form['newName']
		session.add(item)
		session.commit()
		flash("The item has been updated!")
		return redirect(url_for('showItems', category_id=category_id))
	else:
		return render_template('editItem.html', item=item)

@app.route('/catalog/<int:category_id>/<int:item_id>/delete/', methods = ['GET','POST'])
def deleteItem(category_id, item_id):
	if 'username' not in login_session:
		return redirect('/login')
	item = session.query(Item).filter_by(id = item_id).first()
	if request.method == 'POST':
		session.delete(item)
		session.commit()
		flash("The item has been deleted!")
		return redirect(url_for('showItems', category_id=category_id))
	else:
		return render_template('deleteItem.html', item=item)

#API endpoint (GET Request)
@app.route('/catalog/JSON')
def CategoriesJSON():
	categories = session.query(Category).all()
	return jsonify(Categories=[c.serialize for c in categories])

@app.route('/catalog/<int:category_id>/item/JSON')
def CategoryItemsJSON(category_id):
	category = session.query(Category).get(category_id)
	items = session.query(Item).filter_by(category_id=category_id).all()
	return jsonify(Items=[i.serialize for i in items])

@app.route('/catalog/<int:category_id>/<int:item_id>/JSON')
def ItemJSON(category_id, item_id):
	category = session.query(Category).get(category_id)
	item = session.query(Item).filter_by(id=item_id).one()
	return jsonify(Item=[item.serialize])

if __name__ == '__main__':
	app.secret_key = 'temp_secret_key'
	app.debug = True
	app.run(host='0.0.0.0', port=5000)