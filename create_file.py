#!/usr/bin/env python3
'''
A simple script for creating tech lead problem files
'''
import os
from sys import argv


class CreateFile:
    '''General-purpose '''

    def CreateTechLeadProblem(self, filename: str, url: str) -> None:
        cleanFile = filename.replace(' ', '_') + '.py'
        working = os.getcwd()
        new_file_path = os.path.join(
            working,
            'Techlead_Problems/' + cleanFile
        )
        with open(new_file_path, 'w') as file:
            file.write(f'#!/usr/bin/env python3\n\'\'\'\n{url}\n\'\'\'\n')
        os.chmod(new_file_path, 0o744)


if __name__ == '__main__':
    if argv[1] == 'tech':
        arg_len = len(argv)
        if arg_len < 4:
            print('Missing arguments')
            if arg_len == 3:
                print('Missing url')
                argv.append('')
            if arg_len == 2:
                print('Missing filename')
                exit()
        CreateFile().CreateTechLeadProblem(argv[2], argv[3])
