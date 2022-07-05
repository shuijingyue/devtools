from config import project_location
from shell import *


def get_commits(branch, author="", after=""):
    location = pwd()
    cd(project_location())
    args = ["git", "log", f"{branch}", "--oneline", "--format='%H|||%s|||%an'"]
    if author != '':
        args.append(f'--author={author}')
    if after != '':
        args.append(f'--after={after}')
    result = cmd(args)
    cd(location)
    return result
