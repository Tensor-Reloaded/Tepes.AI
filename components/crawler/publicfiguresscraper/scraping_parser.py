import argparse

ARGUMENTS = ["website"]


def get_parser():
    parser = argparse.ArgumentParser(
        prog='CrawlerTAIP',
        description='Crawls public information regarding public figures financial status')
    for argument in ARGUMENTS:
        parser.add_argument(argument)
    return parser
