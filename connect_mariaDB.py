import configparser
import mariadb

config = configparser.ConfigParser()
config.read('db_config.ini')
host = config.get('MySQL', 'host')
user = config.get('MySQL', 'user')
password = config.get('MySQL', 'password')
database = config.get('MySQL', 'database')

db_config = {
    'host': host,
    'user': user,
    'password': password,
    'database': database
}

connect = mariadb.connect(**db_config)
