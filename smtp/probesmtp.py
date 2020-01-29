#!/usr/bin/python
#
# Probe SMTP for known user accounts
#
import argparse
import socket


def main():
    parser = argparse.ArgumentParser(
        description='Verify usernames against smtp server')
    parser.add_argument('smtp', help='smtp server name')
    parser.add_argument('usernames', help='usernames file')

    args = parser.parse_args()

    with open(args.usernames, 'r') as uf:
        usernames = [u.rstrip() for u in uf]

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        try:
            print('Probing {}'.format(args.smtp))
            s.connect((args.smtp, 25))

            for username in usernames:
                s.send(f'VRFY {username} \r\n'.encode())
                print(s.recv(1024))

        except ConnectionRefusedError as e:
            print('ERROR {}: {}'.format(args.smtp, str(e)))


if __name__ == "__main__":
    main()
