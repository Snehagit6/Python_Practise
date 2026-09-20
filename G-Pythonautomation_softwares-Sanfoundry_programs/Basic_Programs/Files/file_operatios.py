# Python File Modes
# Mode	Description
# 'r'	Open a file for reading. (default)
# 'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
# 'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
# 'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
# 't'	Open in text mode. (default)
# 'b'	Open in binary mode.
# '+'	Open a file for updating (reading and writing)

import os

#'x' mode
def x_mode():
    try:
        with open("./data.json",'x') as fo:
            print("File opened")
    except FileExistsError as fe:
        print(fe.args)
# if os.path.exists("./text.txt"):
#     os.remove("./text.txt")
#
# with open("./Sanfoundry_file.txt",'w+') as fo:
#     print((fo.seek(0,2)))
#     print((fo.tell()))

x_mode()