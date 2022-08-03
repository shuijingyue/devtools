from shell import pwd
import subprocess


def ls(dir: str = ""):
    if dir == '':
        dir = pwd()
    return cmd(['ls'])


def cmd(cmd: list):
    output = subprocess.run(cmd, capture_output=True)
    if output.returncode == 0:
        return output.stdout.decode('utf-8')
    else:
        return None
