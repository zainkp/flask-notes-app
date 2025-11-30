CREATE DATABASE IF NOT EXISTS notesdb;

-- Create user if not exists and grant privileges
CREATE USER IF NOT EXISTS 'notes_user'@'localhost' IDENTIFIED BY 'secure_password';
GRANT ALL PRIVILEGES ON notesdb.* TO 'notes_user'@'localhost';
FLUSH PRIVILEGES;

USE notesdb;

CREATE TABLE IF NOT EXISTS notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL
);
