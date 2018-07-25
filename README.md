hx mirador
===============

lti provider of mirador instances.


quick start
============

hxmirador (specifically, hxlti) requires a redis instance running, and by default it will look for
`redis://localhost:6379/0`. Make sure there is a redis instance running and
configured in hxmirador/settings/prod.py

To stand a local hxmirador lti provider instance, follow these quick steps:

    # clone this repo
    $> git clone https://github.com/nmaekawa/hxmirador.git
    $> cd hxmirador

    # create and activate a virtualenv
    $> cd hxmirador
    $hxmirador> virtualenv -p python3 venv
    $hxmirador> source venv/bin/activate
    $(venv) hxmirador>

    # install pip requirements
    $(venv) hxmirador> pip install -r requirements/dev.txt

    # install hxmirador
    $(venv) hxmirador> pip install -e .

    # edit the dotenv sample.env file as you wish
    $(venv) hxmirador> cp hxmirador/settings/sample.env ./sample.env
    $(venv) hxmirador> vi sample.env
    ...

    # run migrations
    $(venv) hxmirador> (HXMIRADOR_DOTENV_PATH=sample.env manage.py migrate)

    # create django admin superuser
    $(venv) hxmirador> (HXMIRADOR_DOTENV_PATH=sample.env manage.py createsuperuser)
    ...

    # run hxmirador
    $(venv) hxmirador> (HXMIRADOR_DOTENV_PATH=sample.env manage.py runserver)

If all goes well, you should be able to access django admin ui at:

    http://localhost:8000/admin

using the superuser you just created, and then create a `consumer` key.


hxmirador is part of [hximg][https://github.com/nmaekawa/hximg-provision] (hx
backend for mirador), please refer to its readme for details in how to stand a
vagrant instance.


# about lti consumer config for hxmirador lti provider

You can configure your lti consumer with the consumer key created in the
previous step. Other lti configs are:

    launch_url: http://localhost:8000/mirador/launch
    
    custom_manifests: ["http://manifests.vm/manifests/sample:m123"]
    

Keep in mind that the lti consumer has to also be local!


# about hxmirador configuration

hxmirador has hxlti as dependency to implement the lti provider and hxlti needs
some configs in the env (see dotenv `hxmirador/settings/sample.env`):

    # dummy consumer key for oauthlib
    HXLTI_DUMMY_CONSUMER_KEY
    ex: HXLTI_DUMMY_CONSUMER_KEY='123456789012345678901234567890'

    # url for redis instance
    HXLTI_REDIS_URL
    ex: HXLTI_REDIS_URL='redis://localhost:6379/0'

for details on hxlti django app, see
[hxlti-djapp][https://github.com/nmaekawa/hxlti-djapp.git]

---eop


