from WebApp.dbOpration import function as fc
import csv
import re

list = fc.read_file("batmans.csv")
# print(str(len(list)))
list += fc.read_file("bowlers.csv")
print("data lenght :"+str(len(list)))
count , skiperd= 0 , 0
for data in list:
    lst = data.split(",")
    if len(lst)<4:
        continue
    # print("lenght of list :" + str(len(lst)))
    # print("processing data :" + str(lst))
    if bool(re.search("B",lst[2])):
        # print("batsman.")
        lst[2] = "B"
        date = lst[1]
        date = date.split(" ")
        date = date[1]
        lst[1] = date
        if len(lst)<10:
            for i in range(len(lst)-1, 10):
                if i<=4:
                    lst.append("")
                else:
                    lst.append(0)
    else:
        # print("bowler")
        lst[2] = "W"
        if len(lst)<9:
            for i in range(len(lst)-1, 8):
                if i<=3:
                    lst.append("")
                else:
                    lst.append(0)
    del lst[3]
    # print(lst)
    # print("length of list :" + str(len(lst)))
    # print("inserting record...")
    chk = lst[:4]
    if fc.check_data(chk) == 1:
        # print("within opration or insertion")
        fc.insert_record(lst)
    else:
        print(lst)
    # print("inserting done of data :"+ str(count))
    count += 1




