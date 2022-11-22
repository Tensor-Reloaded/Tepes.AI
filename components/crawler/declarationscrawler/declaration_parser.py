import argparse

ARGUMENTS = ["website", "--nume", "--prenume", "--institutie", "--functii", "--data_inceput", "--data_sfarsit",
             "--judet", "--localitate", "--tip_declaratie", "--count"]

def parse_args(args):
    parser = get_parser()
    return parser.parse_args(args)

def get_parser():
    parser = argparse.ArgumentParser(
        prog='CrawlerTAIP',
        description='Crawls public information regarding public figures financial status')
    for argument in ARGUMENTS:
        parser.add_argument(argument)
    return parser
