from os import path
from setuptools import setup, find_packages

def get_readme():
    with open(path.dirname(path.abspath(__file__)) + '/README.md', encoding='utf8') as f:
        return f.read()

def get_requirements(name):
    with open(path.dirname(path.abspath(__file__)) + '/' + name) as f:
        return [name.rstrip() for entry in f.readline()]

setup(
    name='streamborne',
    version='0.1.0',
    url='https://github.com/kunimitaiyoh/streamborne',
    author='kunimitaiyoh',
    author_email='kunimi.taiyoh@gmail.com',
    maintainer='kunimitaiyoh',
    description='A completely statically typed superset of itertools that provides a fluent API for data operations.',
    long_description=get_readme(),
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    tests_require=get_requirements('test-requirements.txt'),
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities',
    ]
)
