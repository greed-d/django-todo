# Django Todo

## Motivation :
Was learing django so made a simple todo app to understand how views, models and templates interact with each other

## Usage
- Clone the repo and enter it
```
git clone git@github.com:greed-d/django-todo.git
cd django-todo
```

- Install Python ( Command for Arch based distro)
```
sudo pacman -S python
```
- Start venv 
```
python -m venv venv
```

- Source the venv
```
source venv/bin/activate
```
use `activate.fish` if you're using fish terminal

- Install requirements
```
pip install -r requirements.txt
```
- Run Project
```
python manage.py runserver
```
- This should output something like :
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 19, 2024 - 04:06:05
Django version 5.1.4, using settings 'todo_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
- Go to the link it provides, `127.0.0.1:8000/` in my case


