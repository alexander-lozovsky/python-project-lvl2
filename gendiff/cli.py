import argparse



def run():
    parser = argparse.ArgumentParser()

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output', metavar='FORMAT')

    parser.parse_args()
