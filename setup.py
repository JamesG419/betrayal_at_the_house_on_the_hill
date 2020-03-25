#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="James Glenister",
    author_email='jglen419@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python package of BatHotH board game",
    entry_points={
        'console_scripts': [
            'betrayal_at_the_house_on_the_hill=betrayal_at_the_house_on_the_hill.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='betrayal_at_the_house_on_the_hill',
    name='betrayal_at_the_house_on_the_hill',
    packages=find_packages(include=['betrayal_at_the_house_on_the_hill', 'betrayal_at_the_house_on_the_hill.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/JamesG419/betrayal_at_the_house_on_the_hill',
    version='0.1.0',
    zip_safe=False,
)
