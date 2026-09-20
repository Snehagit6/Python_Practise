import pymysql
from Basic_Programs.Database.database_connectivity import database_con
Query='''Select * from data.employee
'''
Col_query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'HDFC'"
cursor = database_con()

def col_count():
    column_num = cursor.execute(Col_query)
    return column_num
def table_records():
    try:
        c = 1


        #     # store the result
        results_1 = (cursor.fetchall())
        col_list=[]
        i=0
        j=0
        while(i<col_count()):
            val=results_1[i][j]





            col_list.append(val)
            i+=1
        print(col_list)
        cursor.execute(Query)
        results_2=((cursor.fetchall()))

        val_list=[]
        for r in results_2:

            i=0
            # j=0
            # while(j<len(results_2)):
            #     val_list.append(f'Row {j}: ')
            while(i<len(r)):
                val_list.append(r[i])
                i+=1
                # j+=1

        print(val_list)
        print(dict(zip(col_list,val_list)))
    except Exception as e:
        print(e.args)
    finally:
        "Go"
#         print(cursor.rowcount)
#         for row in results:
#             row=list(row)
#             BANK_ID = row[0]
#             row[0]=576578
#             BRANCH = row[1]
#             TURNOVER = row[2]
#             EMPLOYEE_NO = row[3]
#             STATUS=row[4]
#             print(f'Row {c} data \n BANK_ID: {BANK_ID}\n BRANCH: '
#              f'{BRANCH}\n EMPLOYEE_NO: {EMPLOYEE_NO} \n TURNOVER: {TURNOVER} \n'
#                   f'EMPLOYEE_NO: {EMPLOYEE_NO}\n'
#                   f'STATUS: {STATUS}')
#             c += 1
#         db.commit()
#     except Exception as e:
#         print("Query didnot execute successfully",e.args)
#         db.rollback()
#     else:
#         print("Query executed successfully and Data:")
# except Exception as e:
#     print("Database could not be connected as :", e.args)
# else:
#     print("Database is connected successfully")
