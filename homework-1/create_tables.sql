-- SQL-команды для создания таблиц
CREATE DATABASE north;
CREATE TABLE orders(
	order_id int PRIMARY KEY NOT NULL,
	customer_id varchar(7) NOT NULL,
	employee_id varchar(15) NOT NULL,
	order_date date NOT NULL,
	ship_city text NOT NULL
);

CREATE TABLE customers_data(
	customer_id varchar(7) PRIMARY KEY NOT NULL,
	company_name varchar(50) NOT NULL,
	contact_name varchar(50) NOT NULL
);

CREATE TABLE employees_data(
	employee_id int PRIMARY KEY NOT NULL,
	first_name varchar(15) NOT NULL,
	last_name varchar(50) NOT NULL,
	title varchar(500) NOT NULL,
	birth_date varchar(15) NOT NULL,
	notes text NOT NULL
);

ALTER TABLE orders RENAME TO orders_data;