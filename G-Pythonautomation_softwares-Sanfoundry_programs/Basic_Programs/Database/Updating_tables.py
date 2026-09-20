
import pymysql
Query='''UPDATE data.HDFC SET BRANCH='C' 
WHERE STATUS='A'
'''
try:
    # Establish a connection to MySQL database
    db = pymysql.connect("localhost", "root", "Securepass6!",
                         "MySQL")  # Localhost->local machine ,else IP address for remote address
    # Creating a cursor object that handles the records of a particular table
    cursor = db.cursor()
    try:
        cursor.execute(Query)
        db.commit()
    except Exception as e:
        print("Query didnot execute successfully",e.__name)
        db.rollback()
    else:
        print("Query executed successfully")
except Exception as e:
    print("Database could not be connected as :", e.args)
else:
    print("Database is connected successfully")
    
'''Updating from list of tuples without using loop
    items = [(101, 'Nik D300', 'Nik D300', 'DSLR Camera', 3),
             (102, 'Can 1300', 'Can 1300', 'DSLR Camera', 5),
             (103, 'gPhone 13S', 'gPhone 13S', 'Mobile', 10),
             (104, 'Mic canvas', 'Mic canvas', 'Tab', 5),
             (105, 'SnDisk 10T', 'SnDisk 10T', 'Hard Drive', 1)
             ]
  
    try:
        
        cursor.executemany("update ITEMS set quantity_in_stock = ? where item_id = ?",
                       [(4, 103),
                        (2, 101),
                        (0, 105)])'''
