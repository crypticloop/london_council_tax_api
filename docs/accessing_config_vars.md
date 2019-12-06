# Accessing Heroku Config Vars
>A method of mitigating need for secrets stored in plain text

## Setting Vars
### UI
* Go to `https://dashboard.heroku.com/apps/[app-name]/settings`
  * Also found where on far right of dashboard toolbar
* Enter key and value
  * Convention: Key in **capitals**

### CLI
* Also a way to do it with CLI, but don't use that that much

## Accessing from code
* Guide: https://devcenter.heroku.com/articles/config-vars#managing-config-vars
* Use `os` library `environ` object
```
@app.route('/test_secret')
def return_secret():
    return os.environ['SECRET_TEST_VAR']
```
