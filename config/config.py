import os
import sys
import configparser

_path = f'{os.environ.get("HOME")}/.happy.laborer'


def auth():
    if os.path.exists(_path):
        parser = configparser.ConfigParser()
        try:
            parser.read(_path)
            username = parser.get('auth', 'username')
            password = parser.get('auth', 'password')
            return username, password
        except configparser.MissingSectionHeaderError:
            print('''
please check the config file $HOME/.happy.laborer is fit the correct format

[auth]
username=<username>
password=<password>
            ''')

            sys.exit(1)
    else:
        print(f'config file {_path} not exit, please create it and retry. \
            format:')
        print('''\
[auth]
username=<username>
password=<password>
        ''')
        sys.exit(1)


def project_location():
    if os.path.exists(_path):
        parser = configparser.ConfigParser()
        try:
            parser.read(_path)
            return parser.get('project', 'location')
        except configparser.MissingSectionHeaderError:
            print('''
please check the config file $HOME/.happy.laborer is fit the correct format

[project]
location=<location>
            ''')

            sys.exit(1)
    else:
        print(f'config file {_path} not exit, please create it and retry. \
            format:')
        print('''\
[project]
location=<location>
        ''')
        sys.exit(1)
