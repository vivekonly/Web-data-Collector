import csv


def batmat_data(list):
    print("storin batman data")
    with open("batmans.csv", "a") as bat:
        writer = csv.writer(bat, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(list)
        bat.close()


def bowler_data(datas):
    print("storin batman data")
    with open("bowlers.csv", "a") as bat:
        writer = csv.writer(bat, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(datas)
        bat.close()