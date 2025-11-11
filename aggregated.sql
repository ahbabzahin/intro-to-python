-- Create a sample table
CREATE TABLE Employees (
    EmpID INT,
    EmpName VARCHAR(50),
    Department VARCHAR(50),
    Salary DECIMAL(10,2),
    Age INT
);

-- Insert sample data
INSERT INTO Employees (EmpID, EmpName, Department, Salary, Age)
VALUES
(1, 'Alice', 'HR', 35000, 25),
(2, 'Bob', 'IT', 50000, 30),
(3, 'Charlie', 'Finance', 45000, 28),
(4, 'David', 'IT', 60000, 35),
(5, 'Eva', 'HR', 40000, 26),
(6, 'Frank', 'Finance', 48000, 31),
(7, 'Grace', 'IT', 52000, 29);

-- 1. COUNT(): Count total employees
SELECT COUNT(*) AS TotalEmployees FROM Employees;

-- 2. SUM(): Total salary of all employees
SELECT SUM(Salary) AS TotalSalary FROM Employees;

-- 3. AVG(): Average salary
SELECT AVG(Salary) AS AverageSalary FROM Employees;

-- 4. MIN(): Minimum salary
SELECT MIN(Salary) AS LowestSalary FROM Employees;

-- 5. MAX(): Maximum salary
SELECT MAX(Salary) AS HighestSalary FROM Employees;

-- 6. GROUP BY: Aggregate by department
SELECT Department,
       COUNT(*) AS TotalEmployees,
       SUM(Salary) AS TotalDeptSalary,
       AVG(Salary) AS AvgDeptSalary,
       MIN(Salary) AS MinDeptSalary,
       MAX(Salary) AS MaxDeptSalary
FROM Employees
GROUP BY Department;

-- 7. HAVING: Filter aggregated results
SELECT Department,
       AVG(Salary) AS AvgSalary
FROM Employees
GROUP BY Department
HAVING AVG(Salary) > 45000;

-- 8. Combining aggregate with WHERE
SELECT Department,
       SUM(Salary) AS TotalSalary
FROM Employees
WHERE Age > 27
GROUP BY Department;
