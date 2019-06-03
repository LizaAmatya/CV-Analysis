from pymongo import MongoClient

client = MongoClient()
db = client.test_database  # use a database called "test_database"
collection = db.files   # and inside that DB, a collection called "files"
txt='Chandan Singh.txt'
f = open(txt)  # open a file
text = f.read()    # read the entire contents, should be UTF-8 text

Data = text.replace('\t', '\n').split('\n')
parsedData = text.split('\n')
text_file_doc = {"file_name": txt, "contents" : parsedData} #showa o/p im cmd window by connecting it with mongodb
# print(text_file_doc)

# content= set(text.strip().split())
# text_file_doc = {"file_name": txt, "contents" : content }
# print (text_file_doc)

# # build a document to be inserted
# # insert the contents into the "file" collection
# collection.insert_one(content)