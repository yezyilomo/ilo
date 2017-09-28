from setuptools import setup
import commands

setup(
    name='ilo',
    version='1.0',
    py_modules=['commands'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        ilo=commands:cli
    ''',
)
