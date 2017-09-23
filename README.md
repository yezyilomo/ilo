# ilo
  This is a command line tool for managing database eg creating

# Available commands

Usage: ilo [OPTIONS] COMMAND [ARGS]...

Options:

  --help  Show this message and exit.

Commands:

  create_db: This is a command for creating a database with argument as db

             name to create

  drop:      This is a command for droping a database table with argument as

             table name for droping and option --all incase you want to drop

             all tables

  drop_db:   This is a command for droping a database with argument as

             database name to drop

  migrate:    This is a command for migrating database schema(defined as python

             classes) with argument as class name from which a database table

             is created and option --all incase you want to migrate all schema


# How to use it?

$ git clone https://github.com/yezyilomo/ilo

$ cd ilo

$ pip install --editable .  or   pip3 install --editable  .

Then you can start using it in your flask application
