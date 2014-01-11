# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages


def get_text_from_file(fn):
    text = open(fn, 'rb').read()
    if sys.version_info >= (2, 6):
        return text.decode('utf-8')
    return text

setup(
    name="buildout.recipe.uwsgi",
    version="0.0.20",
    description="Buildout recipe downloading, compiling and configuring uWSGI.",
    long_description=get_text_from_file("README.rst"),
    author="Cosmin Lu\xc8\x9b\xc4\x83",
    author_email="q4break@gmail.com",
    license="BSD",
    url="http://github.com/lcosmin/buildout.recipe.uwsgi",
    packages=find_packages(),
    include_package_data=True,
    namespace_packages=["buildout"],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Buildout",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=[
        "zc.recipe.egg",
        "setuptools"
    ],
    zip_safe=False,
    entry_points={"zc.buildout": ["default = buildout.recipe.uwsgi:UWSGI"]}
)
