# Lagos PC BOOM!

Go to https://urop.dhmit.xyz/sonification/
And follow the steps (substituting `sonification` for `lagos-pc-boom`)
We don't have a frontend server, so only follow the backend instructions. And ask @anastasia if you get stuck!

Once backend is set up and running on port :8000, you will want to create a superuser, which will allow you to use the admin interface. 
Open a terminal window:
```
cd lagos
python manage.py createsuperuser
```
You can set it to something simple like 
username: admin
email: admin@example.com
password: password

This is just for development purposes! 

## The project structure, briefly
```
lagos
    | - app/ (our project root)
        | - settings/
        | - static/ (top-level static assets, like global CSS)
        | - templates/ (top-level templates, like base.html which other html files build on top of)
        | - urls.py (check out search URL which we get for free! Woo!)
    | - blog/ (our blog app, running on `blog.localhost:8000/`)
    | - home/ (our home app, running on `localhost:8000`)
    | manage.py (script to start up server, gets run every time `Run backend` is run)
    | requirements.txt (includes everything we need to run this project, so far)
```