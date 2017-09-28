import click, os, sys
sys.path.append(os.getcwd())
try:
  from raw_db import *
except Exception as e:
    print('\033[1m'+'\033[91m'+"Your are not in the right directory!."+'\033[0m')
    print("Please make sure you are in '.../database' directory and there is 'raw_db.py' in it.\n")


@click.group()
def cli():
  pass

@click.command('migrate', short_help='This is a command for migrating database schema(defined as python classes) with argument as class name from which a database table is created')
@click.argument('args', nargs=-1)
@click.option('--all', 'flg', flag_value='all', default=True)
def migrate(args,flg):
   if len(args)==0 and flg=='all':
      try:
        run()
        print('\033[1m'+'\033[93m'+ "All tables created successfully"+'\033[0m')
      except Exception as e:
        print('\033[1m'+'\033[91m'+"there was a problem in creating database"+'\033[0m')
        if 'run' not in globals():
           print("Method 'run' is not defined in your 'raw_db' file ")
        else:
            print (e.args[1])

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
             print (e.args[1])

@click.command('drop', short_help='This is a command for droping a database table with argument as table name for droping and option --all incase you want to drop all tables')
@click.option('--all', 'flg', flag_value='all')
@click.argument('tables', nargs=-1)
def drop(tables,flg):
     if len(tables)==0 and flg != 'all':
       print('\033[1m'+'\033[91m'+"Specify table(s) to drop!."+'\033[0m')
       return

     if flg=='all':
        if len(db.db__tables__)==0:
          print('\033[1m'+'\033[91m'+"No table to drop!."+'\033[0m')
          return
        for table in db.db__tables__:
          try:
            db.drop_tb_without_foreign_key_check(table)
            print('\033[1m'+'\033[93m'+"'"+table+"' table dropped successfully"+'\033[0m')
          except Exception as e:
             print('\033[1m'+'\033[91m'+"failed to drop '"+table+"' table"+'\033[0m')
             if table not in db.db__tables__:
                print("'"+table+"' is not defined in your database")
             else:
                print (e.args[1])
        return

     for table in tables:
       try:
         db.drop_tb_with_foreign_key_check(table)
         print('\033[1m'+'\033[93m'+"'"+table+"' table dropped successfully"+'\033[0m')
       except Exception as e:
          print('\033[1m'+'\033[91m'+"failed to drop '"+table+"' table"+'\033[0m')
          if table not in db.db__tables__:
             print("'"+table+"' is not defined in your database")
          else:
             print (e.args[1])


@click.command('create_db', short_help='This is a command for creating a database with argument as db name to create')
@click.argument('db_name')
def create_db(db_name):
       try:
         db.create_db(db_name)
         print('\033[1m'+'\033[93m'+"'"+db_name+"' database created successfully"+'\033[0m')
       except Exception as e:
          print('\033[1m'+'\033[91m'+"failed to create '"+table+"' database"+'\033[0m')
          print (e.args[1])

@click.command('drop_db', short_help='This is a command for droping a database with argument as database name to drop')
@click.argument('db_name', nargs=-1)
def drop_db(db_name):
     for name in db_name:
       try:
         db.drop_db(name)
         print('\033[1m'+'\033[93m'+"'"+name+"' database dropped successfully"+'\033[0m')
       except Exception as e:
          print('\033[1m'+'\033[91m'+"failed to drop '"+name+"' database"+'\033[0m')
          print (e.args[1])

@click.command('truncate', short_help='This is a command for truncating a database table with argument as table name to truncate and option --all incase you want to truncate all tables')
@click.option('--all', 'flg', flag_value='all')
@click.argument('tables', nargs=-1)
def truncate(tables,flg):
     if len(tables)==0 and flg != 'all':
       print('\033[1m'+'\033[91m'+"Specify table(s) to truncate!."+'\033[0m')
       return

     if flg=='all':
        if len(db.db__tables__)==0:
          print('\033[1m'+'\033[91m'+"No table to truncate!."+'\033[0m')
          return
        for table in db.db__tables__:
          try:
            db.truncate_tb_without_foreign_key_check(table)
            print('\033[1m'+'\033[93m'+"'"+table+"' table truncated successfully"+'\033[0m')
          except Exception as e:
             print('\033[1m'+'\033[91m'+"failed to truncate '"+table+"' table"+'\033[0m')
             if table not in db.db__tables__:
                print("'"+table+"' is not defined in your database")
             else:
                print (e.args[1])
        return

     for table in tables:
       try:
         db.truncate_tb_with_foreign_key_check(table)
         print('\033[1m'+'\033[93m'+"'"+table+"' table truncated successfully"+'\033[0m')
       except Exception as e:
          print('\033[1m'+'\033[91m'+"failed to truncate '"+table+"' table"+'\033[0m')
          if table not in db.db__tables__:
             print("'"+table+"' is not defined in your database")
          else:
             print (e.args[1])


cli.add_command(migrate)
cli.add_command(drop)
cli.add_command(create_db)
cli.add_command(drop_db)
cli.add_command(truncate)
