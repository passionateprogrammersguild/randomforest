# Copyright 2019 NLP Logix Corp.

from setuptools import setup, find_packages


setup(
    name='randomforest',

    version='1.0.0',

    description='Random Forest Classifier',
    long_description='',

    author='NLP Logix',
    author_email='michael.mann@nlplogix.com',   

    py_modules=["randomforest.evaluator", "randomforest.node"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"]
)
