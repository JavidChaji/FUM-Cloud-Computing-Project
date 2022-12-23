from flask import Flask, render_template, request, url_for, redirect, flash
import datetime
from MyUtils import UseDatabase

app = Flask(__name__)

@app.route('/')
def index():
	return(render_template('index.html', heading="Index page", index_actor_link=url_for("actors_index"), index_address_link=url_for("addresses_index"), index_category_link=url_for("categories_index"), index_city_link=url_for("cities_index"), index_country_link=url_for("countries_index"), index_customer_link=url_for("customers_index"), index_film_link=url_for("films_index"), index_filmtext_link=url_for("filmtexts_index"), index_inventory_link=url_for("inventories_index"), index_language_link=url_for("languages_index"), index_payment_link=url_for("payments_index"), index_rental_link=url_for("rentals_index"), index_staff_link=url_for("staffs_index"), index_store_link=url_for("stores_index")))

# =============================================================================================
# ACTORS
# =============================================================================================

# ACTORS INDEX
@app.route('/actors/index', methods=['GET', 'POST'])
def actors_index():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from actors"""
		cursor.execute(SQL)
		actors_list = cursor.fetchall()
	return(render_template('/actors/index.html', heading="Listing actors", actors=actors_list, show_actor_link=url_for("show_actor"), update_actor_link=url_for("update_actor"), delete_actor_link=url_for("delete_actor"), create_actor_link=url_for("create_actor")))

# ACTORS DELETE
@app.route('/actors/delete', methods=['POST'])
def delete_actor():
	SQL = """delete from actors where id = %s"""
	with UseDatabase(app.config) as cursor:
		cursor.execute(SQL, (request.form['id'],))
	return(redirect(url_for("actors_index")))	

# ACTORS CREATE
@app.route('/actors/create', methods=['GET', 'POST'])
def create_actor():
	return(render_template("/actors/create.html", heading="Create a new Actor", index_actor_link=url_for("actors_index"), save_actor_link=url_for("save_actor")))

# ACTORS CREATE SAVE
@app.route('/actors/save', methods=['POST'])
def save_actor():
	INSERT = """insert into actors (first_name, last_name) VALUES (%s, %s)"""
	all_ok = True
	if len(request.form['first_name']) == 0:
		all_ok = False
		flash("Sorry the actor's first name cannot be empty. Try again")
	if len(request.form['last_name']) == 0:
		all_ok = False
		flash("Sorry the actor's last name cannot be empty. Try again")
	if all_ok:
		with UseDatabase(app.config) as cursor:
			cursor.execute(INSERT, (request.form['first_name'], request.form['last_name']))
			SELECTALL = """select * from actors"""
			cursor.execute(SELECTALL)
			actors_list = cursor.fetchall()
		return(render_template('/actors/index.html', heading="Listing actors", actors=actors_list, show_actor_link=url_for("show_actor"), update_actor_link=url_for("update_actor"), delete_actor_link=url_for("delete_actor"), create_actor_link=url_for("create_actor")))
	else:
		return(redirect(url_for("create_actor")))

# ACTORS UPDATE
@app.route('/actors/update', methods=['POST'])
def update_actor():
	with UseDatabase(app.config) as cursor:
		ACTOR = """select * from actors where id = %s"""
		cursor.execute(ACTOR, (request.form['id'],))
		actor_info = cursor.fetchall()
	return(render_template("/actors/update.html", heading="Editing actor", actor=actor_info, show_actor_link=url_for("show_actor"), index_actor_link=url_for("actors_index"), update_actor_save_link=url_for("save_actor_changes")))

# ACTORS UPDATE SAVE
@app.route('/actors/update_save', methods=['POST'])
def save_actor_changes():
	with UseDatabase(app.config) as cursor:
		UPDATE = """update actors set first_name = %s, last_name = %s where id = %s"""
		cursor.execute(UPDATE, (request.form['first_name'], request.form['last_name'], request.form['id']))
		SELECT = """select * from actors"""
		cursor.execute(SELECT)
		actors_list = cursor.fetchall()
	return(render_template('/actors/index.html', heading="Listing actors", actors=actors_list, show_actor_link=url_for("show_actor"), update_actor_link=url_for("update_actor"), delete_actor_link=url_for("delete_actor"), create_actor_link=url_for("create_actor")))

# ACTORS SHOW
@app.route('/actors/show', methods=['POST'])
def show_actor():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from actors where id = %s"""
		cursor.execute(SQL, (request.form['id'],))
		actor_info = cursor.fetchall()
	return(render_template('/actors/show.html', actor=actor_info, index_actor_link=url_for("actors_index"), update_actor_link=url_for("update_actor")))

# =============================================================================================
# ADDRESSES
# =============================================================================================

