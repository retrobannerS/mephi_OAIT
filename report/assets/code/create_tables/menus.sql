CREATE TABLE menus (
	id SERIAL NOT NULL, 
	title VARCHAR(50) NOT NULL, 
	cost FLOAT NOT NULL, 
	count_dishes INTEGER NOT NULL, 
	colorfulness FLOAT NOT NULL, 
	PRIMARY KEY (id)
);