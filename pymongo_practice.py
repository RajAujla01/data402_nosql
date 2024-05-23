import pymongo

# connecting to mongodb
client = pymongo.MongoClient()
db = client["starwars"]

# db.collection.insert_one()
# db.collection.update_many()

# retrieve a document from the database
luke = db.characters.find({"name": "Luke Skywalker"})
#print(luke)
#(type(luke))

luke = db.characters.find_one({"name": "Luke Skywalker"})
#print(luke)
#(type(luke))

# getting only certain fields
luke_short = db.characters.find_one({"name": "Luke Skywalker"}, {"name": 1, "eye_color": 1, "_id": 0})
#print(luke_short)

# iterating though multiple records/documents
droids = db.characters.find({"species.name": "Droid"})
#print(droids)
#for droid in droids:
#    print(droid["name"])

