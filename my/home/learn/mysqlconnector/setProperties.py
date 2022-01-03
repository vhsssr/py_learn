import configparser

parser = configparser.ConfigParser()


class Properties:
    @staticmethod
    def get_parser():
        return parser

    @staticmethod
    def init_properties():
        parser.read("properties.properties")
