import requests
import os
from os import sep

from utils.exceptions import InternalErrorException

class DataDownloader():
    
    # Get the game's version from a URL, named 'url'
    def get_version_from_url(self, url):
        request = requests.get(url)
        
        lines = request.text.split("\n")
        
        return lines[0]
    
    # Download a file to the game directory. This was intended to be called, but was never implemented. 
    def download_file(self, url, out_dir: str = os.getcwd(), file_name: str = None, large_file: bool = False):
        request = requests.get(url, stream=large_file)
        
        if large_file:
            with open(f"{out_dir}{sep}{file_name}", "wb") as file_large:
                for chunk in request.iter_content(chunk_size=1024):
                    if chunk:
                        file_large.write(chunk)
        elif file_name != None:
            open(f"{out_dir}{sep}{file_name}", "wb").write(request.content)
        else:
            raise InternalErrorException("Please set the output filename when trying to download a file!")