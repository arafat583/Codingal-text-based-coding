CREATE TABLE employees156 (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    hire_date DATE
);

INSERT INTO employees156 (id, name, department, salary, hire_date) VALUES
(1, 'Alice Johnson', 'HR', 50000.00, '2020-05-15'),
(2, 'Bob Smith', 'IT', 75000.00, '2018-03-10'),
(3, 'Charlie Brown', 'Finance', 62000.00, '2019-07-22'),
(4, 'David Lee', 'IT', 80000.00, '2021-06-01'),
(5, 'Eve Wilson', 'HR', 55000.00, '2017-11-19');

SELECT * FROM employees156 ORDER BY salary DESC;
SELECT * FROM employees156 ORDER BY hire_date ASC;
SELECT * FROM employees156 WHERE department = 'IT';
SELECT * FROM employees156 WHERE salary > 60000;
SELECT * FROM employees156 WHERE hire_date > '2019-01-01';
SELECT * FROM employees156 WHERE department = 'IT' ORDER BY salary DESC;
SELECT * FROM employees156 WHERE hire_date > '2019-01-01' ORDER BY hire_date ASC;
