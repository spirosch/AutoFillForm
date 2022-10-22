# TODO Multithreading for IO
# TODO Multiprocessing for the actual upload
from multiprocessing import Process, current_process
import os
PROCESS_CAP = 10

# -- 

# if __name__ == "__main__":
#     # Parse file
#     #
#     number_of_files = os.listdir('.').__len__()
#     for  iteration in range(1,number_of_files):
#         pass
#
#     # both threads completely executed
#     print("Done!")
#
#     # Parse file (TODO can we do a universal file?)
#     # Create python objects
#     # Upload
