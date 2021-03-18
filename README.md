# Car Reviews

A web application that allows cars and reviews to be added to the website.

Author: Raihan Ahmed

## Requirements
- Python3
- Virtualenv
- Flask

## Setup For Linux
### Dependencies & Virtual Environment
The virtual environment and the application dependencies can be configured using the following:
```bash
git clone https://github.com/raihan1995/project_car.git
python3 -m venv venv
source venv/bin/activate
cd project_car
pip install -r requirements.txt
python3 app.py
```
_Note: You will have to change the database connection string, try using sqlite_
```bash
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
```

## Application Overview

The flask application allows users to add cars into the website and create a review about it. They can also update a review with new information regarding the car or delete the car itself.

What was considered during the design of the application:
 - Front end design using **FLask** framework, **python** coding language and **Jinja2** template engine
 - Flask framework used for the front-end which implements Werkzeug and WSGI to handle requests.
 - Jinja2 a template language to render pages.
 - CRUD functionality including ADD, SAVE, UPDATE and DELETE
 - Cloud integration by using a mySQL database hosted on GCP.
 - Unit Tests to validate the functionality of the application.

## Trello Board
![123](https://user-images.githubusercontent.com/35694370/111624169-3f0bdc80-87e3-11eb-8b1f-e299dbf01b63.png)

For an updated trello board please click [here](https://trello.com/b/gdGyTHrR/projectcar)


#### References

https://qa-community.co.uk

https://www.youtube.com/watch?v=jTiyt6W1Qpo
