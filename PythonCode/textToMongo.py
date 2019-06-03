from pymongo import MongoClient
import os

client = MongoClient()
db = client.test_database  # use a database called "test_database"
collection = db.files   # and inside that DB, a collection called "files"

txtDir = "D:/MajorProject/Python code/text/"
if txtDir == "": txtDir = os.getcwd() + "\\"  # if no pdfDir passed in
for txt in os.listdir(txtDir):
    fileExtension = txt.split(".")[-1]
    if fileExtension == "txt":
        f = open(txtDir + txt)  # open a file
        text = f.read()    # read the entire contents, should be UTF-8 text

        # build a document to be inserted
        text_file_doc = {"file_name": txt, "contents" : text }
        # insert the contents into the "file" collection
        collection.insert_one(text_file_doc)



