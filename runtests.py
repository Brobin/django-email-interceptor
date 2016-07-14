#!/usr/bin/env python
import sys
import django
from django.conf import settings
from django.test.utils import get_runner


def configure():
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'email_interceptor_test',
            }
        },
        MIDDLEWARE_CLASSES=(),
        INSTALLED_APPS=(
            'email_interceptor',
        ),
    )


def runtests():
    if not settings.configured:
        configure()
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True, failfast=False)
    failures = test_runner.run_tests(['email_interceptor', ])
    sys.exit(failures)


if __name__ == '__main__':
    runtests()
