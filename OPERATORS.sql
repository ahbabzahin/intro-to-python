-- Create a sample table
CREATE TABLE Employees (
    EmpID INT,
    EmpName VARCHAR(50),
    Age INT,
    Salary DECIMAL(10,2),
    Department VARCHAR(50)
);

-- Insert some sample data
INSERT INTO Employees (EmpID, EmpName, Age, Salary, Department)
VALUES
(1, 'Alice', 25, 35000, 'HR'),
(2, 'Bob', 30, 50000, 'IT'),
(3, 'Charlie', 28, 45000, 'Finance'),
(4, 'David', 35, 60000, 'IT'),
(5, 'Eva', 26, 40000, 'HR');

-- 1. Arithmetic Operators (+, -, *, /, %)
SELECT EmpName,
       Salary,
       Salary + 5000 AS BonusAdded,
       Salary - 2000 AS AfterDeduction,
       Salary * 0.10 AS TenPercent,
       Salary / 12 AS MonthlySalary,
       Salary % 10000 AS SalaryRemainder
FROM Employees;

-- 2. Comparison Operators (=, !=, <>, >, <, >=, <=)
SELECT * FROM Employees
WHERE Salary >= 40000 AND Age < 35;

-- 3. Logical Operators (AND, OR, NOT)
SELECT * FROM Employees
WHERE Department = 'IT' OR Department = 'HR';

SELECT * FROM Employees
WHERE NOT Department = 'Finance';

-- 4. BETWEEN Operator
SELECT * FROM Employees
WHERE Salary BETWEEN 40000 AND 55000;

-- 5. IN Operator
SELECT * FROM Employees
WHERE Department IN ('IT', 'Finance');

-- 6. LIKE Operator (pattern matching)
SELECT * FROM Employees
WHERE EmpName LIKE 'A%';  -- Names starting with 'A'

-- 7. IS NULL / IS NOT NULL Operator
-- (First add a NULL example)
UPDATE Employees SET Department = NULL WHERE EmpID = 5;

SELECT * FROM Employees
WHERE Department IS NULL;

SELECT * FROM Employees
WHERE Department IS NOT NULL;

-- 8. ANY / ALL Operators
SELECT * FROM Employees
WHERE Salary > ALL (SELECT Salary FROM Employees WHERE Department = 'HR');

SELECT * FROM Employees
WHERE Salary < ANY (SELECT Salary FROM Employees WHERE Department = 'IT');

-- 9. EXISTS Operator
SELECT EmpName, Salary
FROM Employees E
WHERE EXISTS (SELECT 1 FROM Employees WHERE Department = 'Finance');

-- 10. Logical precedence example
SELECT * FROM Employees
WHERE (Department = 'IT' AND Salary > 45000) OR Age < 27;
