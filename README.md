# Django Person API

This Django project provides an API for managing person records. It allows you to perform CRUD (Create, Read, Update, Delete) operations on person objects.

## Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/your-username/django-person-api.git
   
Change into the project directory:

      cd django-person-api
  
Create a virtual environment and activate it (optional but recommended):

      python -m venv venv

      source venv/bin/activate

Install the project dependencies:

     pip install -r requirements.txt

Run the development server:

     python manage.py runserver

Access the API at http://localhost:8000/api/.

## API Endpoints

### List All Persons

URL: /api/persons/

Method: GET

Description: Retrieve a list of all persons.

Authentication: None required.

### Create a Person

URL: /api/persons/

Method: POST

Description: Create a new person.

Authentication: None required.

### Retrieve a Person

URL: /api/persons/{id}/

Method: GET

Description: Retrieve details of a specific person by ID.

Authentication: None required.

### Update a Person

URL: /api/persons/{id}/

Method: PUT

Description: Update details of a specific person by ID.

Authentication: None required.

### Delete a Person

URL: /api/persons/{id}/

Method: DELETE

Description: Delete a specific person by ID.

Authentication: None required.

### Usage

### You can interact with the API using tools like curl or Postman. Here's an example of using curl to create a new person:

      curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe"}' http://localhost:8000/api/persons/

### Contributing

Feel free to contribute to this project by submitting issues or pull requests.

In this README file, I've provided information on how to install and run the project, an overview of the API endpoints, and an example of how to use `curl` to interact with the API.



