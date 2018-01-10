import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-nat', nargs='+', help='please input target CIDR. e')
    args = parser.parse_args()

    parser.print_help()

