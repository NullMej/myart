import glob
import os

input_fileName = open("csvファイル（ファイル名を羅列したファイル）のあるディレクトリ")
input_lines = input_fileName.readlines()

for read in input_lines:
    read = read.replace('\n','')
    file_name = ("ファイルのあるディレクトリ" + read)
    
    if os.path.exists(file_name):
    
        open_file = open(file_name)

        print(os.path.basename(file_name))
        lines = open_file.readlines()

        if len(lines) > 5:
            print(lines[1])
            print(lines[2])
            print(lines[3])
            print(lines[4])
            print(lines[5])
        else:
            print("あまりにも短いファイルです")

        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

    else:
        print(os.path.basename(file_name))
        print("存在しないファイルです")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")