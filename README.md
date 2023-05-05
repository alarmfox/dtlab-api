# DTLAB-API
This is an activity for DTLAB class about chapters 5-6 of DEVASC course.

## Description

You will work together to create a simple REST service that manages network devices.

The app will provide 3 core functionalities:
* **Managing switches**: users will have a CRUD interface for switches;
* **Managing routers**: users will have a CRUD interface for routers;

Each group will find more instructions for its task in the [*issues*](https://github.com/alarmfox/dtlab-api/issues) section.

*WARN* The following are guidelines. You can discuss on how to implement your solution to accomplish the task.

## Instructions

### Part 1 - Create a development environment (10 minutes)

The application uses [Flask](https://flask.palletsprojects.com/en/2.1.x/) and [Postgres](https://www.postgresql.org/docs/). 
First of all, install project dependencies after creating a new virtual env using the following command:

```
pip install -r requirements.txt
```

Start a Postgres instance using Docker. The application loads database configuration from `.env` file. In order to start Postgres, use the following command:

```sh
docker run -e POSTGRES_PASSWORD=postgres -p 5432:5432 postgres:alpine
```

*Think*: what does this command do? Try to understand every parameter to be able to explain it to other groups!

*WARNING* database configuration must match with the one provided in `.env`. Do not change variable names but only values (*after = sign*).

Now let's create the REST server using Flask, using the following command:

```sh
flask run
```

*HINT* to enable hot reload when developing, set `FLASK_ENV` variable to `development`. For example, on Linux:

```
FLASK_ENV=development flask run
```

Check if everything is working using the following command:

```
curl http://localhost:5000/test
```

or just open the browser at the `/test` endpoint!

### Part 2 - Implement the assigned function (40 minutes)

A CRUD interface is a set of standard operations that permits to Create, Read, Update and Delete data and represents the fundamental of a REST API.

Depending on what you have been assigned, open the correct file and create the requested endpoint. In each file, there is a variable called `~_blueprint` which holds the router.
Looking at the example routes and the documentation create the requested endpoint, minding that all routes are prefixed with a prefix specifified in `app.py`. For example, the switch endpoint is mounted at `/switches` which means that all requests that are going to hit the switches endpoint must match with this prefix. For example, a `GET` request may look like:

```
curl http://localhost:5000/switches
```

So everything added to the path will be appended to the prefix, for example a `/all` endpoint will become:

```
curl http://localhost:5000/switches/all
```

To test what you have done, use **Postman** as you learned in chapter 4.

#### Handler structure

Generally, an HTTP handler follows a standard structure:
* **get request data**: here you will have to look on how to get request data in Flask. Every request will have a JSON body (not every requests needs a body);
* **validate request data**: once you got data, you will have to assure that it is correct. Constraints are up to you! For example, you could make sure that an IP address or a netmask are valid;
* **perform requested operations**: in this phase, you will have to satisfy the request. For example, if the request is about storing a switch, now it's time to do it;
* **return a response**: based on what you have done in the previous step, you will have to return a response according to REST principles as HTTP codes.

#### Accessing the database

Database access is implemented using [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/). Usage is simplified with classes provided in `models.py` file. 
Look at the documentation linked above and example below to learn how to perform simple queries. 
Feel free to change everything as you want!

For example, to store a switch:

```python
from models import db, Switch

switch = Switch(
    hostname: 'switch1'
)
db.session.add(switch)
db.session.commit()
```

To query an object:

```python
from db import db, Switch

switch = Switch.query.filter_by(id=1).first()
```

#### Serialization

Serialization is about transforming an object into a string, so it can be send over the network as a stream of bytes. As it can be a very hard operation, every model in `models.py` offer a serialize method.
In order to return JSON object, you have tu use the `jsonify` function from Flask library.

```python
from db import db, Router
from flask import jsonify

router = Router.query.filter_by(id=1).first()
jsonify(router.serialize())
```

### Part 3 - Commit your changes (10 minutes)

After finishing the implementation, it's time to commit new changes and submit a pull request to the central repository!

You can learn on how to submit a pull request [here](https://opensource.com/article/19/7/create-pull-request-github).

## Bonus activities

Complete these activities once you have finished previous steps. The following steps can be completed at home either in group or individually.

### Bonus 1 - Prepare the application for a Docker deploy

Use what you have learned in chapter 6 to write a Dockerfile and deploy the application using the container model.

Here you will have a problem. Once the application is running in Docker container, it is in an isolated enviroment in its own LAN. How does our server communicate with the database (which is in it's own container)?

*HINT* in Docker you can create virtual networks. Docker will provide DNS service for two hosts in the same network, allowing to specify the container name as the hostname.
You may need to re-deploy the database.

### Bonus 2 - Protect the endpoint with authentication

Use what you have learned in chapter 4 and look at the [documentation](https://pythonhosted.org/Flask-JWT/) to protect your endpoint with JWT Authentication. 