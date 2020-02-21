#!/usr/bin/env python

"""Module docstring: One line description of what your program does."""
"""splits a dict into two list and checks for balanced brackets , returning yes or no and the place index of where the error occurs"""
__author__ = "Mauricio with multiple online searches and help from my wife as well shes in Q2"

import sys

def main(textfile):
    file = open(textfile, "r").readlines()
    output_txt = open (textfile.split(".")[0] + "_output.txt","w")
    for line in file:
            outcome = is_nested(line)
            output_txt.write(outcome + "\n")
    output_txt.close()
    
def is_nested(line):
    line = split_list(line)
    dict = {"(": "p",")": "p","{": "c","}": "c","[": "sq","]": "sq","<": "g",">": "l","(*": "s","*)": "s"}
    brackets = []
    for i, check in enumerate(line):
        if check in ["(","[","{","(*","<"]:
            brackets.append(dict[check])
        elif check in [")","]","}","*)",">"]:
            if dict[check] == brackets[-1]:
                brackets.pop()
            else:
                return "NO" + str(i + 1)
    if len(brackets) == 0:
        return "YES"
    else:
        return "NO " + str(len(line) + 1)

def split_list(line):
    brackets = list(line)[:-1]
    i = 0
    second_brackets = []
    length = len(brackets)
    while i < length:
        if brackets[i] == "(" and i < length - 1 and brackets[i+1] == "*":
            second_brackets.append("(*")
            i += 1
        elif brackets[i] == "*" and i < length - 1 and brackets[i+1] == ")":
            second_brackets.append("*)")
            i += 1
        else:
            second_brackets.append(brackets[i])
        i += 1
    return second_brackets

if __name__ == '__main__':
    textfile = sys.argv[1]
    main(textfile)