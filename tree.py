# -*- coding: utf-8 -*-

import os
import sys

args = ['.']
if len(sys.argv) > 1:
    args = sys.argv[1:]


def tree(arg, indent=""):
    path = os.path.abspath(arg)
    print os.path.basename(path)

    if not os.path.isdir(path):
        return

    current_dirs = os.listdir(arg)
    filtered_names = []

    for f in current_dirs:
        if not f.startswith('.'):
            filtered_names.append(f)

    filtered_names = sorted(filtered_names)
    for i, d in enumerate(filtered_names):
        add = "│  "
        if i == len(filtered_names) - 1:
            print indent + "└──",
            add = "   "
        else:
            print indent + "├──",

        tree(os.path.join(arg, d), indent=indent + add)


def main():
    for arg in args:
        try:
            tree(arg)
        except Exception as e:
            print e.message


if __name__ == '__main__':
    main()
