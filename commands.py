import click, os, sys
sys.path.append(os.getcwd())
from raw_db import *

@click.group()
def cli():
  pass

@click.command('create', short_help='This is a command for creating a database with argument as class name from which a db is created')
@click.argument('args', nargs=-1)
def create(args):
   if len(args)==0:
      try:
        run()
        print('\033[1m'+'\033[93m'+ "All table created successfully"+'\033[0m')
      except Exception as e:
        print('\033[1m'+'\033[91m'+"there was a problem in creating database"+'\033[0m')
        if 'run' not in globals():
           print("Method 'run' is not defined in your 'raw_db' file ")
        else:  
           print(e)
   else:
     
     for class_name in args:
       try:
         globals()[class_name]().create()
         print('\033[1m'+'\033[93m'+"'"+class_name+"' table created successfully"+'\033[0m')
       except Exception as e:
          print('\033[1m'+'\033[91m'+"failed to create '"+class_name+"' table"+'\033[0m')
          if class_name not in globals():
             print("Class '"+class_name+"' is not defined in your 'raw_db' file")
          else:
             print(e)

          
cli.add_command(create)
