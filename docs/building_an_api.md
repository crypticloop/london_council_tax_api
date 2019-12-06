# Building an API (with Flask)
>Building an API which can then be called by other apps

## Guide
https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

## Create route based on input
* Need to extract information from URL
* Then pass this into the page
* Route ready for input:
```
@app.route('/api/v1/tasks/<int:task_id>')
```
* `task_id` is now a variable
