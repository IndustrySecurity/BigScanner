import argparse
from PassiveAsset.Scanner import Scanner
from PassiveAsset.snmpScanner import snmpScanner

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-nat', help='please input target CIDR. for example 192.168.1.0/24')
    args = parser.parse_args()

    scanner = snmpScanner()
    scanner.execute()
    scanner.score()

    parser.print_help()

