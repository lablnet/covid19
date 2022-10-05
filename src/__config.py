"""__config.py: Config manipulation."""
__author__ = "Muhammad Umer Farooq"
__license__ = "GPL-3"
__version__ = "1.0.0"
__maintainer__ = "Muhammad Umer Farooq & Muhammad Usman Naeem"
__email__ = "contact@muhammadumerfarooq.me"
__status__ = "Production"

import json
import os

_cache = {}


def get_config(config, root="", filename="config.json"):
    """
     Get config value from config file.
     Args:
         config: Key for the config you want to get!.
         root: Project root folder path.
         filename: Name of the config file. Defaults to config.json
     Returns:
         The config value loaded from config file or None
     """

    global _cache

    if not _cache:
        if os.path.isfile(root + "/" + filename):
            with open(root + "/" + filename) as file:
                data = file.read()
                _cache = json.loads(data)

    try:
        return _cache[config]
    except KeyError:
        return None
