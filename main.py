import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Command line argument parser')

# Add the arguments
parser.add_argument('command', choices=['abstraction', 'runcfr', 'gamer'], help='The command to execute')
parser.add_argument('file_path', help='Path to the big file')
parser.add_argument('--o', help='Optional argument')

# Parse the command line arguments
args = parser.parse_args()

# Process the parsed arguments
if args.command == 'abstraction':
    print('Executing abstraction command')
    print('Abstraction file path:', args.file_path)
    if args.optional:
        print('Optional argument:', args.optional)
elif args.command == 'runcfr':
    print('Executing runcfr command')
    print('File path:', args.file_path)
    if args.optional:
        print('Optional argument:', args.optional)
elif args.command == 'gamer':
    print('Executing gamer command')
    print('File path:', args.file_path)
else:
    print('Invalid command')
