# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

REQUIRED = [
    "mutagen",
    "pycryptodome",
]

setup(
    name='ncmdump',
    version='0.1.1',
    description='netease cloud music copyright protection file dump',
    url='http://github.com/nondanee/ncmdump',
    author='nondanee',
    author_email='iminezn5656@outlook.com',
    license='MIT',
    keywords=('ncm', 'netease cloud music'),
    packages=find_packages(),
    platforms='any',
    zip_safe=False,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=REQUIRED,
    entry_points={
        'console_scripts': [
            'ncmdump=ncmdump.app:main'
        ]
    }
)
