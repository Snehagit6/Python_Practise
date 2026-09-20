import pymysql


def main():
    sql = '''CREATE TABLE ITEMS(item_id not null integer, item_name varchar(30), item_description varchar(30),
    item_category text, quantity_in_stock integer)'''
    conn = pymysql.connect("localhost", "root", "Securepass6!",
                             "MySQL")
    #create connection cursor
    cursor = conn.cursor()
    #create table ITEMS using the cursor
    try:
        cursor.execute(sql)
    #commit connection 
        cursor.commit()
        res = cursor.execute("Select * from ITEMS")
        print(res)
    except  Exception as e:
        return ('Unable to perform transaction',e.args)
    #close connection
    finally:
        cursor.close()

if __name__=="__main__":
    print(main())