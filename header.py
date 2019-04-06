# -*- coding: utf-8 -*-
import os


def define(title):
    os.system('clear')
    message = "{}".format(title)
    line = "*******************************"
    str_header = "{}\n{}\n{}".format(line, message, line)
    print(str_header)
