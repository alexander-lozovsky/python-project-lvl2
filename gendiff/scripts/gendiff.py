#! usr/bin/env python3
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('first_file')
parser.add_argument('second_file')


def main():
    parser.parse_args()


if __name__ == '__main__':
    main()
