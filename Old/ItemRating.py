import pymongo
import sys

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

ratDB = myclient["ratingsDatabase"]

ratings = ratDB["ratings"]

argv = sys.argv
item = argv[1]

pipeline = [{"$group": { "_id" : "$Item", "Average": {"$avg": '$Rating'}}}, {'$match': {"_id" : item}}]

#

average = ratings.aggregate(pipeline)

val = list(average)[0]['Average']


print(val)