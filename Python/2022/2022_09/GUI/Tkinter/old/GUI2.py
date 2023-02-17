from tkinter import Tk, filedialog
import os
from datetime import date, datetime

root = Tk()  # pointing root to Tk() to use it as Tk() in program.
# root.withdraw()  # Hides small tkinter window.
root.attributes('-topmost', True)  # Opened windows will be active. above all windows despite selection.
open_file = filedialog.askdirectory()  # Returns opened path as str

# print(os.listdir(open_file))

# now = datetime.now()
# dt_str = now.strftime('%Y%m%d%H%M')

# os.makedirs(path, exist_ok=True)

# for d in open_file:
#     try:
#         os.makedirs(dt_str)
#     except FileExistsError:
#         pass




