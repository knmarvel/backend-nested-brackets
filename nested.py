#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This program checks a text filefor invalid brackets.
If an invalid bracket exists, the program returns "Yes"
+ the index of the invalid bracket. If not, the program
returns "No".
"""
import sys


if sys.version_info[0] < 3:
    raise Exception("Need Python 3")


__author__ = "github.com/knmarvel"


def is_nested(line):
    index = 0
    brac_types = {
        "parasts": ["(*", "*)"],
        "parens": ["(", ")"],
        "squares": ["[", "]"],
        "curlies": ["{", "}"],
        "alligators": ["<",">"]
    }
    answer = "YES"
    bracs_used = []
    last_opened_index = 0
    while line:
        if line[:2] == "(*" or line[:2] == "*)":
            token = line[:2]
        else:
            token = line[0]
        for brac in brac_types:
            if token == brac_types[brac][0]:
                bracs_used.append(token)
                last_opened_index = index
            if token == brac_types[brac][1]:
                if bracs_used[-1] != brac_types[brac][0]:
                    answer = "NO " + str(index + 1)
                    token = line
                else:
                    bracs_used.pop()
        line = line[len(token):]
        index += 1
    if len(bracs_used) > 0:
        answer = "NO " + str(index)
    return (answer)


def main(args):
    line_count = 0
    answer = ""
    with open("input.txt", "r") as f:
        for line in f:
            answer += is_nested(line) + "\n"
            line_count += 1
    with open("output.txt", "w") as f:
        f.write(answer)
    with open("output.txt", "r") as f:
        print(f.read())


if __name__ == '__main__':
    main(sys.argv[1:])
