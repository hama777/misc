#!/usr/bin/python
# -*- coding: utf-8 -*-
#  同一ファイルをチェックする

import glob
import re
import os
from collections import defaultdict

# 24/11/01 v0.03 シリアル番号によるチェックを入れた
version = "0.03"

appdir = os.path.dirname(os.path.abspath(__file__))
dirlist = appdir + "./dirlist.txt"
file_info = {}

def main_proc():
    global file_info
    read_dirlist()
    create_file_info()
    same_size_file_check()
    same_seeial_file_check()

def create_file_info() :
    for d in dir_list :
        earch_dir(d)

def earch_dir(d) :
    dir_path = d

    datafile_list = [
        f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))
    ]
    for fname in datafile_list :
        file_path = dir_path + "/" + fname
        size = os.path.getsize(file_path)
        #print(f'name = {fname} / {size}')
        file_info[file_path] = size

    #print(file_info)

def same_size_file_check() :
    size_groups = defaultdict(list)
    for file, size in file_info.items():
        size_groups[size].append(file)

    for size, files in size_groups.items():
        if len(files) > 1:
            print(f"サイズ {size} のファイル:")
            for file in files:
                print(f"- {file}")

def same_seeial_file_check() :
    serial_groups = defaultdict(list)
    for filename  in file_info.keys():
        ret = serial_num_check(filename)
        if ret != None :
            serial_groups[ret].append(filename)

    for serial, files in serial_groups.items():
        if len(files) > 1:
            print(f"シリアル {serial} のファイル:")
            for file in files:
                print(f"- {file}")


def serial_num_check(s) :
    # 正規表現パターンで5個以上の連続する半角数字をマッチ
    match = re.search(r'\d{5,}', s)
    # マッチが見つかった場合はその部分を返す
    return match.group() if match else None


def read_dirlist() :
    global dir_list 

    dir_list = []
    with open(dirlist, "r", encoding="utf-8") as f:
        for line in f:
            dir_list.append(line.rstrip("\n"))

# ----------------------------------------------------------
main_proc()

