import pymongo
import sys

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

ratDB = myclient["adjustedRatingsDatabase"]

ratings  = ratDB["ratings"]

argv = sys.argv
user = argv[1]
item = argv[2]
rating = argv[3]
ev = argv[4]
sd = argv[5]

query = {"User" : user, "Item" : item}
rating = { "$set" : { "Rating" : int(rating), "Ev" : float(ev), "Sd": float(sd) }}
ratings.update(query, rating, True)

