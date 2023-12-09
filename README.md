## The backend

```
python -m venv venv
source venv/bin/activate
```

```
pip install Flask
pip install Flask-SQLAlchemy
pip install Flask-Migrate
pip install mysqlclient
pip install Flask-Bcrypt
```

```
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```
