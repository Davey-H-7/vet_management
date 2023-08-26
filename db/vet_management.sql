DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS pets;

CREATE TABLE vets(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    position VARCHAR(255)
);

CREATE TABLE pets(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    species VARCHAR(255),
    owner VARCHAR(255),
    contact_no VARCHAR(255),
    treatment_notes TEXT,
    vet_id INT NOT NULL REFERENCES vets(id)
);