# ADDRESSES INDEX
@app.route('/addresses/index', methods=['GET', 'POST'])
def addresses_index():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from addresses"""
		cursor.execute(SQL)
		addresses_list = cursor.fetchall()
	return(render_template('/addresses/index.html', heading="Listing addresses", addresses=addresses_list, show_address_link=url_for("show_address"), update_address_link=url_for("update_address"), delete_address_link=url_for("delete_address"), create_address_link=url_for("create_address")))

# ADDRESSES DELETE
@app.route('/addresses/delete', methods=['POST'])
def delete_address():
	SQL = """delete from addresses where id = %s"""
	with UseDatabase(app.config) as cursor:
		cursor.execute(SQL, (request.form['id'],))
	return(redirect(url_for("addresses_index")))	

# ADDRESSES CREATE
@app.route('/addresses/create', methods=['GET', 'POST'])
def create_address():
	return(render_template("/addresses/create.html", heading="Create a new Address", index_address_link=url_for("addresses_index"), save_address_link=url_for("save_address")))

# ADDRESSES CREATE SAVE
@app.route('/addresses/save', methods=['POST'])
def save_address():
	INSERT = """insert into addresses (address, district, city_id, postal_code, phone) VALUES (%s, %s, %s, %s, %s)"""
	all_ok = True
	if len(request.form['address']) == 0:
		all_ok = False
		flash("Sorry the address cannot be empty. Try again")
	if len(request.form['district']) == 0:
		all_ok = False
		flash("Sorry the district cannot be empty. Try again")
	if len(request.form['city_id']) == 0:
		all_ok = False
		flash("Sorry the city id cannot be empty. Try again")
	if len(request.form['postal_code']) == 0:
		all_ok = False
		flash("Sorry the postal code cannot be empty. Try again")
	if len(request.form['phone']) == 0:
		all_ok = False
		flash("Sorry the phone cannot be empty. Try again")
	if all_ok:
		with UseDatabase(app.config) as cursor:
			cursor.execute(INSERT, (request.form['address'], request.form['district'], request.form['city_id'], request.form['postal_code'], request.form['phone'],))
			SELECTALL = """select * from addresses"""
			cursor.execute(SELECTALL)
			addresses_list = cursor.fetchall()	
		return(render_template('/addresses/index.html', heading="Listing addresses", addresses=addresses_list, show_address_link=url_for("show_address"), update_address_link=url_for("update_address"), delete_address_link=url_for("delete_address"), create_address_link=url_for("create_address")))
	else:
		return(redirect(url_for("create_address")))

# ADDRESSES UPDATE
@app.route('/addresses/update', methods=['POST'])
def update_address():
	with UseDatabase(app.config) as cursor:
		ADDRESS = """select * from addresses where id = %s"""
		cursor.execute(ADDRESS, (request.form['id'],))
		address_info = cursor.fetchall()
	return(render_template("/addresses/update.html", heading="Editing address", address=address_info, show_address_link=url_for("show_address"), index_address_link=url_for("addresses_index"), update_address_save_link=url_for("save_address_changes")))

# ADDRESSES UPDATE SAVE
@app.route('/addresses/update_save', methods=['POST'])
def save_address_changes():
	with UseDatabase(app.config) as cursor:
		UPDATE = """update addresses set address = %s, district = %s, city_id = %s, postal_code = %s, phone = %s where id = %s"""
		cursor.execute(UPDATE, (request.form['address'], request.form['district'], request.form['city_id'], request.form['postal_code'], request.form['phone'], request.form['id']))
		SELECT = """select * from addresses"""
		cursor.execute(SELECT)
		addresses_list = cursor.fetchall()
	return(render_template('/addresses/index.html', heading="Listing addresses", addresses=addresses_list, show_address_link=url_for("show_address"), update_address_link=url_for("update_address"), delete_address_link=url_for("delete_address"), create_address_link=url_for("create_address")))

# ADDRESSES SHOW
@app.route('/addresses/show', methods=['POST'])
def show_address():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from addresses where id = %s"""
		cursor.execute(SQL, (request.form['id'],))
		address_info = cursor.fetchall()
	return(render_template('/addresses/show.html', address=address_info, index_address_link=url_for("addresses_index"), update_address_link=url_for("update_address")))

# =============================================================================================
# CATEGORIES
# =============================================================================================

# CATEGORIES INDEX
@app.route('/categories/index', methods=['GET', 'POST'])
def categories_index():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from categories"""
		cursor.execute(SQL)
		categories_list = cursor.fetchall()
	return(render_template('/categories/index.html', heading="Listing categories", categories=categories_list, show_category_link=url_for("show_category"), update_category_link=url_for("update_category"), delete_category_link=url_for("delete_category"), create_category_link=url_for("create_category")))

# CATEGORIES DELETE
@app.route('/categories/delete', methods=['POST'])
def delete_category():
	SQL = """delete from categories where id = %s"""
	with UseDatabase(app.config) as cursor:
		cursor.execute(SQL, (request.form['id'],))
	return(redirect(url_for("categories_index")))	

# CATEGORIES CREATE
@app.route('/categories/create', methods=['GET', 'POST'])
def create_category():
	return(render_template("/categories/create.html", heading="Create a new Category", index_category_link=url_for("categories_index"), save_category_link=url_for("save_category")))

# CATEGORIES CREATE SAVE
@app.route('/categories/save', methods=['POST'])
def save_category():
	INSERT = """insert into categories (name) VALUES (%s)"""
	all_ok = True
	if len(request.form['name']) == 0:
		all_ok = False
		flash("Sorry the categorie's name cannot be empty. Try again")
	if all_ok:
		with UseDatabase(app.config) as cursor:
			cursor.execute(INSERT, (request.form['name'],))
			SELECTALL = """select * from categories"""
			cursor.execute(SELECTALL)
			categories_list = cursor.fetchall()
		return(render_template('/categories/index.html', heading="Listing categories", categories=categories_list, show_category_link=url_for("show_category"), update_category_link=url_for("update_category"), delete_category_link=url_for("delete_category"), create_category_link=url_for("create_category")))
	else:
		return(redirect(url_for("create_category")))

# CATEGORIES UPDATE
@app.route('/categories/update', methods=['POST'])
def update_category():
	with UseDatabase(app.config) as cursor:
		CATEGORY = """select * from categories where id = %s"""
		cursor.execute(CATEGORY, (request.form['id'],))
		category_info = cursor.fetchall()
	return(render_template("/categories/update.html", heading="Editing category", category=category_info, show_category_link=url_for("show_category"), index_category_link=url_for("categories_index"), update_category_save_link=url_for("save_category_changes")))

# CATEGORIES UPDATE SAVE
@app.route('/categories/update_save', methods=['POST'])
def save_category_changes():
	with UseDatabase(app.config) as cursor:
		UPDATE = """update categories set name = %s where id = %s"""
		cursor.execute(UPDATE, (request.form['name'], request.form['id']))
		SELECT = """select * from categories"""
		cursor.execute(SELECT)
		categories_list = cursor.fetchall()
	return(render_template('/categories/index.html', heading="Listing categories", categories=categories_list, show_category_link=url_for("show_category"), update_category_link=url_for("update_category"), delete_category_link=url_for("delete_category"), create_category_link=url_for("create_category")))

# CATEGORIES SHOW
@app.route('/categories/show', methods=['POST'])
def show_category():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from categories where id = %s"""
		cursor.execute(SQL, (request.form['id'],))
		category_info = cursor.fetchall()
	return(render_template('/categories/show.html', category=category_info, index_category_link=url_for("categories_index"), update_category_link=url_for("update_category")))

# =============================================================================================
# CITIES
# =============================================================================================

