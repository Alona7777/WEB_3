import argparse
from pathlib import Path
from shutil import copyfile
import logging
import time

"""
--sourse -s trash  #python3 sorter.py -s garbage
--output -o dist   #python3 sorter.py -s garbage -o name folder
"""

parser = argparse.ArgumentParser(description='App for sorting folder')
parser.add_argument('-s', '--source', required=True)
parser.add_argument('-o', '--output', default='dist')
args = vars(parser.parse_args())
source = args.get('source')
output = args.get('output')

folders = []


def grabs_folder(path: Path):
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            grabs_folder(el)

def copy_file(path: Path):
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix.upper()
            new_path = output_folder / ext
            try:
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(el, new_path / el.name)
            except OSError as e:
                logging.error(e)



if __name__ == '__main__':
    start = time.time()
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    base_folder = Path(source)
    output_folder = Path(output)

    folders.append(base_folder)
    grabs_folder(base_folder)

    for folder in folders:
        copy_file(folder)
    end = time.time() - start
    print(f'Час виконання без потоків {end}')
    

