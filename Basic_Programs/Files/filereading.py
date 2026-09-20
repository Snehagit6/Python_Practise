from functools import reduce
with open("G:\\Pythonautomation_softwares\\Sanfoundry_programs\\Basic_Programs\\File.txt",'r') as fo:

# l_rec=(f.read().split('\n'))
    #Using readlines
    # print([i.split(' ') for i in([i.strip('\n') for i in fo.readlines()])])

    l1=[each.split(' ') for each in (fo.read().split('\n'))]
    l2=[dict(zip(l1[0],each
                 ))for each in l1[1:]]
    l3=[d['Name'] for d in l2  if d['Marks']==reduce(lambda x,y:x if (x>y) else y ,[d['Marks']for d in l2])]
    print("{Student} is having highest marks:{Marks}".format(Student=''.join(l3),Marks=reduce(lambda x,y:x if (x>y) else y ,[d['Marks']for d in l2])))
    fo.close()

max_m=lambda x,y:x if x>y else y
l1=[{"marks":1},{"marks":9,9:"age"},{"marks":14}]
# from functools import reduce
z=reduce(lambda x,y:x if (x>y) else y ,[d["marks"] for d in l1])



