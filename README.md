### BRIEF
  A veterinary practice has approached you to build a web application to help them manage their animals and vets. A vet may look after many animals at a time.   An animal is registered with only one vet.

##### MVP
  - Display all pets registered with the practice
  - Display details of individual pets including name, DOB, species, treatment notes and owner contact information
  - Display all vets employed by the practice
  - Display details of individual vets including pets registered with them
  - Be able to create, delete and edit pet details
  - Be able to create, delete and edit vet details

##### Completed extensions
  - Include details of each pet's owner and be able to assign multiple pets to a single owner
  - Display details of an individual owner including contact info and pets registered with the practice 
  - Be able to create, delete and edit owner details
  - Mark owners as being registered/unregistered with the Vet. unregistered owners will be unable to register new pets with the practice.
  
##### Possible future extensions
  - Include a capacity for patients within each vet details. Vets will be unable to have new pets assigned to them if their capacity is full.
  - Include images of each pet including when adding/editing pet details.
  - Handle check-in / check-out dates
  - Let the practice see all animals currently in the practice if current date is between check-in/check-out dates.
  - Sometimes an owner does not know the DOB. Allow them to enter an age instead. Try and make sure this always up to date - ie if they visit again a year         from now a 3 yr old dog is now 4.

### Tech Stack
  - Python backend
  - Database using PostgreSQL
  - Flask framework
  - Frontend using HTML and CSS

### Set-up
  - Install Flask: https://flask.palletsprojects.com/en/2.3.x/installation/#install-flask
  - Install PostgreSQL: https://www.postgresql.org/download/
  - Create PostgreSQL database using: create *Your database name* i.e. 'vet_management'
  - Initialise database using command: psql -d *Your database name* -f db/vet_management.sql
  - Seed database using command: python3 console.py
  - Run app using command: python3 app.py

### Key Learnings
  - Importance of proper planning when coding.
  - Time required to follow proper methodical process of testing and debugging code.
  - Combining several technologies into my first full stack application.
  - Deepened understanding of all technologies involved, particularly styling using CSS.

