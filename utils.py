from pathlib import Path
import os
import re


def increment_path(name="", base_path="./logs", make_directory=True, ignore="partial"):
    # Check for existence
    Path(base_path).mkdir(parents=True, exist_ok=True)
    n, npath = get_max_file(base_path, ignore=ignore)

    # Create
    logdir = Path(os.path.join(base_path, "{:02d}_{}".format(n + 1, name)))
    if make_directory:
        Path(logdir).mkdir(parents=True, exist_ok=True)
    return logdir

def get_max_file(path, ignore=None):
    """ Gets the file with the highest (first) number in the string, ignoring the "ignore" string
    Args:
        path (str): Folder to search
    Returns:

    """
    if ignore:
        filtered = [p for p in os.listdir(path) if not re.search(ignore, p)]
    else:
        filtered = os.listdir(path)
    numbers = [(int(re.search("^[0-9]+", p)[0]), p) for p in filtered if re.search("^[0-9]+", p)]
    n, npath = max(numbers) if numbers else (0, "")
    # print("Last File Version: {}".format(npath))
    return n, os.path.join(path, npath)