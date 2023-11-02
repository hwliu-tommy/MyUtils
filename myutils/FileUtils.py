
import os

def create_dir(path: str, dry_run=False):
    if dry_run:
        print("Create directory, path={}".format(path))
    else:
        os.mkdir(path)

    return path