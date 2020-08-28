"""__config.py: Config manipulation."""
__author__ = "Muhammad Umer Farooq"
__license__ = "GPL-3"
__version__ = "1.0.0"
__maintainer__ = "Muhammad Umer Farooq & Muhammad Usman Naeem"
__email__ = "contact@muhammadumerfarooq.me"
__status__ = "Production"

import json
import os


def get_config(config, root=""):
    """
     Get config value from config file.
     Args:
         config: key the value you want to get!.
     Returns:
         mixed.
     Raises:
         None.
     """

    if os.path.exists(root+"/config.json"):
        print("true")
        file = open(root+"/config.json", "r")
        data = file.read()
        configuration = json.loads(data)
        if config in configuration:
            return configuration[config]
        else:
            return None
    else : print("false")

db_name = get_config("db_name")
print(db_name)
