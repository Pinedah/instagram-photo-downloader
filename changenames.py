import os, logging, pprint


logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s -  %(levelname)s -   %(message)s')
logging.disable(logging.DEBUG)

def clean_file_names(folderPath):
    logging.info(folderPath)
    os.chdir(folderPath)
    logging.info(os.curdir)
    logging.info(pprint.pformat(os.listdir(os.curdir)))
    for file in os.listdir(os.curdir):
        os.rename(file, str(file).split('---cut---')[1])
        logging.info(file)

clean_file_names(f'photos-mewton_the_cat')