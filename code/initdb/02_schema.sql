CREATE TABLE couriers (
	id SERIAL NOT NULL, 
	first_name VARCHAR(50) NOT NULL, 
	middle_name VARCHAR(50), 
	last_name VARCHAR(50) NOT NULL, 
	birth_date DATE NOT NULL, 
	PRIMARY KEY (id)
);


CREATE TABLE dishes (
	id SERIAL NOT NULL, 
	title VARCHAR(100) NOT NULL, 
	type VARCHAR(100) NOT NULL, 
	weight FLOAT NOT NULL, 
	colorfulness FLOAT NOT NULL, 
	PRIMARY KEY (id)
);


CREATE TABLE ingredients (
	id SERIAL NOT NULL, 
	title VARCHAR(100) NOT NULL, 
	type VARCHAR(100) NOT NULL, 
	cost FLOAT NOT NULL, 
	PRIMARY KEY (id)
);


CREATE TABLE menus (
	id SERIAL NOT NULL, 
	title VARCHAR(50) NOT NULL, 
	cost FLOAT NOT NULL, 
	count_dishes INTEGER NOT NULL, 
	colorfulness FLOAT NOT NULL, 
	PRIMARY KEY (id)
);


CREATE TABLE payment_methods (
	id SERIAL NOT NULL, 
	title VARCHAR(50) NOT NULL, 
	require_requisites BOOLEAN NOT NULL, 
	PRIMARY KEY (id)
);


CREATE TABLE preference_categories (
	id SERIAL NOT NULL, 
	title VARCHAR(50) NOT NULL, 
	PRIMARY KEY (id)
);


CREATE TABLE suppliers (
	id SERIAL NOT NULL, 
	title VARCHAR(100) NOT NULL, 
	productivity FLOAT NOT NULL, 
	PRIMARY KEY (id)
);


CREATE TABLE users (
	id SERIAL NOT NULL, 
	first_name VARCHAR(50) NOT NULL, 
	middle_name VARCHAR(50), 
	last_name VARCHAR(50) NOT NULL, 
	sex gender, 
	birth_date DATE NOT NULL, 
	phone_number VARCHAR(10) NOT NULL, 
	invited_by_id INTEGER, 
	bonuses INTEGER DEFAULT 0 NOT NULL, 
	address VARCHAR(200), 
	PRIMARY KEY (id), 
	FOREIGN KEY(invited_by_id) REFERENCES users (id) ON DELETE SET NULL
);


CREATE TABLE dishes_ingredients (
	id SERIAL NOT NULL, 
	dish_id INTEGER NOT NULL, 
	ingredient_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(dish_id) REFERENCES dishes (id) ON DELETE CASCADE, 
	FOREIGN KEY(ingredient_id) REFERENCES ingredients (id) ON DELETE CASCADE
);


CREATE TABLE dishes_menus (
	id SERIAL NOT NULL, 
	dish_id INTEGER NOT NULL, 
	menu_id INTEGER NOT NULL, 
	date DATE DEFAULT 'now()' NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(dish_id) REFERENCES dishes (id) ON DELETE CASCADE, 
	FOREIGN KEY(menu_id) REFERENCES menus (id) ON DELETE CASCADE
);


CREATE TABLE ingredients_suppliers (
	id SERIAL NOT NULL, 
	ingredient_id INTEGER NOT NULL, 
	supplier_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(ingredient_id) REFERENCES ingredients (id) ON DELETE CASCADE, 
	FOREIGN KEY(supplier_id) REFERENCES suppliers (id) ON DELETE CASCADE
);


CREATE TABLE payment_infos (
	id SERIAL NOT NULL, 
	user_id INTEGER, 
	payment_method_id INTEGER, 
	requisites VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id) ON DELETE CASCADE, 
	FOREIGN KEY(payment_method_id) REFERENCES payment_methods (id) ON DELETE CASCADE
);


CREATE TABLE preferences (
	id SERIAL NOT NULL, 
	title VARCHAR(50) NOT NULL, 
	preference_category_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(preference_category_id) REFERENCES preference_categories (id) ON DELETE CASCADE
);


CREATE TABLE ingredients_preferences (
	id SERIAL NOT NULL, 
	ingredient_id INTEGER NOT NULL, 
	preference_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(ingredient_id) REFERENCES ingredients (id) ON DELETE CASCADE, 
	FOREIGN KEY(preference_id) REFERENCES preferences (id) ON DELETE CASCADE
);


CREATE TABLE orders (
	id SERIAL NOT NULL, 
	user_id INTEGER NOT NULL, 
	menu_id INTEGER, 
	created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL, 
	status status DEFAULT 'new' NOT NULL, 
	courier_id INTEGER, 
	payment_info_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id) ON DELETE CASCADE, 
	FOREIGN KEY(menu_id) REFERENCES menus (id) ON DELETE SET NULL, 
	FOREIGN KEY(courier_id) REFERENCES couriers (id) ON DELETE SET NULL, 
	FOREIGN KEY(payment_info_id) REFERENCES payment_infos (id) ON DELETE SET NULL
);


CREATE TABLE preferences_users (
	id SERIAL NOT NULL, 
	preference_id INTEGER NOT NULL, 
	user_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(preference_id) REFERENCES preferences (id) ON DELETE CASCADE, 
	FOREIGN KEY(user_id) REFERENCES users (id) ON DELETE CASCADE
);

