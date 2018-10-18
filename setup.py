from setuptools import setup, find_packages

PROJECT = "tinder"
VERSION = "0.0.0"
DESC = "Python wrapper for the Tinder API"
LONG_DESC = open("README.md").read().strip()
AUTHOR = "Vikash Kothary"
AUTHOR_EMAIL = "kothary.vikash@gmail.com"
URL = "https://github.com/Vikash-Kothary/tinder-api-python"
LICENSE = open("LICENSE").read().strip()

setup(name=PROJECT,
      version=VERSION,
      description=DESC,
      long_description=LONG_DESC,
      long_description_content_type="text/markdown",
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      license=LICENSE,
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          "requests==2.20.0",
          "robobrowser==0.5.3",
          "lxml==4.2.5"
      ],
      keywords=["tinder-api", "tinder", "python-3", "robobrowser"],
      classifiers=[
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Intended Audience :: End Users/Desktop",
          "Operating System :: OS Independent",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 2.7",
          "Topic :: Internet :: WWW/HTTP",
          "Environment :: Console"
      ],
      )
