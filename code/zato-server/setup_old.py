# -*- coding: utf-8 -*-

"""
Copyright (C) 2019, Zato Source s.r.o. https://zato.io

Licensed under AGPLv3, see LICENSE.txt for terms and conditions.
"""

# flake8: noqa
from setuptools import setup, find_packages
import os
version = '3.2'
def parse_requirements(requirements):
    ignored = ['#', 'setuptools', '-e']

    with open(requirements) as f:
        return [line.split('==')[0] for line in f if line.strip() and not any(line.startswith(prefix) for prefix in ignored)]

setup(
      name = 'zato-server',
      version = version,

      author = 'Zato Source s.r.o.',
      author_email = 'info@zato.io',
      url = 'https://zato.io',

      package_dir = {'':'src'},
      packages = find_packages('src'),

      namespace_packages = ['zato'],
      install_requires = parse_requirements(
          os.path.join(os.path.dirname(os.path.realpath(__file__)), 'requirements.txt')),

      zip_safe = False,
)
