# Bookmarks

## Bookmarks is a social website that users can use to share external images with their friends.

This project run on Python 3.8.10

If you want to run the project in your local machine and modify it, you need to have [docker](http://docker.com/) and docker-compose installed.
After installing on your machine, rename the .env.example to .env and set your environment variables. After this run:
```sh
$ docker-compose up
```

### Social Networks Authentication
To be able to login using your social networks account, you'll nedd to edit your /etc/hosts file and set
it to mysite.com instead of localhost. That is because the social_django app needs a domain name and an TLS connection.
After editing yout /etc/hosts file, you are ready to go.