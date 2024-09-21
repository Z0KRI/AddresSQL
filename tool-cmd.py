import argparse
from src.core.const import *
from src.core.utils.revolve_args import *
from src.core.core import Core

class ToolCMD:
    name = 'address-sql'
    description = """Herramienta para automatizar el
    proceso de migraciones de los estados, ciudades y códigos postales"""

    def setArgs(self, parser: argparse.ArgumentParser):
        parser.add_argument('-t', '--type', type=str, choices=['csv', 'sql'], default='sql', help=TYPE_HELP)
        parser.add_argument('-of', '--only-file', help=FILE_HELP, action='store_true')
        parser.add_argument('-p', '--path', help=PATH_HELP, default=r'src\files\csv')
        parser.add_argument('-o', '--output', help=OUT_PUT_HELP, default=r'src\exports')
        parser.add_argument('-e', '--engine', help=ENGINE, type=str, choices=['mysql', 'postgres'], default='postgres')
        self.args = self.parser.parse_args()

    def __init__(self):
        self.parser = argparse.ArgumentParser(prog=self.name, description=self.description)
        self.setArgs(self.parser)
        self.args = ResolveArgs.handler(self.args)
        Core(self.args)

if __name__ == "__main__":
    tool = ToolCMD()
