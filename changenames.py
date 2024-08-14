import os, logging, pprint


logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s -  %(levelname)s -   %(message)s')
logging.disable(logging.DEBUG)

def clean_file_names(folderPath):
    logging.info(folderPath)
    os.chdir(folderPath)
    logging.info(os.curdir)
    logging.info(pprint.pformat(os.listdir(os.curdir)))
    names = {}

    logging.info(os.curdir)

    logging.info(len(os.listdir(os.curdir)))

    i = 0
    for file in os.listdir(os.curdir):
        os.rename(file, 'Photo ' + str(i) + ' - ' + str(file).split('---cut---')[1])
        i += 1

clean_file_names(f'photo test copy')