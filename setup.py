import os
from setuptools import setup


def read_file(filename):
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    return open(filepath).read()


setup(
    name='django-email-interceptor',
    version='0.1',
    author='Tobin Brown',
    author_email='tobin@brobin.me',
    packages=['email_interceptor'],
    url='https://github.com/Brobin/django-email-interceptor',
    license='MIT',
    description='Simple backend to intercept emails during development',
    classifiers=(
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
    long_description=read_file('README.rst'),
    test_suite="runtests.runtests",
    zip_safe=False,
)