# CITIES INDEX
@app.route('/cities/index', methods=['GET', 'POST'])
def cities_index():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from cities"""
		cursor.execute(SQL)
		cities_list = cursor.fetchall()
	return(render_template('/cities/index.html', heading="Listing cities", cities=cities_list, show_city_link=url_for("show_city"), update_city_link=url_for("update_city"), delete_city_link=url_for("delete_city"), create_city_link=url_for("create_city")))

# CITIES DELETE
@app.route('/cities/delete', methods=['POST'])
def delete_city():
	SQL = """delete from cities where id = %s"""
	with UseDatabase(app.config) as cursor:
		cursor.execute(SQL, (request.form['id'],))
	return(redirect(url_for("cities_index")))	

# CITIES CREATE
@app.route('/cities/create', methods=['GET', 'POST'])
def create_city():
	return(render_template("/cities/create.html", heading="Create a new City", index_city_link=url_for("cities_index"), save_city_link=url_for("save_city")))

# CITIES CREATE SAVE
@app.route('/cities/save', methods=['POST'])
def save_city():
	INSERT = """insert into cities (city, country_id) VALUES (%s, %s)"""
	all_ok = True
	if len(request.form['city']) == 0:
		all_ok = False
		flash("Sorry the city name cannot be empty. Try again")
	if len(request.form['country_id']) == 0:
		all_ok = False
		flash("Sorry the country's id cannot be empty. Try again")
	if all_ok:
		with UseDatabase(app.config) as cursor:
			cursor.execute(INSERT, (request.form['city'], request.form['country_id']))
			SELECTALL = """select * from cities"""
			cursor.execute(SELECTALL)
			cities_list = cursor.fetchall()
		return(render_template('/cities/index.html', heading="Listing cities", cities=cities_list, show_city_link=url_for("show_city"), update_city_link=url_for("update_city"), delete_city_link=url_for("delete_city"), create_city_link=url_for("create_city")))
	else:
		return(redirect(url_for("create_city")))

# CITIES UPDATE
@app.route('/cities/update', methods=['POST'])
def update_city():
	with UseDatabase(app.config) as cursor:
		CITY = """select * from cities where id = %s"""
		cursor.execute(CITY, (request.form['id'],))
		city_info = cursor.fetchall()
	return(render_template("/cities/update.html", heading="Editing city", city=city_info, show_city_link=url_for("show_city"), index_city_link=url_for("cities_index"), update_city_save_link=url_for("save_city_changes")))

# CITIES UPDATE SAVE
@app.route('/cities/update_save', methods=['POST'])
def save_city_changes():
	with UseDatabase(app.config) as cursor:
		UPDATE = """update cities set city = %s, country_id = %s where id = %s"""
		cursor.execute(UPDATE, (request.form['city'], request.form['country_id'], request.form['id']))
		SELECT = """select * from cities"""
		cursor.execute(SELECT)
		cities_list = cursor.fetchall()
	return(render_template('/cities/index.html', heading="Listing cities", cities=cities_list, show_city_link=url_for("show_city"), update_city_link=url_for("update_city"), delete_city_link=url_for("delete_city"), create_city_link=url_for("create_city")))

# CITIES SHOW
@app.route('/cities/show', methods=['POST'])
def show_city():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from cities where id = %s"""
		cursor.execute(SQL, (request.form['id'],))
		city_info = cursor.fetchall()
	return(render_template('/cities/show.html', city=city_info, index_city_link=url_for("cities_index"), update_city_link=url_for("update_city")))

# =============================================================================================
# COUNTRIES
# =============================================================================================

# COUNTRIES INDEX
@app.route('/countries/index', methods=['GET', 'POST'])
def countries_index():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from countries"""
		cursor.execute(SQL)
		countries_list = cursor.fetchall()
	return(render_template('/countries/index.html', heading="Listing countries", countries=countries_list, show_country_link=url_for("show_country"), update_country_link=url_for("update_country"), delete_country_link=url_for("delete_country"), create_country_link=url_for("create_country")))

# COUNTRIES DELETE
@app.route('/countries/delete', methods=['POST'])
def delete_country():
	SQL = """delete from countries where id = %s"""
	with UseDatabase(app.config) as cursor:
		cursor.execute(SQL, (request.form['id'],))
	return(redirect(url_for("countries_index")))	

# COUNTRIES CREATE
@app.route('/countries/create', methods=['GET', 'POST'])
def create_country():
	return(render_template("/countries/create.html", heading="Create a new Country", index_country_link=url_for("countries_index"), save_country_link=url_for("save_country")))

# COUNTRIES CREATE SAVE
@app.route('/countries/save', methods=['POST'])
def save_country():
	INSERT = """insert into countries (country) VALUES (%s)"""
	all_ok = True
	if len(request.form['country']) == 0:
		all_ok = False
		flash("Sorry the country name cannot be empty. Try again")
	if all_ok:
		with UseDatabase(app.config) as cursor:
			cursor.execute(INSERT, (request.form['country'],))
			SELECTALL = """select * from countries"""
			cursor.execute(SELECTALL)
			countries_list = cursor.fetchall()
		return(render_template('/countries/index.html', heading="Listing countries", countries=countries_list, show_country_link=url_for("show_country"), update_country_link=url_for("update_country"), delete_country_link=url_for("delete_country"), create_country_link=url_for("create_country")))
	else:
		return(redirect(url_for("create_country")))

# COUNTRIES UPDATE
@app.route('/countries/update', methods=['POST'])
def update_country():
	with UseDatabase(app.config) as cursor:
		COUNTRY = """select * from countries where id = %s"""
		cursor.execute(COUNTRY, (request.form['id'],))
		country_info = cursor.fetchall()
	return(render_template("/countries/update.html", heading="Editing country", country=country_info, show_country_link=url_for("show_country"), index_country_link=url_for("countries_index"), update_country_save_link=url_for("save_country_changes")))

# COUNTRIES UPDATE SAVE
@app.route('/countries/update_save', methods=['POST'])
def save_country_changes():
	with UseDatabase(app.config) as cursor:
		UPDATE = """update countries set country = %s where id = %s"""
		cursor.execute(UPDATE, (request.form['country'], request.form['id']))
		SELECT = """select * from countries"""
		cursor.execute(SELECT)
		countries_list = cursor.fetchall()
	return(render_template('/countries/index.html', heading="Listing countries", countries=countries_list, show_country_link=url_for("show_country"), update_country_link=url_for("update_country"), delete_country_link=url_for("delete_country"), create_country_link=url_for("create_country")))

# COUNTRIES SHOW
@app.route('/countries/show', methods=['POST'])
def show_country():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from countries where id = %s"""
		cursor.execute(SQL, (request.form['id'],))
		country_info = cursor.fetchall()
	return(render_template('/countries/show.html', country=country_info, index_country_link=url_for("countries_index"), update_country_link=url_for("update_country")))

# =============================================================================================
# CUSTOMERS
# =============================================================================================

