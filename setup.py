import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='django-hiken',
    version='0.1',
    packages=['django_hiken'],
    description='A line of description',
    long_description=README,
    author='jefri',
    author_email='sosmed.jefrihutama@gmail.com',
    url='https://github.com/ioiiiioi/django_hiken/',
    license='BSD',
    install_requires=[
        'Django>=4.3',
    ]
)