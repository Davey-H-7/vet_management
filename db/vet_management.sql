DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS owners;


CREATE TABLE vets(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    position VARCHAR(255)
);

CREATE TABLE owners(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    contact_no VARCHAR(255)
);

CREATE TABLE pets(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob DATE,
    species VARCHAR(255),
    owner_id INT NOT NULL REFERENCES owners(id) ON DELETE CASCADE,
    treatment_notes TEXT,
    vet_id INT REFERENCES vets(id) ON DELETE SET NULL
);




