## Create a python virtual env
python -m venv env

## install dependencies
pip install -r requirements.txt

## Update requirements.txt
pip freeze > requirements.txt

## How to run
Set up correct environment variables
1. .env file, set DB_CONFIG to your db connection url, something like below:-  
DB_CONFIG=postgresql+asyncpg://{username}:{password}@localhost:5432/postgres

2. Run the backend server using the command below:-

uvicorn main:app --reload