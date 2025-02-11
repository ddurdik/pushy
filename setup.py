import os,sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args="./tests/test_pushysdk.py"

    def run_tests(self):
        import shlex
        import pytest
        errno=pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def makeLongDescription():
    this_directory = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        return f.read()

setup(
    name="PushySDK",
    version="0.1.6",
    author="Rob Kent",
    author_email="jazzycamel@googlemail.com",
    description="A very simple Python client for the Pushy notification service API.",
    license="MIT",
    keywords="Pushy Notification API",
    url="https://github.com/jazzycamel/pushy",
    packages=find_packages(exclude=['docs','tests']),
    install_requires=['requests','six'],
    tests_require=['pytest','pytest-cov'],
    cmdclass={'test': PyTest},
    long_description=makeLongDescription(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",       
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: MIT License",
    ]
)
