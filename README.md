# Bookmarks

## Bookmarks is a social website that users can use to share external images with their friends.

If you want to run the project in your local machine and modify it, you have to install the requirements (enter in venv mode first):
```sh
$ pip install -r requirements.txt
```

After this, you have to rename the file `.env.example` to `.env` and change your SECRET_KEY.

Then, you should migrate all the project models to a database of your choice (you can configure the database in settings.py):

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

Finally, you can run the project in your machine:
```sh
$ python3 manage.py runserver
```