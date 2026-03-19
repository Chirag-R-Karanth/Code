CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    age INT,
    grade CHAR(1),
    city VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO students (first_name, last_name, age, grade, city) VALUES
('Aarav', 'Sharma', 17, 'A', 'Bengaluru'),
('Priya', 'Patel', 16, 'B', 'Mumbai'),
('Rahul', 'Kumar', 18, 'A', 'Delhi'),
('Sneha', 'Gupta', 15, NULL, 'Bengaluru'),
('Vikram', 'Singh', 17, 'C', 'Pune'),
('Ananya', 'Reddy', 16, 'B', 'Hyderabad');

SELECT * FROM students;
