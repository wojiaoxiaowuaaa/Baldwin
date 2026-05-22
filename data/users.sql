-- 创建数据库（如果不存在）
CREATE DATABASE IF NOT EXISTS mydatabase;
USE mydatabase;

-- 创建用户表
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    birthdate DATE,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 插入示例数据
INSERT INTO users (username, email, birthdate) VALUES
    ('JohnDoe', 'john@example.com', '1990-01-15'),
    ('JaneSmith', 'jane@example.com', '1985-08-22'),
    ('BobJohnson', 'bob@example.com', '1995-04-10');