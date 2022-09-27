import csv
from csv import DictReader


def readCsv():
    # open file in read mode
    with open(f'../Desktop/data.csv', 'r') as read_obj:
        # pass the file object to DictReader() to get the DictReader object
        for data in csv.DictReader(read_obj):
            # print(data)
            return data


if __name__ == '__main__':
    readCsv()
