CREATE TABLE dishes_ingredients (
	id SERIAL NOT NULL, 
	dish_id INTEGER NOT NULL, 
	ingredient_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(dish_id) REFERENCES dishes (id) ON DELETE CASCADE, 
	FOREIGN KEY(ingredient_id) REFERENCES ingredients (id) ON DELETE CASCADE
);