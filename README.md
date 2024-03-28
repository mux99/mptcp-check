# mptcp-check
A website to check the validity of a mptcp connection

The website is designed with [Flask](https://flask.palletsprojects.com/en/3.0.x/), it can be installed with `pip install Flask`.
For test purposses, the app can be started with `flask run` from `/flask_app`.
For production, one of the [recommended](https://flask.palletsprojects.com/en/3.0.x/deploying/) app should be used instead.

For convegnance, `uwsgi` can be used with the provided `app.ini` config file.
simply run => `mptcpize run uwsgi --ini app.ini` preferably as root.

