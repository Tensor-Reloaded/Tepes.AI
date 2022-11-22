import unittest
from argparse import ArgumentParser

from components.crawler.declarationscrawler.constants import DECLARATII_INTEGRITATE_WEBSITE
from components.crawler.declarationscrawler.declaration_parser import get_parser, ARGUMENTS


class DeclarationParserTest(unittest.TestCase):
    parser = None

    def setUp(self) -> None:
        self.parser = get_parser()

    def test_get_parser(self):
        self.assertEqual(self.parser.__class__, ArgumentParser)

    def test_parse_args_when_no_args_error_thrown(self):
        self.assertRaises(SystemExit, self.parser.parse_args)

    def test_parse_args_when_only_website_provided(self):
        parsed = self.parser.parse_args([DECLARATII_INTEGRITATE_WEBSITE])
        self.assertIsNotNone(parsed.website)

    def test_parse_args_when_all_arguments_provided(self):
        arguments_for_parser = []
        for arg in ARGUMENTS:
            if arg.startswith("--"):
                arguments_for_parser.append(arg)
                arguments_for_parser.append("mockValue")
            else:
                arguments_for_parser.append("mockValue")
        parsed = self.parser.parse_args(arguments_for_parser)
        self.assertEqual(parsed.website, "mockValue")
        self.assertEqual(parsed.nume, "mockValue")
        self.assertEqual(parsed.prenume, "mockValue")
        self.assertEqual(parsed.institutie, "mockValue")
        self.assertEqual(parsed.functii, "mockValue")
        self.assertEqual(parsed.data_inceput, "mockValue")
        self.assertEqual(parsed.data_sfarsit, "mockValue")
        self.assertEqual(parsed.judet, "mockValue")
        self.assertEqual(parsed.localitate, "mockValue")
        self.assertEqual(parsed.tip_declaratie, "mockValue")
        self.assertEqual(parsed.count, "mockValue")
