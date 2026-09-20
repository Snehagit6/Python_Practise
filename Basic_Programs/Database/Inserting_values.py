from Basic_Programs.Database import database_connectivity

Query='''INSERT INTO data.HDFC(BANK_ID,BRANCH,
TURNOVER,EMPLOYEE_NO,
STATUS)VALUES(78988,'BANGALORE',89000,70000,'A')'''
c = 1
try:
    with database_connectivity.database_con() as cursor:
        cursor.execute(Query)
        cursor.execute("Select * FROM HDFC")
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
    
''' Inserting from list of tuples without using loop
    items = [(101, 'Nik D300', 'Nik D300', 'DSLR Camera', 3),
             (102, 'Can 1300', 'Can 1300', 'DSLR Camera', 5),
             (103, 'gPhone 13S', 'gPhone 13S', 'Mobile', 10),
             (104, 'Mic canvas', 'Mic canvas', 'Tab', 5),
             (105, 'SnDisk 10T', 'SnDisk 10T', 'Hard Drive', 1)
             ]
  
    try:
        cursor.executemany("Insert into ITEMS values (?,?,?,?,?)", items)'''
        