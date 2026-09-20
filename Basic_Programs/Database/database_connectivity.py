import pymysql
#Execute SQL query
Query_src = """Select c.BusinessID,Client_name,e.DEPT,Project from data.clients c
right join data.employee e
on c.BusinessID = e.BusinessID"""
Query_trgt = '''Select c.BusinessID,Client_name,e.DEPT,Project from data.clients c
left join data.employee e
on c.BusinessID = e.BusinessID'''


def database_con():

    try:   # Establish a connection to MySQL database
        con = pymysql.connect\
            (host = "localhost", uname ="root",pwd= "Securepass6!",
                             db = "MySQL") # Localhost->local machine ,else IP address for remote address
        # Creating a cursor object that handles the records of a particular table
        cursor = con.cursor()
    except Exception as e:
        print("Database could not be connected as :", e.args)
    else:

        print("Database is connected successfully")
        return cursor


    # # c = 1
    # # try:
    # #     cursor.execute(Query_trgt)
    # #     # cursor.execute("SELECT VERSION()")
    # #     # store the result
    # #     results = cursor.fetchall()
    # #     print(cursor.rowcount)
    # #     for row in results:
    # #         BusinessID = row[0]
    # #         Client_name = row[1]
    # #         DEPT = row[2]
    # #         Project = row[3]
    # #         print(f'Row {c} data \n BusinessID: {BusinessID}\n Client_name: '
    # #               f'{Client_name}\n DEPT: {DEPT} \n Project: { Project}')
    # #         c += 1
    # #
    # #     # data = cursor.fetchone()
    # #     # # print("Print version of database : %s"%data)
    # #     # print("The retrieved data ", data)
    # #     # # Disconnecting from  database server
    # # except Exception as e:
    # #     print("Query didnot execute", ''.join(e.args))
    # return db
def closing_conn():
    database_con().close()

