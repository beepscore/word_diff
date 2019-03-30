#!/usr/bin/env python3

import subprocess


def text_from_file(filename):
    """
    read file
    """
    with open(filename, 'r') as input_file:
        text = input_file.read()
        return text


def write_diffs(filename_a, filename_b):
    args = ['dwdiff', filename_a, filename_b]
    subprocess.run(args)


if __name__ == '__main__':

    filename_a = './data/input/a.txt'
    filename_b = './data/input/b.txt'
    write_diffs(filename_a, filename_b)


