DROP TABLE IF EXISTS pets;

CREATE TABLE pets(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    species VARCHAR(255),
    owner VARCHAR(255),
    contact_no VARCHAR(255),
    treatment_notes TEXT
);


