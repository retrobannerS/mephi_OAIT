CREATE TABLE payment_methods (
	id SERIAL NOT NULL, 
	title VARCHAR(50) NOT NULL, 
	require_requisites BOOLEAN NOT NULL, 
	PRIMARY KEY (id)
);