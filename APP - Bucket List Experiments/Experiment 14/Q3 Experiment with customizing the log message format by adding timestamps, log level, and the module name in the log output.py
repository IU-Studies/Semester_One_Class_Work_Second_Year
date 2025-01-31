#Experiment with customizing the log message format by adding timestamps, log level, 
#and the module name in the log output

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(module)s - %(message)s',
    filename='app.log',
    filemode='a'
)

logging.debug("This is a DEBUG message, used for detailed diagnostic information.")
logging.info("This is an INFO message, used to confirm normal operations.")
logging.warning("This is a WARNING message, used to indicate a potential problem.")
logging.error("This is an ERROR message, used to report an issue that occurred.")
logging.critical("This is a CRITICAL message, used for serious issues requiring immediate attention.")
