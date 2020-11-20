# Logging

import logging

# This is the logging function in Python
# filename=' ' allows logging to be shown as a txt file
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='(asctime)s - %(levelname)s - %(message)s')

# To disable all log functions

## logging.disable(logging.CRITICAL) # disable all log levels critical and under

# Log Levels (from lowest to highest):
# .debug : low importance
# .info : more important 
# .warning : something could go wrong
# .error : means something here has gone wrong
# .critical :  would cause program to fail

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.critical('i is %s, total is %s' % (i, total))

    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))

# With logging we see that we started at 0, so everything
# was multiplied by 0

