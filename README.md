# ravelry-yarn-stasher

This is an application to scan yarn order confirmation emails and record the yarn stash using the Ravelry API.

Built using [FastAPI](https://fastapi.tiangolo.com/).

## Local Setup
(1) Set-up Credentials
Create a .env in the project base directory file with your credentials. You will need to create a Ravelry Developers 
Pro account to generate API username and password. Then create a new app to generate personal account access credentials.

Sample .env file:
```
# Ravelry API Auth
RAVELRY_USERNAME="<generated username>"
RAVELRY_PASSWORD="<generated password>"

RAVELRY_USER="<profile username>"
```

(2) Build and Run
To install requirements: `pip install -r requirements.txt`
To run: `fastapi dev main.py`

Then, Navigate to URL: http://127.0.0.1:8000/


References:
* [FastAPI](https://fastapi.tiangolo.com/)
* [Ravelry API](https://www.ravelry.com/api)[ravelryapi.py](ravelry%2Fravelryapi.py)