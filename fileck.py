#!/usr/bin/python
# -*- coding: utf-8 -*-
#  同一ファイルをチェックする

import glob
import re
import os
from collections import defaultdict

# 24/10/29 v0.02 複数ディレクトリに対応
version = "0.02"

appdir = os.path.dirname(os.path.abspath(__file__))
dirlist = appdir + "./dirlist.txt"
file_info = {}

def main_proc():
    global file_info
    read_dirlist()
    create_file_info()
    same_size_file_check()

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

def read_dirlist() :
    global dir_list 

    dir_list = []
    with open(dirlist, "r", encoding="utf-8") as f:
        for line in f:
            dir_list.append(line.rstrip("\n"))

# ----------------------------------------------------------
main_proc()

