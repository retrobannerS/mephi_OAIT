CREATE TABLE ingredients_preferences (
	id SERIAL NOT NULL, 
	ingredient_id INTEGER NOT NULL, 
	preference_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(ingredient_id) REFERENCES ingredients (id) ON DELETE CASCADE, 
	FOREIGN KEY(preference_id) REFERENCES preferences (id) ON DELETE CASCADE
);