import os
from config import config_from_ini, config_from_dict

from shared_data import SharedData

# A class that was going to be used, but didn't make the cut.
class ConfigUtils():
    
    # Init the base config object and its default values, along with shared_data, etc...
    def __init__(self) -> None:
        self._data = SharedData()
        self._cwd = self._data.current_cwd
        self._sep = self._data.os_sep
        self.default_config = {
            "GAME.window_width": 1080,
            "GAME.window_height": 720,
            "GAME.game_fps": 60,
            "GAME.enable_experimental_features": False,
        }
        
    # Actually create the config object, file, and so forth...
    def init_config(self, file_name: str = "config.ini", file_dir: str = "_config"):
        if not os.path.exists(f"{self._cwd}{self._sep}{file_dir}{self._sep}{file_name}"):
            with open(f"{self._cwd}{self._sep}{file_dir}{self._sep}{file_name}", "w") as config_file:
                cfg = config_from_dict({k: str(v) for k, v in self.default_config.items()})
                config_file.write(self.default_config)