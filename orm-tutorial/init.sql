-- Initialise DB authentication -- 
CREATE USER "test";
ALTER USER "test" WITH PASSWORD 'test';
CREATE DATABASE demo WITH ENCODING = 'UTF8'
ALTER DATABASE demo OWNER TO "test";

-- Create table --
