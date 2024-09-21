import sys 

class ResolveArgs:
    @staticmethod
    def handler(args):
        if(args.only_file and args.type == 'csv'):
            print("Error: No puede seleccionar un solo archivo para el tipo csv")
            sys.exit(1) 
        return args