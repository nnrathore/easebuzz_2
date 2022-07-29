
import logging


def customLogger():
    # Gets the name of the class / method from where this method is called

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG,filename="text.log")
    logger = logging.getLogger()
    return logger


    # By default, log all messages
    # logger.setLevel(logging.DEBUG)
    #
    # fileHandler = logging.FileHandler("automation.log", mode='a')
    # fileHandler.setLevel(logging.DEBUG)
    #
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
    #                 datefmt='%m/%d/%Y %I:%M:%S %p')
    # fileHandler.setFormatter(formatter)
    # logger.addHandler(fileHandler)




