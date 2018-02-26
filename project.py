from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from catalog_dbsetup import Base, Category, Item, User
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



#takes in login_session and extract user.id
def createUser(login_session):
	newUser = User(name=login_session['username'], email=login_session['email'], picture=login_session['picture'])
	session.add(newUser)
	session.commit()
	user = session.query(User).filter_by(email=login_session['email']).one()
	return user.id 


def getUserInfo(user_id):
	user = session.query(User).filter_by(id= user_id).one()
	return user

def getUserID(email):
	try:
		user = session.query(User).filter_by(email=login_session['email']).one()
		return user.id
	except:
		return None 


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

	login_session['provider'] = 'google'
	login_session['username'] = data['name']
	login_session['picture'] = data['picture']
	login_session['email'] = data['email']

	user_id = getUserID(login_session['email'])
	if not user_id:
		user_id = createUser(login_session)
	login_session['user_id'] = user_id

	output = ''
	output += 'Welcome, '
	output += login_session['username']
	output += '!<br>'
	output += '<img src="'
	output += login_session['picture']
	output += ' " style = "width: 70px; border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
	flash("You are now logged in as %s" % login_session['username'])
	print "done!"
	return output


@app.route('/gdisconnect')
def gdisconnect():
	access_token = login_session.get('access_token')
	
	if access_token is None:
		print 'Access Token is None'
		response = make_response(json.dumps('Current user not connected.'), 401)
		response.headers['Content-Type'] = 'application/json'
		return response

	url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
	h = httplib2.Http()
	result = h.request(url, 'GET')[0]

	if result['status'] == '200':
		response = make_response(json.dumps('Successfully disconnected.'), 200)
		response.headers['Content-Type'] = 'application/json'
		return redirect(url_for('showCategory'))
	else:
		response = make_response(json.dumps('Failed to revoke token for given user.', 400))
		response.headers['Content-Type'] = 'application/json'
		return response


@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = request.data
    print "access token received %s " % access_token

    #exchange client token for long-lived server-side token with GET
    app_id = json.loads(
        open('fb_client_secrets.json', 'r').read())['web']['app_id']
    app_secret = json.loads(
        open('fb_client_secrets.json', 'r').read())['web']['app_secret']
    url = ('https://graph.facebook.com/v2.9/oauth/access_token?'
           'grant_type=fb_exchange_token&client_id=%s&client_secret=%s'
           '&fb_exchange_token=%s') % (app_id, app_secret, access_token)
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)
    token = 'access_token=' + data['access_token']

    # Use token to get user info from API
    # make API call with new token
    url = 'https://graph.facebook.com/v2.9/me?%s&fields=name,id,email,picture' % token
  
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)
    login_session['provider'] = 'facebook'
    login_session['username'] = data['name']
    login_session['email'] = data['email']
    login_session['facebook_id'] = data['id']
    login_session['picture'] = data['picture']["data"]["url"]
    login_session['access_token'] = access_token

    #see if user exists
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += 'Welcome, '
    output += login_session['username']
    output += '!<br>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 70px; border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("You are now logged in as %s" % login_session['username'])
    print "done!"
    return output


@app.route('/fbdisconnect')
def fbdisconnect():
    facebook_id = login_session['facebook_id']
    # The access token must be included to successfully logout
    access_token = login_session['access_token']
    url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % (facebook_id,access_token)
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]
    return "you have been logged out"


