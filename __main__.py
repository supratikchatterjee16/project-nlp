from config import pgsql_config
from source.gcide import gcide2_insertion

config = pgsql_config

if __name__ == '__main__':
	gcide2_insertion.run()
