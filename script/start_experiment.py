import os
import sys
import time
from main import main_loop
from utils import *
from param import *

if __name__ == '__main__':
    path_to_logs = os.path.abspath(PATH_TO_FILTERED_LOG) + '/'
    if REMOVE_INCOMPLETE_LOGS:
        for fname in os.listdir(path_to_logs):
            flag_deletable = False
            wab_dir = path_to_logs + fname + '/w_adblocker/'
            woab_dir = path_to_logs + fname + '/wo_adblocker/'
            try:
                for f in os.listdir(wab_dir):
                    if not os.path.getsize(wab_dir + f):
                        shutil.rmtree(path_to_logs + fname)
                        with open(PATH_TO_URLFILE, "a") as urllist:
                            urllist.write(fname + '\n')
                        print '[INFO][starter] ' + fname + ' is an incomplete log, to be deleted...'
                        flag_deletable = True
                        break
            except OSError:
                print '[ERROR][starter] ' + fname + ' does not have raw log folders, skipping...'
                continue
            if flag_deletable:
                continue
            for f in os.listdir(woab_dir):
                if not os.path.getsize(woab_dir + f):
                    shutil.rmtree(path_to_logs + fname)
                    with open(PATH_TO_URLFILE, "a") as urllist:
                        urllist.write(fname + '\n')
                    print '[INFO][starter] ' + fname + ' is an incomplete log, to be deleted...'
                    flag_deletable = True
                    break
        finished_list = []
        for fname in os.listdir(path_to_logs):
            finished_list.append(fname)
        finished_set = set(finished_list)

    if BACKUP_OLD_LOG:
        try:
            os.rename(path_to_logs, path_to_logs + '_old_' + str(int(time.time() * 100)))
        except OSError:
            print '[ERROR][starter] ' + path_to_logs + ' has not been created yet'
            print '[INFO][starter] Creating a new one...'
            os.mkdir(path_to_logs)

    if DELETE_RAW_LOG:
        try:
            delete_raw_log(path_to_logs)
        except OSError:
            print '[ERROR][starter] ' + path_to_logs + ' has not been created yet, nothing to delete'

    if DOWNLOAD_LIST:
        downloaded_list = download_urllist(URL_TO_ALEXA_10K)
        downloaded_set = set(downloaded_list)
        real_set = downloaded_set - finished_set
        real_list = list(real_set)
        real_list = map(lambda lne: lne + '\n', real_list)
        with open(PATH_TO_URLFILE, 'w') as f:
            f.writelines(real_list)

    if RUN_EXP:
        main_loop()
