-- Store --
INSERT INTO stores_store (id, name, address) VALUES (1, "Perth Book Shop", "1 Hay Street, Perth WA 6000");

-- Enter Books --
INSERT INTO books_book (id, title, author, price, store_id) VALUES (1, "Sapiens", "Yuval Harari", 29.99, 1);
INSERT INTO books_book (id, title, author, price, store_id) VALUES (2, "The New Jim Crow: Mass Incarceration in the Age of Colorblindness", "Michelle Alexander", 25.99, 1);
INSERT INTO books_book (id, title, author, price, store_id) VALUES (3, "Range: Why Generalists Triumph in a Specialized World", "David Epstein", 29.99, 1);
INSERT INTO books_book (id, title, author, price, store_id) VALUES (4, "The Splendid and the Vile: A Saga of Churchill, Family, and Defiance During the Blitz", "Erik Larson", 36.99, 1);
INSERT INTO books_book (id, title, author, price, store_id) VALUES (5, "The Spy and the Traitor: The Greatest Espionage Story of the Cold War", "Ben Macintyre", 39.99, 1);
INSERT INTO books_book (id, title, author, price, store_id) VALUES (6, "Breath from Salt: A Deadly Genetic Disease, a New Era in Science, and the Patients and Families Who Changed Medicine", "Bijal P. Trivedi", 31.99, 1);

-- Enter Inventory --
INSERT INTO inventory_inventory (id, quantity, book_id, store_id) VALUES (1, 4, 1, 1);
INSERT INTO inventory_inventory (id, quantity, book_id, store_id) VALUES (2, 13, 2, 1);
INSERT INTO inventory_inventory (id, quantity, book_id, store_id) VALUES (3, 7, 3, 1);
INSERT INTO inventory_inventory (id, quantity, book_id, store_id) VALUES (4, 9, 4, 1);
INSERT INTO inventory_inventory (id, quantity, book_id, store_id) VALUES (5, 15, 5, 1);
INSERT INTO inventory_inventory (id, quantity, book_id, store_id) VALUES (6, 341, 6, 1);