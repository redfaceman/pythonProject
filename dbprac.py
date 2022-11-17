from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.k0y47s6.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

all_users = list(db.users.find({}))

for user in all_users:
    print(user)
