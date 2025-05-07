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