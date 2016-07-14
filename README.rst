=================
Email Interceptor
=================

Django email interceptor provides email backends to intercept outgoing mail and mail them to a specified email instead.

-------

|python| |pypi| |license| |travis| |django|

-------

Quickstart
==========

Install via pip

.. code-block:: bash

    pip install django-email-interceptor

Add to installed apps:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'email_interceptor',
        ...
    )

Change the email backend to use interceptor and set an email to send the intercepted mail to:

.. code-block:: python

    EMAIL_BACKEND = 'email_interceptor.backends.SmtpInterceptorBackend'

    INTERCEPTOR_EMAIL = 'test@example.com'

Testing
=======

To run tests, install the requirements for testing and run!

.. code-block:: bash
    
    pip install -r requirements/test.txt
    python runtests.py


.. |python| image:: https://img.shields.io/pypi/v/django-email-interceptor.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-email-interceptor/
    :alt: Supported Python versions

.. |pypi| image:: https://img.shields.io/pypi/pyversions/django-email-interceptor.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-email-interceptor/
    :alt: Latest Version

.. |license| image:: https://img.shields.io/pypi/l/django-email-interceptor.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-email-interceptor/
    :alt: License

.. |travis| image:: https://img.shields.io/travis/Brobin/django-email-interceptor.svg?style=flat-square
    :target: https://travis-ci.org/Brobin/django-email-interceptor/
    :alt: Travis CI

.. |django| image:: https://img.shields.io/badge/Django-1.8, 1.9-orange.svg?style=flat-square
    :target: http://djangoproject.com/
    :alt: Django 1.7, 1.8
