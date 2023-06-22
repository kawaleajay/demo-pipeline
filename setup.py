from setuptools import setup, find_packages

setup(name="census-income",
      version="0.0.2",
      author="ajay",
      author_email="ajay.kawaleajay916@gmail.com",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )