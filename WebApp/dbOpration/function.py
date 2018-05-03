import MySQLdb
import re


def execute_opration(quert):
    db = MySQLdb.connect("localhost", "root", "", "ipldata")
    # print("get curser...")
    curser = db.cursor()
    try:
        # print("query to execute: "+quert)
        curser.execute(quert)
        # print("executin is done")
        db.commit()
    except:
        # print("execption :"+ db.error())
        db.rollback()
        return  0
    db.close()
    return 1

def read_file(path):
    with open(path,"r") as f:
        # print("file is reading")
        list = []
        for line in f:
            list.append(line)
    return list


def check_data(data):
    # print("CHEKING EXISTANCE OF DATA")
    query = "SELECT * FROM ipl_data WHERE team='"+ data[0] +"' AND date='"+ data[1] +"' AND name='"+ data[3] +"' AND type='"+data[2]+"'"
    status = execute_opration(query)
    return status

def insert_record(list):
    # print("INSERTING DATA")
    # print(list)
    if bool(re.search("B", list[2])):
        query = "INSERT INTO ipl_data (team, date, type, name, cmt, runs, balls, sr, fours, sixs) VALUES ('"+list[0]+"','"+list[1]+"' ,'"+list[2]+"' ,'"+list[3]+"' ,'"+list[4]+"' ,"+ str(list[5]) + "," + str(list[6]) + "," + str(list[7]) + "," + str(list[8]) + " ,"+str(list[9])+" )"
        execute_opration(query)
    else:
        query = "INSERT INTO ipl_data (team, date, type, name,b_overs, b_runs, b_wickets, b_econ, b_dots) VALUES ('" + list[0] + "', '" + list[1] + "' ,'" + list[2] + "' ,'" + list[3] + "' ," + str(list[4]) + "," + str(list[5]) + "," + str(list[6]) + "," + str(list[7]) + "," + str(list[8]) + ")"
        execute_opration(query)



