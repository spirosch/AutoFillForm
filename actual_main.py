import os
from multiprocessing import Process, current_process, Pool
import time
from flows.executor_flow_1 import driver_flow_1, dummy_driver

CORE_CAP = 4
THREAD_CAP = 12


def work_log(work_data):
    print(" Process %s waiting %s seconds" % (work_data[0], work_data[1]))
    time.sleep(int(work_data[1]))
    print(" Process %s Finished." % work_data[0])


def pool_handler(driver_flow, work):
    p = Pool(CORE_CAP)
    p.map(driver_flow, work)

def main():
    # Parse file
    #
    # number_of_files = os.listdir('.').__len__()
    # for iteration in range(1, number_of_files):
    #     pass
    # Fetch client folders
    client_folders = os.listdir('/flows/flow_1')
    driver_flow = 'driver_flow_1'
    work = ()

    for item in client_folders:
        work = work + (item,)

    pool_handler(driver_flow,work)


if __name__ == '__main__':
    main()