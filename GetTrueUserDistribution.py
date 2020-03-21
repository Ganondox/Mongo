import pymongo
import sys

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

ratDB = myclient["adjustedRatingsDatabase"]

ratings = ratDB["ratings"]

argv = sys.argv
user = argv[1]

lower_pipeline = [ {'$match': {"User" : user}} ]


# , {'$project': {"Rating": {"$map": {"input": "$Rating", "in": {"$add": ["$$this", -0.5]}} }} }

#average = ratings.aggregate(pipeline)

lower = ratings.aggregate(lower_pipeline)

print(list(lower))

#val = list(average)[0]['Average']


#print(val)