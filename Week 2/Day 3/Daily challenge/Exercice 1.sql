CREATE TABLE product_orders (
    order_id SERIAL PRIMARY KEY,
    order_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price NUMERIC(10,2) NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    order_id INTEGER REFERENCES product_orders(order_id) ON DELETE CASCADE
);

CREATE OR REPLACE FUNCTION get_order_total(order_input_id INTEGER)
RETURNS NUMERIC(10,2) AS $$
DECLARE
    total NUMERIC(10,2);
BEGIN
    SELECT SUM(price * quantity)
    INTO total
    FROM items
    WHERE order_id = order_input_id;

    RETURN COALESCE(total, 0);
END;
$$ LANGUAGE plpgsql;

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

ALTER TABLE product_orders
ADD COLUMN user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE;

CREATE OR REPLACE FUNCTION get_user_order_total(user_input_id INTEGER, order_input_id INTEGER)
RETURNS NUMERIC(10,2) AS $$
DECLARE
    total NUMERIC(10,2);
BEGIN
    SELECT SUM(i.price * i.quantity)
    INTO total
    FROM items i
    JOIN product_orders po ON i.order_id = po.order_id
    WHERE po.user_id = user_input_id AND po.order_id = order_input_id;

    RETURN COALESCE(total, 0);
END;
$$ LANGUAGE plpgsql;

INSERT INTO users (name) VALUES ('Alice');

INSERT INTO product_orders (user_id) VALUES (1);

INSERT INTO items (product_name, price, quantity, order_id)
VALUES
('Book', 15.00, 2, 1),
('Pen', 2.50, 5, 1);

SELECT get_order_total(1);

SELECT get_user_order_total(1, 1);
SELECT*FROM items