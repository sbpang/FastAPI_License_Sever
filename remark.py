## create table

"""
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    machine_key TEXT,
    subscription_expiry DATE,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

## view table

"""
SELECT * FROM users;
"""

## insert data

"""
INSERT INTO users (email, machine_key, subscription_expiry, is_active)
VALUES ('siubongpang@gmail.com', 'ABCD1234', '2025-12-31', true);
"""

## update data

"""
UPDATE users 
SET is_active = false 
WHERE email = 'siubongpang@gmail.com';
"""

"""
UPDATE users
SET subscription_expiry = '2026-01-01'
WHERE email = 'siubongpang@gmail.com';
"""

"""
UPDATE users
SET machine_key = 'ABCD1234'
WHERE email = 'siubongpang@gmail.com';
"""

## delete data

"""
DELETE FROM users 
WHERE email = 'siubongpang@gmail.com';
"""


