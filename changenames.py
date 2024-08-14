import os, logging, pprint


logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s -  %(levelname)s -   %(message)s')
logging.disable(logging.DEBUG)

def clean_file_names(folderPath):
    logging.info(folderPath)
    os.chdir(folderPath)
    logging.info(os.curdir)
    logging.info(pprint.pformat(os.listdir(os.curdir)))
    i = 0
    names = {}

    logging.info(os.curdir)

    num = 1
    for file in os.listdir(os.curdir):
        name, extension = os.path.splitext(file)
        original_name = name
        os.rename(file, original_name + str(num) + extension)
        num += 1

    logging.info(len(os.listdir(os.curdir)))

    for file in os.listdir(os.curdir):
        os.rename(file, str(file).split('---cut---')[1])


    """for file in os.listdir(os.curdir):
        # Descomponer el nombre del archivo y la extensión
        name, extension = os.path.splitext(file)
        original_name = name
        logging.info(original_name)
    
        counter = 1
        while os.path.exists(file):
        # Agregar el número secuencial al nombre del archivo
            name = f"{original_name} ({counter})"
            logging.info(name)
            file = name + extension
            os.rename(original_name, str(file).split('---cut---')[1])
            
            counter += 1"""
"""
    for file in os.listdir(os.curdir):
        #if file in os.listdir(os.curdir):
        #    os.rename(file, str(file).split('---cut---')[1] + '('+str(i)+')')
        #    i += 1
        #else:
        os.rename(file, str(file).split('---cut---')[1])
        #    i = 0

        logging.info(file)
"""

clean_file_names(f'photos-samueln.ortigoza')