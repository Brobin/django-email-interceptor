=================
Email Interceptor
=================

Django email interceptor provides email backends to intercept outgoing mail and mail them to a specified email instead.

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

