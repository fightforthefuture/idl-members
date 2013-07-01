# Getting Started

Installation of this app should be pretty simple:

## Prerequisites

- Python 2.x, where x >= 6
- [Virtualenv](http://www.virtualenv.org) >= 1.6

## Installation

Clone and enter the repository:

    git clone git@github.com:fightforthefuture/idl-members.git
    cd idl-members

Create an environment and install dependencies:

    virtualenv env --distribute
    source env/bin/activate
    pip install -r dev-requirements.txt

Set up the database:

    ./manage.py syncdb
    ./manage.py migrate --all

## Usage

In development, Django's [development server](https://docs.djangoproject.com/en/dev/ref/django-admin/#runserver-port-or-address-port) is used. To start the server:

    cd idl-members
    source env/bin/activate
    ./manage.py runserver

In production, this runs on Heroku, using [Green Unicorn](http://gunicorn.org/) and [gevent](http://www.gevent.org/).

## How it works

1. An IDL member configures and installs a JavaScript snippet to their page. 
2. That snippet creates and inserts a ``<script>`` tag into the page, with a ``src`` pointing to IDL's servers.
3. Based on the passed configuration, the Django application generates and returns a JavaScript file.
4. This JavaScript file creates and injects an ``<iframe>`` and ``<link rel="stylesheet">`` tag into the DOM of the IDL member's page.
5. To keep the application server's load down, the target stylesheet and iframe's ``src`` attribute both point to files hosted on Amazon S3.

# Architecture

## Apps

Currently, the project is comprised of three applications:

- ``campaigns`` - used to model and administer campaigns
- ``include`` - used for everything related to the member include code
- ``analytics`` - used for very basic analytics tracking of each impression

## Caching

[memcached](http://memcached.org/) is used heavily in production. As the site is extremely read-heavy, everything that could possibly be cached is: views, queries, template fragments, etc.

All caches are flushed whenever a ``Campaign`` object is created or modified. Additionally, a ``clearcache`` management command is provided to manually flush the entirety of the cache. Use this judiciously, lest you face the wrath of the [thundering herd](http://en.wikipedia.org/wiki/Thundering_herd_problem).

## Settings

Rather than use a traditional settings.py, a full settings module is used. ``__init__.py`` loads all settings from base.py, then attempts to load a local settings file, which is selected using the following logic:

1. If there is a file with a name identical to the machine's hostname, it will be imported (e.g. if the hostname is ``ubuntu``, then ``ubuntu.py`` is loaded).
2. If there is an environment variable named ``WSGI_EVIRONMENT``, a file with that variable's value will be loaded (e.g. if ``WSGI_ENVIRONMENT`` is set to ``production``, then ``production.py`` is loaded)
3. ``dev.py`` is loaded.

Settings in the local settings file overwrite those in ``base.py``.

## Static files

With one exception, all files involved in an include are served using ``django.contrib.staticfiles``, off Amazon S3 in production. This includes the CSS injected into IDL members pages, HTML source of the iframe, and all CSS and JavaScript files referenced within the iframe. One JavaScript file (the one produced by ``IncludeView``) is dynamically generated and is cached in memory, rather than served from S3.

### Minification

The JavaScript produced by ``IncludeView`` is minified by a template tag in the ``include`` app.

Currently, all other static files are minified by a [grunt](https://github.com/cowboy/grunt) script located in the ``static`` directory. In the near future, this task will be moved to a Django management command.