@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            del login_session['access_token']
        if login_session['provider'] == 'facebook':
            fbdisconnect()
            del login_session['facebook_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("You have been logged out.")
        return redirect(url_for('showCategory'))
    else:
        flash("You were not logged in")
        return redirect(url_for('showCategory'))


@app.route('/')
@app.route('/catalog/')
def showCategory():
	categories = session.query(Category).all()
	firstitems = [];
	for c in categories:
		firstitem = session.query(Item).filter_by(category_id=c.id).first()
		firstitems.append(firstitem)
	if 'username' not in login_session:
		return render_template('publicmain.html', categories = categories, firstitems = firstitems)
	user = getUserInfo(login_session['user_id'])
	return render_template('index.html', categories = categories, firstitems = firstitems, user=user)


@app.route('/catalog/new',methods = ['GET','POST'])
def newCategory():
	if 'username' not in login_session:
		return redirect('/login')
	if request.method == 'POST':
			newCategory = Category(name = request.form['name'], user_id=login_session['user_id'])
			session.add(newCategory)
			session.commit()
			flash("New category %s was successfully created!" %newCategory.name)
			return redirect(url_for('showCategory'))
	else:
		categories = session.query(Category).all()
		user = getUserInfo(login_session['user_id'])
		return render_template('newCategory.html', user=user)

@app.route('/catalog/<int:category_id>/edit', methods = ['GET','POST'])
def editCategory(category_id):
	if 'username' not in login_session:
		return redirect('/login')
	category = session.query(Category).filter_by(id= category_id).first()
	if category.user_id != login_session['user_id']:
		flash("You are not authorized to edit this category!")
		return redirect(url_for('showCategory'))
	if request.method == 'POST':
		category.name	= request.form['name']
		session.add(category)
		session.commit()
		flash("The category has been updated!")
		return redirect(url_for('showCategory'))
	else:
		user = getUserInfo(login_session['user_id'])
		return render_template('editCategory.html', category=category, user=user)

@app.route('/catalog/<int:category_id>/delete', methods = ['GET','POST'])
def deleteCategory(category_id):
	if 'username' not in login_session:
		return redirect('/login')
	category = session.query(Category).filter_by(id= category_id).first()
	firstitem = session.query(Item).filter_by(category_id=category_id).first()
	if category.user_id != login_session['user_id']:
		flash("You are not authorized to delete this category!")
		return redirect(url_for('showCategory'))
	if request.method == 'POST':
		session.delete(category)
		session.commit()	
		flash("The category has been deleted!")	
		return redirect(url_for('showCategory'))
	else:
		user = getUserInfo(login_session['user_id'])
		return render_template('deleteCategory.html', category=category, firstitem=firstitem, user=user)

@app.route('/catalog/<int:category_id>/')
def showItems(category_id):
	categories = session.query(Category).all()
	category = session.query(Category).get(category_id)
	items = session.query(Item).filter_by(category_id=category_id).all()
	if 'username' not in login_session:
		return render_template('publicitems.html', categories=categories,category=category, items = items)
	user = getUserInfo(login_session['user_id'])
	return render_template('items.html', categories=categories, category=category, items = items, user=user)

@app.route('/catalog/<int:category_id>/new/', methods = ['GET','POST'])
def newItem(category_id):
	if 'username' not in login_session:
		return redirect('/login')
	if request.method == 'POST':
		newItem = Item(name = request.form['name'], img= request.form['img'], brand= request.form['brand'], shopURL= request.form['shopURL'], price= request.form['price'], category_id=category_id, user_id=login_session['user_id'])
		session.add(newItem)
		session.commit()
		flash("New item %s was successfully Created!" %newItem.name)
		return redirect(url_for('showItems',category_id=category_id))
	else:
		categories = session.query(Category).all()
		user = getUserInfo(login_session['user_id'])
		return render_template('newItem.html',  categories=categories, category_id=category_id, user=user)


@app.route('/catalog/<int:category_id>/<int:item_id>/edit/', methods = ['GET','POST'])
def editItem(category_id, item_id):
	if 'username' not in login_session:
		return redirect('/login')
	item = session.query(Item).filter_by(id = item_id).first()
	if item.user_id != login_session['user_id']:
		flash("You are not authorized to edit this item!")
		return redirect(url_for('showItems', category_id=category_id))
	if request.method == 'POST':
		item.name	= request.form['name']
		item.img= request.form['img']
		item.brand= request.form['brand']
		item.shopURL= request.form['shopURL']
		item.price= request.form['price']
		flash("The item has been updated!")
		return redirect(url_for('showItems', category_id=category_id))
	else:
		user = getUserInfo(login_session['user_id'])
		return render_template('editItem.html', category_id=category_id, item_id=item_id, item=item, user=user)

@app.route('/catalog/<int:category_id>/<int:item_id>/delete/', methods = ['GET','POST'])
def deleteItem(category_id, item_id):
	if 'username' not in login_session:
		return redirect('/login')
	item = session.query(Item).filter_by(id = item_id).first()
	if item.user_id != login_session['user_id']:
		flash("You are not authorized to delete this item!")
		return redirect(url_for('showItems', category_id=category_id))
	if request.method == 'POST':
		session.delete(item)
		session.commit()
		flash("The item has been deleted!")
		return redirect(url_for('showItems', category_id=category_id))
	else:
		user = getUserInfo(login_session['user_id'])
		return render_template('deleteItem.html', category_id=category_id, item_id=item_id, item=item, user=user)

#JSON API endpoints to view Catalog 
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