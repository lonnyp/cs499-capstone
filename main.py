# 
#
#

from pymongo import MongoClient
from functions import create_document,read_document,update_document,delete_document,menu
from login import login



# Allows connection to MongoDB on the local machine. Also connects to the database and collection
connection = MongoClient('localhost', 27017)
db = connection['students']
collection = db['information']

start = False

if __name__ == '__main__':
    
    start = login()
    
    if start == True:
        menu(connection,db,collection)
    else:
        print("end of program")
