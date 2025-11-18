-- Capstone Project 2 – SQL (LIKE, DISTINCT, Sorting, Filtering)

-- 1. Customers whose names start with A
SELECT *
FROM Customers
WHERE CustomerName LIKE 'A%';

-- 2. Products containing "Pro"
SELECT *
FROM Products
WHERE ProductName LIKE '%Pro%';

-- 3. Distinct cities where orders were placed
SELECT DISTINCT City
FROM Orders;

-- 4. Employees with email ending in .com, sorted alphabetically
SELECT *
FROM Employees
WHERE Email LIKE '%.com'
ORDER BY EmployeeName ASC;

-- 5. Orders above 500, sorted highest first
SELECT *
FROM Orders
WHERE OrderAmount > 500
ORDER BY OrderAmount DESC;

-- 6. Customers with phone numbers containing 555
SELECT *
FROM Customers
WHERE Phone LIKE '%555%';

-- 7. Distinct product categories, sorted alphabetically
SELECT DISTINCT Category
FROM Products
ORDER BY Category ASC;

-- 8. Products whose names end with "Box"
SELECT *
FROM Products
WHERE ProductName LIKE '%Box';

-- 9. Orders with shipping address starting with Dhaka
SELECT OrderID, ShippingAddress
FROM Orders
WHERE ShippingAddress LIKE 'Dhaka%';

-- 10. Distinct customer names who placed orders above 1000
SELECT DISTINCT CustomerName
FROM Orders
WHERE OrderAmount > 1000;
