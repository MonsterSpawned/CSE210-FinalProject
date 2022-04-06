from os import sep, linesep, pathsep, curdir
import os

# Various filesystem utilities...
class FSUtils():
    
    # Get the OS directory name seperator:
    def get_os_sep(self):
        return sep
    
    # Get the OS line seperator:
    def get_os_linesep(self):
        return linesep
    
    # Get the OS pathsep:
    def get_os_pathsep(self):
        return pathsep
    
    # Get the current directory:
    def get_curdir(self):
        return curdir
    
    # Get the current working directory:
    def get_cwd(self):
        return os.getcwd()