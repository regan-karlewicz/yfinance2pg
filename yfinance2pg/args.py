import sys


def get(arg):
    try:
        idx = sys.argv.index('--' + arg)
        return sys.argv[idx + 1]
    except Exception:
        return None


def get_list(arg):
    try:
        idx = sys.argv.index('--' + arg)
        return sys.argv[idx + 1].split(',')
    except Exception:
        return []


def exists(arg):
    try:
        sys.argv.index('--' + arg)
        return True
    except Exception:
        return False
