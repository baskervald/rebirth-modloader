from glob import glob
from shutil import rmtree
from os import remove

from crosscompat import RESPATH

def clean():
    resources = RESPATH.replace('\\','/')
    for directory in glob(resources+'*'+'/'):
        print('Removing: '+directory)
        rmtree(directory)
    for xmlfile in glob(resources+'*.xml'):
        print('Removing: '+xmlfile)
        remove(xmlfile)