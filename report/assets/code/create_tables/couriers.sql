CREATE TABLE couriers (
	id SERIAL NOT NULL, 
	first_name VARCHAR(50) NOT NULL, 
	middle_name VARCHAR(50), 
	last_name VARCHAR(50) NOT NULL, 
	birth_date DATE NOT NULL, 
	PRIMARY KEY (id)
);