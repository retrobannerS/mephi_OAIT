CREATE TABLE payment_infos (
	id SERIAL NOT NULL, 
	user_id INTEGER, 
	payment_method_id INTEGER, 
	requisites VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id) ON DELETE CASCADE, 
	FOREIGN KEY(payment_method_id) REFERENCES payment_methods (id) ON DELETE CASCADE
);
