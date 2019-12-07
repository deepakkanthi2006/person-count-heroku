# person-count-heroku
This is a Django app, which can easily be deployed to Heroku.
The app use machiine learning CNN Caffe model to find person count in image / video which play on web page .
Code is collected from various blog post available on internet .
Special thanks to [Adrian at PyImageSearch](https://www.pyimagesearch.com/) .
You can visit this web-site which has great material for image processing using machine learning. 

[Live App URL](https://vast-fortress-26654.herokuapp.com)
How to Use App :
1. Set 'Video URL' , right now only mp4 files are supported .
    (We have supplied three files with app /static/example1.mp4 , /static/example2.mp4 , /static/example3.mp4)
2. After playing the video ,click  'Show Number Of Person' button .
     It would show person count and image/ Frame .


## Running Locally

Make sure you have Python 3.6.8 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/deepakkanthi2006/person-count-heroku.git
$ cd person-count-heroku

$ python3 -m venv person-count
$ pip install -r requirements.txt

$ createdb person_count_db

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:8000](http://localhost:8000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
