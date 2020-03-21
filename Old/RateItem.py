import pymongo
import sys

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

ratDB = myclient["ratingsDatabase"]

ratings  = ratDB["ratings"]

argv = sys.argv
user = argv[1]
item = argv[2]
rating = argv[3]


query = {"User" : user, "Item" : item}
rating = { "$set" : { "Rating" : int(rating) }}
ratings.update(query, rating, True)

