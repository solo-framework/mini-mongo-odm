# encoding=utf8

from setuptools import setup

setup(name='mini-mongo-odm',
      version='1.0',
      description='Easy MongoDB Object Document Mapper',
      url='https://github.com/solo-framework/mini-mongo-odm',
      author='Andrey Filippov',
      author_email='a.fiwork@gmail.com',
      license='MIT',
      packages=['mini-mongo-odm'],
      install_requires=[
          'mongoengine',
      ],
      zip_safe=False)