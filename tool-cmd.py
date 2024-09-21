import argparse
from src.core.const import *

class ToolCMD:
    description = 'Descripción de la herramienta'

    def setArgs(self, parser: argparse.ArgumentParser):
        parser.add_argument('--type', type=str, choices=['csv', 'sql'], help=TYPE_HELP)
        self.args = self.parser.parse_args()

    def __init__(self):
        self.parser = argparse.ArgumentParser(description=self.description)
        self.setArgs(self.parser)
        print(self.args)

if __name__ == "__main__":
    tool = ToolCMD()
