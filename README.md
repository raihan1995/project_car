# project_car

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
## Trello Board
![trello](https://imgur.com/a/SnQDS1P)
![123](https://user-images.githubusercontent.com/35694370/111624169-3f0bdc80-87e3-11eb-8b1f-e299dbf01b63.png)

