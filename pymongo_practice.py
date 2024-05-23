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



collection = db.characters
pipeline = [
    {"$match": {"gender": "female"}},  # match docs where  gender is female
    {"$group": {"_id": None, "average_height": {"$avg": "$height"}}}  # group doc & calculate the avg height
]

result = list(collection.aggregate(pipeline)) # calls aggregation method then convert object to list

if result: # if there is a result from the above pipeline
    average_height_female = result[0]["average_height"] # fill var with first result
else:
    average_height_female = None

#print("Average height of female characters:", average_height_female)

tallest_character = collection.find_one(sort=[("height", -1)])

if tallest_character:
    print("The tallest character is:", tallest_character["name"])
else:
    print("No character found.")