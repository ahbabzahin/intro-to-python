
CREATE TABLE Employees (
    EmpID INT,
    Name VARCHAR(50),
    Age INT,
    Salary DECIMAL(10,2),
    Department VARCHAR(30)
);


INSERT INTO Employees (EmpID, Name, Age, Salary, Department) VALUES
(1, 'Alice', 25, 30000, 'HR'),
(2, 'Bob', 30, 45000, 'IT'),
(3, 'Charlie', 28, 40000, 'Finance'),
(4, 'David', 35, 55000, 'IT'),
(5, 'Eva', 22, 28000, 'HR');

SELECT 
    Name,
    Salary,
    Salary + 5000 AS BonusAdded,
    Salary - 2000 AS Deducted,
    Salary * 1.1 AS RaisedBy10Percent,
    Salary / 12 AS MonthlyPay,
    Age % 2 AS AgeMod2
FROM Employees;


SELECT 
    Name, Age, Salary
FROM Employees
WHERE Salary >= 40000
  AND Age < 35;


SELECT 
    Name, Department, Salary
FROM Employees
WHERE (Department = 'IT' OR Department = 'Finance')
  AND NOT (Salary < 40000);


SELECT 
    Name, Age, Department
FROM Employees
WHERE Age BETWEEN 25 AND 35
  AND Department IN ('IT', 'Finance')
  AND Name LIKE 'C%';


SELECT 
    EmpID,
    EmpID & 1 AS BitwiseAND,
    EmpID | 2 AS BitwiseOR,
    EmpID ^ 3 AS BitwiseXOR
FROM Employees;
