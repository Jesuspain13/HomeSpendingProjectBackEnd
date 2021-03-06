GRANT ALL PRIVILEGES ON DATABASE spendings TO admin;

CREATE SEQUENCE SEQ_SUPPLIER INCREMENT BY 1 START 1;

CREATE TABLE suppliers
(
	id BIGINT NOT NULL default nextval('spendings.SEQ_SUPPLIER'),
	name VARCHAR(100) NOT NULL,
	PRIMARY KEY (id)
);

CREATE SEQUENCE SEQ_SPENDING_TYPE INCREMENT BY 1 START 1;

CREATE TABLE spending_type
(
	id BIGINT NOT NULL default nextval('spendings.SEQ_SPENDING_TYPE'),
	name VARCHAR(100) NOT NULL,
	PRIMARY KEY (id)
);

CREATE SEQUENCE app.SEQ_SPENDING INCREMENT BY 1 START 1;

CREATE TABLE spendings
(
	id BIGINT NOT NULL default nextval('spendings.SEQ_SPENDING'),
	type_id INTEGER NOT NULL,
	amount FLOAT NOT NULL,
	supplier_id INTEGER NOT NULL,
	description VARCHAR(300),
	purchase_date DATE NOT NULL DEFAULT CURRENT_DATE,
	PRIMARY KEY (id),
	CONSTRAINT fk_supplier FOREIGN KEY(supplier_id) REFERENCES spendings.suppliers(id),
    CONSTRAINT fk_type FOREIGN KEY(type_id) REFERENCES spendings.spending_type(id)
);