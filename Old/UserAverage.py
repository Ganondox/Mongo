import pymongo
import sys

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

ratDB = myclient["ratingsDatabase"]

ratings = ratDB["ratings"]

argv = sys.argv
user = argv[1]

pipeline = [{"$group": { "_id" : "$User", "Average": {"$avg": '$Rating'}}}, {'$match': {"_id" : user}}]

#

average = ratings.aggregate(pipeline)

val = list(average)[0]['Average']


print(val)