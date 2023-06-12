from main import *
import argparse

parser = argparse.ArgumentParser(
    prog="Google Photos Matcher (Linux fork)",
    description="Linux fork of Google Photos Matcher by @anderbggo on GitHub")
parser.add_argument("path")
parser.add_argument("-s", "--suffix")

args = parser.parse_args()

mainProcess(args.path, args.suffix)
