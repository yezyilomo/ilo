# ilo
  This is a command line tool for managing simple database operations, it comes with
  several powerful commands for database manipulations

# Available commands

Usage: ilo [OPTIONS] COMMAND [ARGS]...

Options:

  --help  Show this message and exit.

Commands:


create_db:

      This is a command for creating a database with argument as db name to create

drop:
  
      This is a command for droping a database table with argument as table name for 
      
      droping and option --all incase you want to drop all tables

drop_db:
  
      This is a command for droping a database with argument as database name to drop

migrate:
  
      This is a command for migrating database schema(defined as python classes) with 
      
      argument as class name from which a database table is created and option --all 
      
      incase you want to migrate all schema
      
truncate:

      This is a command for truncating a database table with argument as table name 
      
      to truncate and option --all incase you want to truncate all tables 


# How to use it?

$ pip3 install ilo

But if you have dorm in your system, you don't need to install ilo, because dorm install

it automatically

