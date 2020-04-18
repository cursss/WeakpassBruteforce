import sys
import importlib
from optparse import OptionParser
from lib.helper import file_to_list

if __name__ == '__main__':

    # check version of python
    if sys.version_info < (3, 0):
        sys.stdout.write("Sorry, this tool requires Python 3.x\n")
        sys.exit(1)

    # arguments parser
    parser = OptionParser(usage = "Usage : python %prog -s service -a address [-p port] [-u userlist.txt] [-p password.txt] [-t thread] [-d delay]")
    parser.add_option("-s", "--service", action = "store", type = "str", dest = "service", default = False, help = "Service to bruteforce")
    parser.add_option("-a", "--address", action = "store", type = "str", dest = "address", default = False, help = "Address where the service is running")
    parser.add_option("-p", "--port", action = "store", type = "int", dest = "port", default = 0, help = "Port where the service is running")
    parser.add_option("-U", "--userlist", action = "store", type = "str", dest = "userlist", default = "userlist.txt", help = "Username list")
    parser.add_option("-P", "--passlist", action = "store", type = "str", dest = "passlist", default = "passlist.txt", help = "Password list")
    parser.add_option("-t", "--thread", action = "store", type = "int", dest = "thread", default = 10, help = "Maximum number of threads used, default value is 10")
    parser.add_option("-d", "--delay", action = "store", type = "float", dest = "delay", default = 0, help = "Time interval between each execution, default value is 0 second")

    # parameter assignment
    options, values = parser.parse_args()
    if options.service == False:
        exit('[!] Service parameter cannot be empty !')
    if options.address == False:
        exit('[!] Address parameter cannot be empty !')
    service, address, port, userlist, passlist, thread, delay = options.service.lower(), options.address, options.port, options.userlist, options.passlist, options.thread, options.delay
    try:
        userlist = file_to_list(userlist)
        passlist = file_to_list(passlist)
    except FileNotFoundError:
        exit('[!] Dictionary file not found !')

    # dynamic import module
    try:
        module = importlib.import_module('lib.'+service)
    except ModuleNotFoundError:
        exit('[!] Unsupported for bruteforce this service "' + service + '" !')
    obj = module.bruteforce_class(userlist, passlist, address, port, thread, delay)
    obj.bruteforce_func()