CREATE TABLE `customers` (
  `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
)

CREATE TABLE `orders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int NOT NULL,
  `order_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`) ON DELETE action CASCADE
) DEFAULT CHARSET=utf8;


INSERT INTO customers (first_name, last_name, email) VALUES
	('John', 'Doe','john@abv.bg'),
	('Jane', 'Doe',''),
	('John', 'Smith', ''),
	('Ada', 'Byron', 'ada@gmail.com');

INSERT INTO orders (customer_id,order_date)
  VALUES (1, "2020-01-20 21:00:00"),
		 (2, "2020-01-20 21:00:00"),
		 (3, "2020-01-20 21:00:00"),
		 (4, "2020-01-20 21:00:00"),
		 (1, "2020-01-22 22:00:00")
		 (1, "2020-01-23 22:00:00")
		 (1, "2020-01-24 22:00:00");


ALTER TABLE test.orders
DROP FOREIGN KEY `orders_ibfk_1`;


ALTER TABLE test.orders
ADD FOREIGN KEY `FK_customer_id`(customer_id)
            REFERENCES `customers` (`id`) ON DELETE CASCADE;


SELECT customers.first_name, orders.order_date FROM customers, orders
WHERE customers.id = orders.customer_id AND order_date = '2020-01-20 21:00:00';


SELECT t1.first_name,t2.order_date FROM customers t1
INNER JOIN orders t2
ON t1.id = t2.customer_id;