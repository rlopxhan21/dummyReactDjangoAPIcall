# Django Rest Framework
An web application to add reviews & rating for movies. This project is still under development. For now, it just includes API endpoints, in future, react will be used iin the future.

## How to install:
In terminal bash:

```
git clone https://github.com/rlopxhan21/LopxhanBlog.git
```


After the clone is sucesful, add the project folder in IDE, then in in terminal of project folder:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

To run:

```
python manage.py runserver
```

If there is any error in the code, send me a email at rlopxhan21@gmail.com

## Available API EndPoints:
- For ```User```:
  
  -```POST``` /account/login
  
  -```POST``` /account/register
  
  -```POST``` /account/logout
 
 
 - For ```rating```:
 
  -```GET``` /video
 
 -```POST``` /video
  
 -```GET``` /video/<int:pk>
 
 -```PUT``` /video/<int:pk>
 
 -```PATCH``` /video/<int:pk>
 
 -```DELETE``` /video/<int:pk>
  
 -```GET``` /sp
 
 -```POST``` /sp
  
 
 -```GET``` /sp/<int:pk>
  
 -```PUT``` /sp/<int:pk>
 
 -```PATCH``` /sp/<int:pk>
 
 -```DELETE``` /sp/<int:pk>
  
 -```GET``` /video/<int:pk>/rating
  
 -```POST``` /video/<int:pk>/rating-create
  
  
 -```GET``` /video/rating/<int:pk>
  
 -```PUT``` /video/rating/<int:pk>
  
 -```PATCH``` /video/rating/<int:pk>
  
 -```DELETE``` /video/rating/<int:pk>
  
 -```GET``` /video/rating/<str:username>
  
  
