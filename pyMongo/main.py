import pymongo


if __name__ == "__main__":
    print('Welcome in pyMongo')

    # --------------------------------
    # connect MongoDb

    client = pymongo.MongoClient('mongodb://localhost:27017/')
    # print(client)

    # ------------------------
    # show all databases

    # allDBs = client.list_database_names()
    # print(allDBs)

    # ------------------------------
    # create database and collection

    db = client['anurag']
    collection = db['mySampleCollection']

    # ------------------------------
    # insert data in collection

    # collection.insert_one(
    #     {
    #     "item": "canvas",
    #     "qty": 100,
    #     "tags": ["cotton"],
    #     "size": {"h": 28, "w": 35.5, "uom": "cm"},
    #     }
    # )

    # db.mySampleCollection.insert_one(
    #     {
    #     "item": "canvas",
    #     "qty": 100,
    #     "tags": ["cotton"],
    #     "size": {"h": 28, "w": 35.5, "uom": "cm"},
    #     }
    # )

    # ----------------------------------------
    #  search data from collection

    # one = collection.find_one({"item":"mousepad"})
    # print(one)

    # one1 = db.mySampleCollection.find_one()
    # print(one1)

    # allDocs = collection.find({"item":"mousepad"}, {'item':1, '_id':0})
    # print(allDocs)
    # for item in allDocs:
    #     print(item)

    # ------------------------------------
    # show all collection

    # col = client['employee']
    # print( col.list_collection_names())

    # ------------------------------
    # update database

    # collection.update_one(
    #     {"item":"mat"},
    #     {
    #         "$set":{"qty":20}
    #     }

    #     )

    # or

    # prev = {"item": "mat"}
    # nextt = {"qty": 45}
    # # collection.update_one(prev, {"$set": nextt})

    # up = collection.update_one(prev, {"$set": nextt})
    # print(up.modified_count)


    # ----------------------------
    # delete data

    result = collection.delete_one({"item":"mat"})
    print(result.deleted_count)
    







