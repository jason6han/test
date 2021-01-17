import os 
def run(**args):
    print('in dirlist modules')
    files=os.listdir('.')
    return str(files)