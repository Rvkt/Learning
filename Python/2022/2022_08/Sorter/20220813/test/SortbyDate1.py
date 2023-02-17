import pathlib
import re
from datetime import datetime


# pathlib.Path('file_path').stat().st_mtime

def main():
    # ask for path
    path = input('Enter path:\n')
      
    # check if the given path is present
    path = pathlib.Path(path).absolute()
    
    # If the given path is not present notify the user.
    if not path.is_dir():
        print('Check the path')
        return


    items = list(path.iterdir())
    item_count = len(items)
    # print(f"--> Only {item_count} files are in the given directory.")

    for item in items:
        # skip folders
        if item.is_dir() and re.fullmatch(r'\d{8}', item.name):
            print(f'    Skipping {item.name}')
            continue

        print(f'    Moving {item.name}')


        time = datetime.fromtimestamp(item.lstat().st_mtime)

        # print(time)

        dstn_path = item.parent / time.strftime('%Y%m%d').zfill(2)
        dstn_path.mkdir(exist_ok=True)
        item.rename(dstn_path / item.name)

print('Done!')

if __name__ == '__main__':
    main()