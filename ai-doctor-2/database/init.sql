-- Ensure the database and user are created
CREATE DATABASE ai_doctor_db;
CREATE USER auth_user WITH ENCRYPTED PASSWORD 'admin123';
GRANT ALL PRIVILEGES ON DATABASE ai_doctor_db TO auth_user;

-- Run migrations
\i migrations/001_init.sql
\i migrations/002_add_indexes.sql
