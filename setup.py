import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-djmongo',
    version='0.1',
    packages=['djmongo', 'djmongo.console', 'djmongo.search','djmongo.dataimport' ],
    include_package_data=True,
    license='Public Domain',  
    description='Django app providing a MongoDB Web UI and REST API Toolkit.',
    long_description=README,
    url='https://github.com/hhsidealab/django-djmongo',
    author='Alan Viars',
    author_email='alan.viars@cms.hhs.gov',
    install_requires=[
        'pymongo', ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)


