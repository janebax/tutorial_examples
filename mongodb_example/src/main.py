from pymongo import MongoClient
from login import username, password, url

# Replace the uri string with your MongoDB deployment's connection string.
uri = (
    f"mongodb+srv://{username}:{password}@{url}?retryWrites=true&writeConcern=majority"
)

client = MongoClient(uri)

# database and collection code goes here
db = client.sample_guides
coll = db.planets
# find code goes here
cursor = coll.find({"hasRings": True})
# iterate code goes here
for doc in cursor:
    print(doc)
# Close the connection to MongoDB when you're done.
client.close()
