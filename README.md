### UPDATES
All updates and changes was made after deadline (Fri 9, February) and stored on **updates** branch.
1. Change logging database signals. Adding to exceptions DebugMiddlewareModel and DBLoggerModel.
2. Update custom calendar widget (located in user_profile/forms.py) with using bootstrap ui datepicker interface.

### TASK 1


For loading fixtures use `python manage.py loaddata initial.json`
Syncdb was deleted  in older Django versions.
Extended model which related on standard User model by One-to-One relationship  was created for implementing additional info for user.
In this project only **one user** with credentials:

login: **admin**

password: **superuser**


### TASK 2

All http request handled in custom middleware in app `debug_middleware`. CustomDebugMiddleware locate on 
`debug_middleware/middleware/requests_middleware.py`. Results available on http://127.0.0.1:8000/request_handler/

### TASK 3 

Template context processor locate on debug_middleware/context_processor directory. Results on 
http://127.0.0.1:8000/settings-context-processor/


### TASK 4-5

All forms and widget settings located on user_profile project. Result: http://127.0.0.1:8000/edit_profile/

### TASK 6

Custom simple_tag for creating admin link locate on user_profile/templatetags directory. 

http://127.0.0.1:8000/edit_tag_example/

### TASK 7

Management command model_info and script model_info.sh locate in app management_command.

### TASK 8

Handler for changing models was implemented with signals. 

http://127.0.0.1:8000/db_logger/


### TASK 9

On page /send you should choose delay time in seconds for request from server. Function `send_http_request_task` 
processes and sends the request in the background as the user continues to use the site (see async_queue app).
In venv must be installed Celery and redis-server on pc/server.
http://127.0.0.1:8000/send/
For launching:
`celery -A django_profile beat -l info`
(Response from httpbin.org in terminal)

### TASK 10

Every minute from https://baconipsum.com/api/?type=all-meat loaded random text and stored in database.

http://127.0.0.1:8000/random_text/



