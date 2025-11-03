-- Step 1: Create a table
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    Department VARCHAR(50),
    Grade CHAR(1)
);

-- Step 2: Insert sample records
INSERT INTO Students (StudentID, Name, Age, Department, Grade)
VALUES
(1, 'Aisha', 20, 'Computer Science', 'A'),
(2, 'Rafi', 22, 'Electrical Engineering', 'B'),
(3, 'Tania', 21, 'Computer Science', 'A'),
(4, 'Nabil', 23, 'Mechanical Engineering', 'C'),
(5, 'Sadia', 20, 'Computer Science', 'B');

-- Step 3: Fetch all records
SELECT * FROM Students;

-- Step 4: Fetch records using WHERE clause
SELECT * FROM Students
WHERE Department = 'Computer Science' AND Grade = 'A';
