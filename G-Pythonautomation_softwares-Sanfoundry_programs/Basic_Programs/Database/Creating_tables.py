from Basic_Programs.Database import database_connectivity
database_connectivity.database_con()
Query='''CREATE TABLE HDFC(BANK_ID bigint PRIMARY KEY ,BRANCH varchar(50),
TURNOVER bigint,EMPLOYEE_NO bigint,
STATUS char)'''
c = 1
try:
    with database_connectivity.database_con() as cursor:

        cursor.execute("DROP TABLE IF EXISTS HDFC")
        cursor.execute(Query)
        cursor.execute("Select * FROM HDFC")
    #db.commit()








    # cursor.execute("SELECT VERSION()")
    # store the result
    # results = database_connectivity.database_con().fetchall()
    # print(database_connectivity.database_con().rowcount)
    # for row in results:
    #     BusinessID = row[0]
    #     Client_name = row[1]
    #     DEPT = row[2]
    #     Project = row[3]
    #     print(f'Row {c} data \n BusinessID: {BusinessID}\n Client_name: '
    #           f'{Client_name}\n DEPT: {DEPT} \n Project: { Project}')
    #     c += 1

except Exception as e:
    print("Query didnot execute",e.args)
    # db.rollback