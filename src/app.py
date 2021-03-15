import mysql.connector

host = "127.0.0.1"
user = "root"
passwd = "toor"
database = "FYP"

def sql_queryname(input):
	conn = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)
	cursor = conn.cursor()
	sql_query = "select * from users where name = '%s'"
	name = input
	try:
		cursor.execute(sql_query % name)
		result=cursor.fetchall()
		return result
	except:
		return "Search Failed"


def sql_queryid(input):
	conn = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)
	cursor = conn.cursor()
	sql_query = "select * from users where id = '%s'"
	id = input
	try:
		cursor.execute(sql_query % id)
		result=cursor.fetchall()
		return result
	except:
		return "Search Failed"
