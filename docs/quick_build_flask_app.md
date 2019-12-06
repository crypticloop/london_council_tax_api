#  Quick Build Flask App

## Overview
1. Create app.py
2. Create virtualenv
3. Create Procfile
4. Create requirements file
5. Set up link in Heroku UI

## 1. Create app.py
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'
```

## 2. Create virtualenv
* At top level of repo
```
$ virtualenv flask_app
```
* Install all required packages inside this
* To start:
```
source flask_app/bin/activate
```
* To exit:
```
$ deactivate
```

## 3. Create Procfile
* At top level of repo
* Create file with `gunicorn` specifier
  * Upgrade to built-in heroku web app
* Inside file:
```
web: gunicorn app:app
```

## 4. Create requirements.txt
* Easiest way is with a `pip freeze` inside venv
* Output results to file at directory root
```
$ pip freeze > requirements.txt
```
