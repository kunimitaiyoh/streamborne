# -*- coding:utf-8 -*-
from os import path
from setuptools import setup, find_packages

def get_readme():
    with open(path.dirname(__file__) + '/README.md', encoding='utf8') as f:
        return f.read()

setup(
    name='streamborne',
    version='0.0.1',
    url='https://github.com/kunimitaiyoh/streamborne',
    author='kunimitaiyoh',
    maintainer='kunimitaiyoh',
    description='A completely statically typed superset of itertools that provides a fluent API for data operations.',
    long_description=get_readme(),
    packages=find_packages(),
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3 :: Only'
    ]
)
