import fnmatch
import os
import shutil
import sys


def main():
    args = sys.argv[1:]
    if len(args) > 1:
        sys.exit(1)
    _dir = args[0] if len(args) == 1 else "."
    os.chdir(_dir)

    print(f"List {_dir}: ")
    for i in os.listdir():
        print(i)
    line = "---------------------------------------------"
    print(line)
    filtered_items = []
    while not filtered_items:
        pattern = input("Filter pattern(Glob): ")
        filtered_items = fnmatch.filter(os.listdir("."), pattern)
        if not filtered_items:
            print("Pattern matched nothing, please re-enter.")
    for i in filtered_items:
        print(i)
    print(line)
    print("Replace <A> to <B>:\n")
    str_a = input("A: ")
    str_b = input("B: ")
    for i in filtered_items:
        os.rename(i, i.replace(str_a, str_b))


if __name__ == "__main__":
    main()
