from setuptools import setup

setup(
    name='ilo',
    version='0.1',
    py_modules=['ex'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        ilo=commands:cli
    ''',
)
