# Utils that enable functionality

import platform
import os

class file_util:
    def __init__():
        pass
    def file_path(self, selector):
        if platform.system() == "Linux":
            if selector == "home":
                return os.path.expanduser("~")
            elif selector == "stuhome":
                path = os.path.join(os.path.expanduser(~), "mount/stuhome")

        elif platform.system() == "Windows":
            if selector == "home":
                return os.path.expanduser("~")
            elif selector == "stuhome":
                print("Add stuhome")
        else:
            if selector == "home":
                return os.path.expanduser("~")