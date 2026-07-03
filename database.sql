CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    wallet_balance DECIMAL(10,2)
);

CREATE TABLE orders (
    queue_id INT PRIMARY KEY,
    menu VARCHAR(100),
    total_price DECIMAL(10,2),
    status VARCHAR(20)
);

INSERT INTO users (id, name, wallet_balance)
VALUES
(1, 'Alice', 150.00),
(2, 'Bob', 80.00),
(3, 'Charlie', 200.00);

INSERT INTO orders (queue_id, menu, total_price, status)
VALUES
(101, 'Fried Rice', 50.00, 'Pending'),
(102, 'Noodle Soup', 60.00, 'Pending'),
(103, 'Iced Coffee', 40.00, 'Ready');

UPDATE orders
SET status = 'Ready'
WHERE status = 'Pending';

SELECT *
FROM orders
WHERE status = 'Pending';