# CUSTOMERS INDEX
@app.route('/customers/index', methods=['GET', 'POST'])
def customers_index():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from customers"""
		cursor.execute(SQL)
		customers_list = cursor.fetchall()
	return(render_template('/customers/index.html', heading="Listing customers", customers=customers_list, show_customer_link=url_for("show_customer"), update_customer_link=url_for("update_customer"), delete_customer_link=url_for("delete_customer"), create_customer_link=url_for("create_customer")))

# CUSTOMERS DELETE
@app.route('/customers/delete', methods=['POST'])
def delete_customer():
	SQL = """delete from customers where id = %s"""
	with UseDatabase(app.config) as cursor:
		cursor.execute(SQL, (request.form['id'],))
	return(redirect(url_for("customers_index")))	

# CUSTOMERS CREATE
@app.route('/customers/create', methods=['GET', 'POST'])
def create_customer():
	return(render_template("/customers/create.html", heading="Create a new Customer", index_customer_link=url_for("customers_index"), save_customer_link=url_for("save_customer")))

# CUSTOMERS CREATE SAVE
@app.route('/customers/save', methods=['POST'])
def save_customer():
	if request.form['active'] == 'on':
		checkbox = 1;
	else:
		checkbox = 0;
	INSERT = """insert into customers (store_id, first_name, last_name, email, address_id, active, create_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
	all_ok = True
	if len(request.form['first_name']) == 0:
		all_ok = False
		flash("Sorry the customer's first name cannot be empty. Try again")
	if len(request.form['last_name']) == 0:
		all_ok = False
		flash("Sorry the customer's last name cannot be empty. Try again")
	if len(request.form['email']) == 0:
		all_ok = False
		flash("Sorry the customer's email cannot be empty. Try again")
	if all_ok:
		with UseDatabase(app.config) as cursor:
			current_time = datetime.datetime.now().time()
			cursor.execute(INSERT, (request.form['store_id'], request.form['first_name'], request.form['last_name'], request.form['email'], request.form['address_id'], checkbox, current_time.strftime('%Y-%m-%d %H:%M:%S'),))
			SELECTALL = """select * from customers"""
			cursor.execute(SELECTALL)
			customers_list = cursor.fetchall()
		return(render_template('/customers/index.html', heading="Listing customers", customers=customers_list, show_customer_link=url_for("show_customer"), update_customer_link=url_for("update_customer"), delete_customer_link=url_for("delete_customer"), create_customer_link=url_for("create_customer")))
	else:
		return(redirect(url_for("create_customer")))

# CUSTOMERS UPDATE
@app.route('/customers/update', methods=['POST'])
def update_customer():
	with UseDatabase(app.config) as cursor:
		CUSTOMER = """select * from customers where id = %s"""
		cursor.execute(CUSTOMER, (request.form['id'],))
		customer_info = cursor.fetchall()
	return(render_template("/customers/update.html", heading="Editing customer", customer=customer_info, show_customer_link=url_for("show_customer"), index_customer_link=url_for("customers_index"), update_customer_save_link=url_for("save_customer_changes")))

# CUSTOMERS UPDATE SAVE
@app.route('/customers/update_save', methods=['POST'])
def save_customer_changes():
	with UseDatabase(app.config) as cursor:
		if request.form['active'] == 'on':
			checkbox = 1;
		else:
			checkbox = 0;
		UPDATE = """update customers set store_id = %s, first_name = %s, last_name = %s, email = %s, address_id = %s, active = %s where id = %s"""
		cursor.execute(UPDATE, (request.form['store_id'], request.form['first_name'], request.form['last_name'], request.form['email'], request.form['address_id'], checkbox, request.form['id']))
		SELECT = """select * from customers"""
		cursor.execute(SELECT)
		customers_list = cursor.fetchall()
	return(render_template('/customers/index.html', heading="Listing customers", customers=customers_list, show_customer_link=url_for("show_customer"), update_customer_link=url_for("update_customer"), delete_customer_link=url_for("delete_customer"), create_customer_link=url_for("create_customer")))

# CUSTOMERS SHOW
@app.route('/customers/show', methods=['POST'])
def show_customer():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from customers where id = %s"""
		cursor.execute(SQL, (request.form['id'],))
		customer_info = cursor.fetchall()
	return(render_template('/customers/show.html', customer=customer_info, index_customer_link=url_for("customers_index"), update_customer_link=url_for("update_customer")))

# =============================================================================================
# FILMS
# =============================================================================================

# FILMS INDEX
@app.route('/films/index', methods=['GET', 'POST'])
def films_index():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from films"""
		cursor.execute(SQL)
		films_list = cursor.fetchall()
	return(render_template('/films/index.html', heading="Listing films", films=films_list, show_film_link=url_for("show_film"), update_film_link=url_for("update_film"), delete_film_link=url_for("delete_film"), create_film_link=url_for("create_film")))

# FILMS DELETE
@app.route('/films/delete', methods=['POST'])
def delete_film():
	SQL = """delete from films where id = %s"""
	with UseDatabase(app.config) as cursor:
		cursor.execute(SQL, (request.form['id'],))
	return(redirect(url_for("films_index")))	

# FILMS CREATE
@app.route('/films/create', methods=['GET', 'POST'])
def create_film():
	return(render_template("/films/create.html", heading="Create a new Film", index_film_link=url_for("films_index"), save_film_link=url_for("save_film")))

# FILMS CREATE SAVE
@app.route('/films/save', methods=['POST'])
def save_film():
	INSERT = """insert into films (title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
	all_ok = True
	if len(request.form['title']) == 0:
		all_ok = False
		flash("Sorry the film's title cannot be empty. Try again")
	if len(request.form['description']) == 0:
		all_ok = False
		flash("Sorry the film's description cannot be empty. Try again")
	if all_ok:
		with UseDatabase(app.config) as cursor:
			cursor.execute(INSERT, (request.form['title'], request.form['description'], request.form['release_year'], request.form['language_id'], request.form['rental_duration'], request.form['rental_rate'], request.form['length'], request.form['replacement_cost'], request.form['rating'], request.form['special_features'],))
			SELECTALL = """select * from films"""
			cursor.execute(SELECTALL)
			films_list = cursor.fetchall()
		return(render_template('/films/index.html', heading="Listing films", films=films_list, show_film_link=url_for("show_film"), update_film_link=url_for("update_film"), delete_film_link=url_for("delete_film"), create_film_link=url_for("create_film")))
	else:
		return(redirect(url_for("create_film")))

# FILMS UPDATE
@app.route('/films/update', methods=['POST'])
def update_film():
	with UseDatabase(app.config) as cursor:
		FILM = """select * from films where id = %s"""
		cursor.execute(FILM, (request.form['id'],))
		film_info = cursor.fetchall()
	return(render_template("/films/update.html", heading="Editing film", film=film_info, show_film_link=url_for("show_film"), index_film_link=url_for("films_index"), update_film_save_link=url_for("save_film_changes")))

# FILMS UPDATE SAVE
@app.route('/films/update_save', methods=['POST'])
def save_film_changes():
	with UseDatabase(app.config) as cursor:
		UPDATE = """update films set title = %s, description = %s, release_year = %s, language_id = %s, rental_duration = %s, rental_rate = %s, length = %s, replacement_cost = %s, rating = %s, special_features = %s where id = %s"""
		cursor.execute(UPDATE, (request.form['title'], request.form['description'], request.form['release_year'], request.form['language_id'], request.form['rental_duration'], request.form['rental_rate'], request.form['length'], request.form['replacement_cost'], request.   form['rating'], request.form['special_features'], request.form['id'],))
		SELECT = """select * from films"""
		cursor.execute(SELECT)
		films_list = cursor.fetchall()
	return(render_template('/films/index.html', heading="Listing films", films=films_list, show_film_link=url_for("show_film"), update_film_link=url_for("update_film"), delete_film_link=url_for("delete_film"), create_film_link=url_for("create_film")))

# FILMS SHOW
@app.route('/films/show', methods=['POST'])
def show_film():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from films where id = %s"""
		cursor.execute(SQL, (request.form['id'],))
		film_info = cursor.fetchall()
	return(render_template('/films/show.html', film=film_info, index_film_link=url_for("films_index"), update_film_link=url_for("update_film")))

# =============================================================================================
# FILM TEXTS
# =============================================================================================

# FILMS TEXTS INDEX
@app.route('/filmtexts/index', methods=['GET', 'POST'])
def filmtexts_index():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from filmtexts"""
		cursor.execute(SQL)
		filmtexts_list = cursor.fetchall()
	return(render_template('/filmtexts/index.html', heading="Listing film texts", filmtexts=filmtexts_list, show_filmtext_link=url_for("show_filmtext"), update_filmtext_link=url_for("update_filmtext"), delete_filmtext_link=url_for("delete_filmtext"), create_filmtext_link=url_for("create_filmtext")))

# FILMS TEXTS DELETE
@app.route('/filmtexts/delete', methods=['POST'])
def delete_filmtext():
	SQL = """delete from filmtexts where id = %s"""
	with UseDatabase(app.config) as cursor:
		cursor.execute(SQL, (request.form['id'],))
	return(redirect(url_for("filmtexts_index")))	

# FILMS TEXTS CREATE
@app.route('/filmtexts/create', methods=['GET', 'POST'])
def create_filmtext():
	return(render_template("/filmtexts/create.html", heading="Create a new Film Text", index_filmtext_link=url_for("filmtexts_index"), save_filmtext_link=url_for("save_filmtext")))

# FILMS TEXTS CREATE SAVE
@app.route('/filmtexts/save', methods=['POST'])
def save_filmtext():
	INSERT = """insert into filmtexts (title, description) VALUES (%s, %s)"""
	all_ok = True
	if len(request.form['title']) == 0:
		all_ok = False
		flash("Sorry the film text's title cannot be empty. Try again")
	if len(request.form['description']) == 0:
		all_ok = False
		flash("Sorry the film text's description cannot be empty. Try again")
	if all_ok:
		with UseDatabase(app.config) as cursor:
			cursor.execute(INSERT, (request.form['title'], request.form['description']))
			SELECTALL = """select * from filmtexts"""
			cursor.execute(SELECTALL)
			filmtexts_list = cursor.fetchall()
		return(render_template('/filmtexts/index.html', heading="Listing filmtexts", filmtexts=filmtexts_list, show_filmtext_link=url_for("show_filmtext"), update_filmtext_link=url_for("update_filmtext"), delete_filmtext_link=url_for("delete_filmtext"), create_filmtext_link=url_for("create_filmtext")))
	else:
		return(redirect(url_for("create_filmtext")))

# FILMS TEXTS UPDATE
@app.route('/filmtexts/update', methods=['POST'])
def update_filmtext():
	with UseDatabase(app.config) as cursor:
		FILMTEXT = """select * from filmtexts where id = %s"""
		cursor.execute(FILMTEXT, (request.form['id'],))
		filmtext_info = cursor.fetchall()
	return(render_template("/filmtexts/update.html", heading="Editing film text", filmtext=filmtext_info, show_filmtext_link=url_for("show_filmtext"), index_filmtext_link=url_for("filmtexts_index"), update_filmtext_save_link=url_for("save_filmtext_changes")))

# FILMS TEXTS UPDATE SAVE
@app.route('/filmtexts/update_save', methods=['POST'])
def save_filmtext_changes():
	with UseDatabase(app.config) as cursor:
		UPDATE = """update filmtexts set title = %s, description = %s where id = %s"""
		cursor.execute(UPDATE, (request.form['title'], request.form['description'], request.form['id']))
		SELECT = """select * from filmtexts"""
		cursor.execute(SELECT)
		filmtexts_list = cursor.fetchall()
	return(render_template('/filmtexts/index.html', heading="Listing film texts", filmtexts=filmtexts_list, show_filmtext_link=url_for("show_filmtext"), update_filmtext_link=url_for("update_filmtext"), delete_filmtext_link=url_for("delete_filmtext"), create_filmtext_link=url_for("create_filmtext")))

# FILMS TEXTS SHOW
@app.route('/filmtexts/show', methods=['POST'])
def show_filmtext():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from filmtexts where id = %s"""
		cursor.execute(SQL, (request.form['id'],))
		filmtext_info = cursor.fetchall()
	return(render_template('/filmtexts/show.html', filmtext=filmtext_info, index_filmtext_link=url_for("filmtexts_index"), update_filmtext_link=url_for("update_filmtext")))



# =============================================================================================
# INVENTORIES						
# =============================================================================================

# INVENTORIES INDEX
@app.route('/inventories/index', methods=['GET', 'POST'])
def inventories_index():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from inventories"""
		cursor.execute(SQL)
		inventories_list = cursor.fetchall()
	return(render_template('/inventories/index.html', heading="Listing inventories", inventories=inventories_list, show_inventory_link=url_for("show_inventory"), update_inventory_link=url_for("update_inventory"), delete_inventory_link=url_for("delete_inventory"), create_inventory_link=url_for("create_inventory")))

# INVENTORIES DELETE
@app.route('/inventories/delete', methods=['POST'])
def delete_inventory():
	SQL = """delete from inventories where id = %s"""
	with UseDatabase(app.config) as cursor:
		cursor.execute(SQL, (request.form['id'],))
	return(redirect(url_for("inventories_index")))	

# INVENTORIES CREATE
@app.route('/inventories/create', methods=['GET', 'POST'])
def create_inventory():
	return(render_template("/inventories/create.html", heading="Create a new Inventory", index_inventory_link=url_for("inventories_index"), save_inventory_link=url_for("save_inventory")))

# INVENTORIES CREATE SAVE
@app.route('/inventories/save', methods=['POST'])
def save_inventory():
	INSERT = """insert into inventories (film_id, store_id) VALUES (%s, %s)"""
	with UseDatabase(app.config) as cursor:
		cursor.execute(INSERT, (request.form['film_id'], request.form['store_id']))
		SELECTALL = """select * from inventories"""
		cursor.execute(SELECTALL)
		inventories_list = cursor.fetchall()
	return(render_template('/inventories/index.html', heading="Listing inventories", inventories=inventories_list, show_inventory_link=url_for("show_inventory"), update_inventory_link=url_for("update_inventory"), delete_inventory_link=url_for("delete_inventory"), create_inventory_link=url_for("create_inventory")))

# INVENTORIES UPDATE
@app.route('/inventories/update', methods=['POST'])
def update_inventory():
	with UseDatabase(app.config) as cursor:
		INVENTORY = """select * from inventories where id = %s"""
		cursor.execute(INVENTORY, (request.form['id'],))
		inventory_info = cursor.fetchall()
	return(render_template("/inventories/update.html", heading="Editing inventories", inventory=inventory_info, show_inventory_link=url_for("show_inventory"), index_inventory_link=url_for("inventories_index"), update_inventory_save_link=url_for("save_inventory_changes")))

# INVENTORIES UPDATE SAVE
@app.route('/inventories/update_save', methods=['POST'])
def save_inventory_changes():
	with UseDatabase(app.config) as cursor:
		UPDATE = """update inventories set film_id = %s, store_id = %s where id = %s"""
		cursor.execute(UPDATE, (request.form['film_id'], request.form['store_id'], request.form['id']))
		SELECT = """select * from inventories"""
		cursor.execute(SELECT)
		inventories_list = cursor.fetchall()
	return(render_template('/inventories/index.html', heading="Listing inventories", inventories=inventories_list, show_inventory_link=url_for("show_inventory"), update_inventory_link=url_for("update_inventory"), delete_inventory_link=url_for("delete_inventory"), create_inventory_link=url_for("create_inventory")))

# INVENTORIES SHOW
@app.route('/inventories/show', methods=['POST'])
def show_inventory():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from inventories where id = %s"""
		cursor.execute(SQL, (request.form['id'],))
		inventory_info = cursor.fetchall()
	return(render_template('/inventories/show.html', inventory=inventory_info, index_inventory_link=url_for("inventories_index"), update_inventory_link=url_for("update_inventory")))



# =============================================================================================
# LANGUAGES
# =============================================================================================

# LANGUAGES INDEX
@app.route('/languages/index', methods=['GET', 'POST'])
def languages_index():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from languages"""
		cursor.execute(SQL)
		languages_list = cursor.fetchall()
	return(render_template('/languages/index.html', heading="Listing languages", languages=languages_list, show_language_link=url_for("show_language"), update_language_link=url_for("update_language"), delete_language_link=url_for("delete_language"), create_language_link=url_for("create_language")))

# LANGUAGES DELETE
@app.route('/languages/delete', methods=['POST'])
def delete_language():
	SQL = """delete from languages where id = %s"""
	with UseDatabase(app.config) as cursor:
		cursor.execute(SQL, (request.form['id'],))
	return(redirect(url_for("languages_index")))	

# LANGUAGES CREATE
@app.route('/languages/create', methods=['GET', 'POST'])
def create_language():
	return(render_template("/languages/create.html", heading="Create a new Language", index_language_link=url_for("languages_index"), save_language_link=url_for("save_language")))

# LANGUAGES CREATE SAVE
@app.route('/languages/save', methods=['POST'])
def save_language():
	INSERT = """insert into languages (name) VALUES (%s)"""
	all_ok = True
	if len(request.form['name']) == 0:
		all_ok = False
		flash("Sorry the language's name cannot be empty. Try again")
	if all_ok:
		with UseDatabase(app.config) as cursor:
			cursor.execute(INSERT, (request.form['name'],))
			SELECTALL = """select * from languages"""
			cursor.execute(SELECTALL)
			languages_list = cursor.fetchall()
		return(render_template('/languages/index.html', heading="Listing languages", languages=languages_list, show_language_link=url_for("show_language"), update_language_link=url_for("update_language"), delete_language_link=url_for("delete_language"), create_language_link=url_for("create_language")))
	else:
		return(redirect(url_for("create_language")))

# LANGUAGES UPDATE
@app.route('/languages/update', methods=['POST'])
def update_language():
	with UseDatabase(app.config) as cursor:
		LANGUAGE = """select * from languages where id = %s"""
		cursor.execute(LANGUAGE, (request.form['id'],))
		language_info = cursor.fetchall()
	return(render_template("/languages/update.html", heading="Editing language", language=language_info, show_language_link=url_for("show_language"), index_language_link=url_for("languages_index"), update_language_save_link=url_for("save_language_changes")))

# LANGUAGES UPDATE SAVE
@app.route('/languages/update_save', methods=['POST'])
def save_language_changes():
	with UseDatabase(app.config) as cursor:
		UPDATE = """update languages set name = %s where id = %s"""
		cursor.execute(UPDATE, (request.form['name'], request.form['id']))
		SELECT = """select * from languages"""
		cursor.execute(SELECT)
		languages_list = cursor.fetchall()
	return(render_template('/languages/index.html', heading="Listing languages", languages=languages_list, show_language_link=url_for("show_language"), update_language_link=url_for("update_language"), delete_language_link=url_for("delete_language"), create_language_link=url_for("create_language")))

# LANGUAGES SHOW
@app.route('/languages/show', methods=['POST'])
def show_language():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from languages where id = %s"""
		cursor.execute(SQL, (request.form['id'],))
		language_info = cursor.fetchall()
	return(render_template('/languages/show.html', language=language_info, index_language_link=url_for("languages_index"), update_language_link=url_for("update_language")))



# =============================================================================================
# PAYMENTS
# =============================================================================================

# PAYMENTS INDEX
@app.route('/payments/index', methods=['GET', 'POST'])
def payments_index():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from payments"""
		cursor.execute(SQL)
		payments_list = cursor.fetchall()
	return(render_template('/payments/index.html', heading="Listing payments", payments=payments_list, show_payment_link=url_for("show_payment"), update_payment_link=url_for("update_payment"), delete_payment_link=url_for("delete_payment"), create_payment_link=url_for("create_payment")))

# PAYMENTS DELETE
@app.route('/payments/delete', methods=['POST'])
def delete_payment():
	SQL = """delete from payments where id = %s"""
	with UseDatabase(app.config) as cursor:
		cursor.execute(SQL, (request.form['id'],))
	return(redirect(url_for("payments_index")))	

# PAYMENTS CREATE
@app.route('/payments/create', methods=['GET', 'POST'])
def create_payment():
	return(render_template("/payments/create.html", heading="Create a new Payment", index_payment_link=url_for("payments_index"), save_payment_link=url_for("save_payment")))

# PAYMENTS CREATE SAVE
@app.route('/payments/save', methods=['POST'])
def save_payment():
	INSERT = """insert into payments (customer_id, staff_id, rental_id, amount, payment_date) VALUES (%s, %s, %s, %s, %s)"""
	with UseDatabase(app.config) as cursor:
		current_time = datetime.datetime.now().time()
		cursor.execute(INSERT, (request.form['customer_id'], request.form['staff_id'], request.form['rental_id'], request.form['amount'], current_time.strftime('%Y-%m-%d %H:%M:%S')))
		SELECTALL = """select * from payments"""
		cursor.execute(SELECTALL)
		payments_list = cursor.fetchall()
	return(render_template('/payments/index.html', heading="Listing payments", payments=payments_list, show_payment_link=url_for("show_payment"), update_payment_link=url_for("update_payment"), delete_payment_link=url_for("delete_payment"), create_payment_link=url_for("create_payment")))

# PAYMENTS UPDATE
@app.route('/payments/update', methods=['POST'])
def update_payment():
	with UseDatabase(app.config) as cursor:
		PAYMENT = """select * from payments where id = %s"""
		cursor.execute(PAYMENT, (request.form['id'],))
		payment_info = cursor.fetchall()
	return(render_template("/payments/update.html", heading="Editing payment", payment=payment_info, show_payment_link=url_for("show_payment"), index_payment_link=url_for("payments_index"), update_payment_save_link=url_for("save_payment_changes")))

# PAYMENTS UPDATE SAVE
@app.route('/payments/update_save', methods=['POST'])
def save_payment_changes():
	with UseDatabase(app.config) as cursor:

		UPDATE = """update payments set customer_id = %s, staff_id = %s, rental_id = %s, amount = %s where id = %s"""
		cursor.execute(UPDATE, (request.form['customer_id'], request.form['staff_id'], request.form['rental_id'], request.form['amount'], request.form['id']))
		SELECT = """select * from payments"""
		cursor.execute(SELECT)
		payments_list = cursor.fetchall()
	return(render_template('/payments/index.html', heading="Listing payments", payments=payments_list, show_payment_link=url_for("show_payment"), update_payment_link=url_for("update_payment"), delete_payment_link=url_for("delete_payment"), create_payment_link=url_for("create_payment")))

# PAYMENTS SHOW
@app.route('/payments/show', methods=['POST'])
def show_payment():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from payments where id = %s"""
		cursor.execute(SQL, (request.form['id'],))
		payment_info = cursor.fetchall()
	return(render_template('/payments/show.html', payment=payment_info, index_payment_link=url_for("payments_index"), update_payment_link=url_for("update_payment")))

# =============================================================================================
# RENTALS
# =============================================================================================

# RENTALS INDEX
@app.route('/rentals/index', methods=['GET', 'POST'])
def rentals_index():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from rentals"""
		cursor.execute(SQL)
		rentals_list = cursor.fetchall()
	return(render_template('/rentals/index.html', heading="Listing rentals", rentals=rentals_list, show_rental_link=url_for("show_rental"), update_rental_link=url_for("update_rental"), delete_rental_link=url_for("delete_rental"), create_rental_link=url_for("create_rental")))

# RENTALS DELETE
@app.route('/rentals/delete', methods=['POST'])
def delete_rental():
	SQL = """delete from rentals where id = %s"""
	with UseDatabase(app.config) as cursor:
		cursor.execute(SQL, (request.form['id'],))
	return(redirect(url_for("rentals_index")))	

# RENTALS CREATE
@app.route('/rentals/create', methods=['GET', 'POST'])
def create_rental():
	return(render_template("/rentals/create.html", heading="Create a new Rental", index_rental_link=url_for("rentals_index"), save_rental_link=url_for("save_rental")))

# RENTALS CREATE SAVE
@app.route('/rentals/save', methods=['POST'])
def save_rental():
	INSERT = """insert into rentals (rental_date, inventory_id, customer_id, return_date, staff_id) VALUES (%s, %s, %s, %s, %s)"""
	with UseDatabase(app.config) as cursor:
		rental_date = datetime.datetime.now().time()
		cursor.execute(INSERT, (rental_date.strftime('%Y-%m-%d %H:%M:%S'), request.form['inventory_id'], request.form['customer_id'], rental_date.strftime('%Y-%m-%d %H:%M:%S'), request.form['staff_id']))
		SELECTALL = """select * from rentals"""
		cursor.execute(SELECTALL)
		rentals_list = cursor.fetchall()
	return(render_template('/rentals/index.html', heading="Listing rentals", rentals=rentals_list, show_rental_link=url_for("show_rental"), update_rental_link=url_for("update_rental"), delete_rental_link=url_for("delete_rental"), create_rental_link=url_for("create_rental")))

# RENTALS UPDATE
@app.route('/rentals/update', methods=['POST'])
def update_rental():
	with UseDatabase(app.config) as cursor:
		RENTAL = """select * from rentals where id = %s"""
		cursor.execute(RENTAL, (request.form['id'],))
		rental_info = cursor.fetchall()
	return(render_template("/rentals/update.html", heading="Editing rental", rental=rental_info, show_rental_link=url_for("show_rental"), index_rental_link=url_for("rentals_index"), update_rental_save_link=url_for("save_rental_changes")))

# RENTALS UPDATE SAVE
@app.route('/rentals/update_save', methods=['POST'])
def save_rental_changes():
	with UseDatabase(app.config) as cursor:
		UPDATE = """update rentals set inventory_id = %s, customer_id = %s, staff_id = %s where id = %s"""
		cursor.execute(UPDATE, (request.form['inventory_id'], request.form['customer_id'], request.form['staff_id'], request.form['id']))
		SELECT = """select * from rentals"""
		cursor.execute(SELECT)
		rentals_list = cursor.fetchall()
	return(render_template('/rentals/index.html', heading="Listing rentals", rentals=rentals_list, show_rental_link=url_for("show_rental"), update_rental_link=url_for("update_rental"), delete_rental_link=url_for("delete_rental"), create_rental_link=url_for("create_rental")))

# RENTALS SHOW
@app.route('/rentals/show', methods=['POST'])
def show_rental():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from rentals where id = %s"""
		cursor.execute(SQL, (request.form['id'],))
		rental_info = cursor.fetchall()
	return(render_template('/rentals/show.html', rental=rental_info, index_rental_link=url_for("rentals_index"), update_rental_link=url_for("update_rental")))



# =============================================================================================
# STAFF
# =============================================================================================

# STAFF INDEX
@app.route('/staffs/index', methods=['GET', 'POST'])
def staffs_index():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from staffs"""
		cursor.execute(SQL)
		staffs_list = cursor.fetchall()
	return(render_template('/staffs/index.html', heading="Listing staffs", staffs=staffs_list, show_staff_link=url_for("show_staff"), update_staff_link=url_for("update_staff"), delete_staff_link=url_for("delete_staff"), create_staff_link=url_for("create_staff")))

# STAFF DELETE
@app.route('/staffs/delete', methods=['POST'])
def delete_staff():
	SQL = """delete from staffs where id = %s"""
	with UseDatabase(app.config) as cursor:
		cursor.execute(SQL, (request.form['id'],))
	return(redirect(url_for("staffs_index")))	

# STAFF CREATE
@app.route('/staffs/create', methods=['GET', 'POST'])
def create_staff():
	return(render_template("/staffs/create.html", heading="Create a new Staff", index_staff_link=url_for("staffs_index"), save_staff_link=url_for("save_staff")))

# STAFF CREATE SAVE
@app.route('/staffs/save', methods=['POST'])
def save_staff():
	if request.form['active'] == 'on':
		checkbox = 1;
	else:
		checkbox = 0;
	INSERT = """insert into staffs (first_name, last_name, address_id, email, store_id, active, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
	all_ok = True
	if len(request.form['first_name']) == 0:
		all_ok = False
		flash("Sorry the staffs first name cannot be empty. Try again")
	if len(request.form['last_name']) == 0:
		all_ok = False
		flash("Sorry the staffs last name cannot be empty. Try again")
	if all_ok:
		with UseDatabase(app.config) as cursor:
			cursor.execute(INSERT, (request.form['first_name'], request.form['last_name'], request.form['address_id'], request.form['email'], request.form['store_id'], checkbox, request.form['username'], request.form['password'],))
			SELECTALL = """select * from staffs"""
			cursor.execute(SELECTALL)
			staffs_list = cursor.fetchall()
		return(render_template('/staffs/index.html', heading="Listing staff", staffs=staffs_list, show_staff_link=url_for("show_staff"), update_staff_link=url_for("update_staff"), delete_staff_link=url_for("delete_staff"), create_staff_link=url_for("create_staff")))
	else:
		return(redirect(url_for("create_staff")))

# STAFF UPDATE
@app.route('/staffs/update', methods=['POST'])
def update_staff():
	with UseDatabase(app.config) as cursor:
		STAFF = """select * from staffs where id = %s"""
		cursor.execute(STAFF, (request.form['id'],))
		staff_info = cursor.fetchall()
	return(render_template("/staffs/update.html", heading="Editing staff", staff=staff_info, show_staff_link=url_for("show_staff"), index_staff_link=url_for("staffs_index"), update_staff_save_link=url_for("save_staff_changes")))

# STAFF UPDATE SAVE
@app.route('/staffs/update_save', methods=['POST'])
def save_staff_changes():
	with UseDatabase(app.config) as cursor:
		if request.form['active'] == 'on':
			checkbox = 1;
		else:
			checkbox = 0;
		UPDATE = """update staffs set first_name = %s, last_name = %s, address_id = %s, email = %s, store_id = %s, active = %s, username = %s, password = %s where id = %s"""
		cursor.execute(UPDATE, (request.form['first_name'], request.form['last_name'], request.form['address_id'], request.form['email'], request.form['store_id'], checkbox, request.form['username'], request.form['password'], request.form['id']))
		SELECT = """select * from staffs"""
		cursor.execute(SELECT)
		staffs_list = cursor.fetchall()
	return(render_template('/staffs/index.html', heading="Listing staffs", staffs=staffs_list, show_staff_link=url_for("show_staff"), update_staff_link=url_for("update_staff"), delete_staff_link=url_for("delete_staff"), create_staff_link=url_for("create_staff")))

# STAFF SHOW
@app.route('/staffs/show', methods=['POST'])
def show_staff():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from staffs where id = %s"""
		cursor.execute(SQL, (request.form['id'],))
		staff_info = cursor.fetchall()
	return(render_template('/staffs/show.html', staff=staff_info, index_staff_link=url_for("staffs_index"), update_staff_link=url_for("update_staff")))


# =============================================================================================
# STORES
# =============================================================================================

# STORES INDEX
@app.route('/stores/index', methods=['GET', 'POST'])
def stores_index():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from stores"""
		cursor.execute(SQL)
		stores_list = cursor.fetchall()
	return(render_template('/stores/index.html', heading="Listing stores", stores=stores_list, show_store_link=url_for("show_store"), update_store_link=url_for("update_store"), delete_store_link=url_for("delete_store"), create_store_link=url_for("create_store")))

# STORES DELETE
@app.route('/stores/delete', methods=['POST'])
def delete_store():
	SQL = """delete from stores where id = %s"""
	with UseDatabase(app.config) as cursor:
		cursor.execute(SQL, (request.form['id'],))
	return(redirect(url_for("stores_index")))	

# STORES CREATE
@app.route('/stores/create', methods=['GET', 'POST'])
def create_store():
	return(render_template("/stores/create.html", heading="Create a new Store", index_store_link=url_for("stores_index"), save_store_link=url_for("save_store")))

# STORES CREATE SAVE
@app.route('/stores/save', methods=['POST'])
def save_store():
	INSERT = """insert into stores (address_id) VALUES (%s)"""
	with UseDatabase(app.config) as cursor:
		cursor.execute(INSERT, (request.form['address_id'],))
		SELECTALL = """select * from stores"""
		cursor.execute(SELECTALL)
		stores_list = cursor.fetchall()
	return(render_template('/stores/index.html', heading="Listing stores", stores=stores_list, show_store_link=url_for("show_store"), update_store_link=url_for("update_store"), delete_store_link=url_for("delete_store"), create_store_link=url_for("create_store")))

# STORES UPDATE
@app.route('/stores/update', methods=['POST'])
def update_store():
	with UseDatabase(app.config) as cursor:
		STORE = """select * from stores where id = %s"""
		cursor.execute(STORE, (request.form['id'],))
		store_info = cursor.fetchall()
	return(render_template("/stores/update.html", heading="Editing store", store=store_info, show_store_link=url_for("show_store"), index_store_link=url_for("stores_index"), update_store_save_link=url_for("save_store_changes")))

# STORES UPDATE SAVE
@app.route('/stores/update_save', methods=['POST'])
def save_store_changes():
	with UseDatabase(app.config) as cursor:
		UPDATE = """update stores set address_id = %s where id = %s"""
		cursor.execute(UPDATE, (request.form['address_id'], request.form['id']))
		SELECT = """select * from stores"""
		cursor.execute(SELECT)
		stores_list = cursor.fetchall()
	return(render_template('/stores/index.html', heading="Listing stores", stores=stores_list, show_store_link=url_for("show_store"), update_store_link=url_for("update_store"), delete_store_link=url_for("delete_store"), create_store_link=url_for("create_store")))

# STORES SHOW
@app.route('/stores/show', methods=['POST'])
def show_store():
	with UseDatabase(app.config) as cursor:
		SQL = """select * from stores where id = %s"""
		cursor.execute(SQL, (request.form['id'],))
		store_info = cursor.fetchall()
	return(render_template('/stores/show.html', store=store_info, index_store_link=url_for("stores_index"), update_store_link=url_for("update_store")))


app.config['SECRET_KEY'] = 'thisismysecretkeywhichyouwillneverguesshahahahahahahahaha'

if __name__ == "__main__":
	app.config['DB_HOST'] = "127.0.0.1"
	app.config['DB_USER'] = "sakila_app"
	app.config['DB_PASSWORD'] = "ramz"
	app.config['DB'] = "sakila"
	app.run()



