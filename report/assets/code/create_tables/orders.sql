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