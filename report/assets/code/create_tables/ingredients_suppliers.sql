CREATE TABLE ingredients_suppliers (
	id SERIAL NOT NULL, 
	ingredient_id INTEGER NOT NULL, 
	supplier_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(ingredient_id) REFERENCES ingredients (id) ON DELETE CASCADE, 
	FOREIGN KEY(supplier_id) REFERENCES suppliers (id) ON DELETE CASCADE
);