# flask_restful_backend
Basic restful backend service with flask. Features:
  - Flask for backend api
  - Restful api
  - env file manage environment variable
  - Integrated with posrgresql and redis
  - Authorization based on jwt
  - Docker support
  - Python3

# Table of content
  - [Installation](#Installation) 
  - [Run locally](#Run-locally)
    - [Preparation](#Preparation)
    - [Migration](#Migration)
    - [Run](#Run)
    - [Tests](#Tests)
  - [Run with docker](#Run-with-docker)

# Installation
  -  git clone https://github.com/alexcc4/flask_restful_backend
  -  python3 installed
  
# Run locally

## Preparation
  - Redis and postgresql service running
  - Add code  to your local hosts file
  ```
  127.0.0.1	postgres
  127.0.0.1	redis
  ```
  - Manually create postgres user and db which your app need
  - `pip install -r requirements.txt`
  - `cp .env.sample .env.development`
  - `export PYTHON_ENV=development`

## Migration
  - `python manage.py db migrate`
  - `python manage.py db upgrade`

## Run
  - `python3 manage.py runserver`
  - `curl http://localhost:5000/api/v1/index`
  ```
    {
      "hello": "hello world!"
    }
  ```
  
## Tests
  -  Manually create postgres user and db which your app testing need
  - pytest 


# Run with docker
  - requirements: docker, docker-compose
  - chmod +x build.sh && ./build.sh`
  - `curl http://localhost:3000/api/v1/index`
  ```
    {
      "hello": "hello world!"
    }