
from pymongo import MongoClient
import json
import re

"""
given the MSAN_697 Homework2 json file

Example
{
	"url":"mongodb://<user>:<password>@linus.mongohq.com:10024/MSAN_697",
	"dbname":<database>,
	"collection":<collection>,
	"user":<username>, 
	"pass":<password>
}
"""

def connectDB(param):
	#get the parameter
	url = param['url']
	dbname = param['dbname']
	collection = param['user']
	user = param['user']
	pwd = param['pass']

	#replacing the user name
	url = re.sub(r'<user>',user,url)
	#replacing the password
	url = re.sub(r'<password>',pwd,url)

	print url
	# connect the MongoDB
	client = MongoClient(url)
	# show the collections
	print "=========Collection========="
	for i in client[dbname].collection_names():
		print i
	#return DB
	return client[dbname]
