#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pathlib
from setuptools import find_packages, setup

NAME = "kv2js"
DESCRIPTION = "Azure keyvault 2 json import / export tool"
AUTHOR = "r44v"

with open('requirements.txt' , 'r', encoding='utf-8') as f:
    REQUIRED = f.read().split('\n')

def get_version():
    p = pathlib.Path(".version")
    version = p.read_text(encoding="utf-8")
    major, minor, patch = (int(x) for x in version.split('.'))

    patch += 1

    version_new = str.join('.', map(str, (major,minor,patch)))
    p.write_text(version_new, encoding="utf-8")
    print(f"{version} -> {version_new}")
    return version_new

VERSION = get_version()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    packages=find_packages(),
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]
)