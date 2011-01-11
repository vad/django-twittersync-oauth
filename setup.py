#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
    from setuptools.command.test import test
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
    from setuptools.command.test import test

long_description = open('README.rst').read()

setup(
    name='django-twittersync-oauth',
    version='0.1',
    author='Davide Setti',
    author_email='davide.setti@gmail.com',
    url='http://github.com/vad/django-twittersync-oauth',
    description = 'OAuth Plugin for django-twittersync',
    packages=find_packages(),
    license='BSD License',
    zip_safe=False,
    install_requires=[
        'Django',
        'twitter',
        'django-twittersync',
    ],
    include_package_data=True,
    long_description=long_description,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development'
    ],
)
