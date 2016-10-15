#!/usr/bin/python

import sys

def parse(fd):
    members = [
        'cheersgao',
        'chriskzhou',
        'droidfang',
        'hexleowang',
        'huarongcai',
        'jupiterwang',
        'kanedong',
        'leontli',
        'luciolong',
        'singerli',
        'skindhu',
        'wecityyan',
        'yilerwang',
    ]
    
    record = {}
    print_table_header()
    for line in fd:
        if len(line) > 1:
            key = ""
            for name in members:
                if line.startswith(name):
                    if len(record) > 0:
                        printline(record)
                        record.clear()

                    # Create new column
                    key = line.split()[0]
                    record[key] = []
                    break

            keys = list(record.keys())
            if len(keys) == 0 or len(key) > 0:
                continue
            else:
                record[keys[0]].append(line)
    # Print last line
    printline(record)

def printline(record):
    keys = list(record.keys())
    if (len(keys) > 0):
        name = keys[0]
        works = record[name]
        print("| %s |" % name, end="")
        num = len(works)
        for index in range(num):
            line = works[index]
            if index == num - 1:
                print("%s" % line.replace("\n", "|"))
            else:
                print("%s" % line.replace("\n", "<br/>"), end="")

def print_table_header():
    print("| 姓名 | 工作小结 |")
    print("| :-: | :- |")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage:")
        print("%s recorder_file_path" % sys.argv[0])
    else:
        fd = open(sys.argv[1])
        parse(fd)
