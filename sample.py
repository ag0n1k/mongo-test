from pymongo import MongoClient
import pprint
import datetime

client = MongoClient('localhost', 27017)
print(client)

db = client.test_database
print(db)

post = {
    "author": "Mike",
    "text": "My third blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()
}

posts = db.posts
print(posts)

post_ = posts.insert_one(post)

pprint.pprint(posts.find_one())
