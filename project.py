import os
import sqlite3
from sqlite3 import Error
   ## Include SQLite package
import random

################ Connect SQLite Database ################

db_connection = None # Define the connection parameter
#db_name = "/Users/bowma/CSE 111/Project/CSE111-Project-F20/moviesdata.db" # Specify the full path of Database file
db_name = "/Users/bowma/CSE 111/Project/CSE111-Project-F20/project.db"
#db_name = "moviesdata.db"

# def openConnection(_dbFile): 
#     print("++++++++++++++++++++++++++++++++++")
#     print("Open database: ", _dbFile)
#     conn = None
#     try:
#         conn = sqlite3.connect(_dbFile)
#         print("success")
#     except Error as e:
#         print(e)

#     print("++++++++++++++++++++++++++++++++++")

#     return conn