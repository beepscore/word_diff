#!/usr/bin/env python3

from subprocess import PIPE, run


def text_from_file(filename):
    """
    read file
    """
    with open(filename, 'r') as input_file:
        text = input_file.read()
        return text


def text_to_file(text, filename):
    """
    write file
    """
    with open(filename, 'w') as output_file:
        output_file.write(text)
        return text


def write_diffs(in_filename_a, in_filename_b, out_filename):
    # https://stackoverflow.com/questions/1996518/retrieving-the-output-of-subprocess-call
    command = ['dwdiff', in_filename_a, in_filename_b]
    completed_process = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    text_to_file(completed_process.stdout, out_filename)


if __name__ == '__main__':

    in_a = './data/input/a.txt'
    in_b = './data/input/b.txt'
    out_ab = './data/output/ab.txt'
    out_ba = './data/output/ba.txt'
    write_diffs(in_a, in_b, out_ab)
    write_diffs(in_b, in_a, out_ba)


