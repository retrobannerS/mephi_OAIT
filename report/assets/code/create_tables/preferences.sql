CREATE TABLE preferences (
	id SERIAL NOT NULL, 
	title VARCHAR(50) NOT NULL, 
	preference_category_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(preference_category_id) REFERENCES preference_categories (id) ON DELETE CASCADE
);