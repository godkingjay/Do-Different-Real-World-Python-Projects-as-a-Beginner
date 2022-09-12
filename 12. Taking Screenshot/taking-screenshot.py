# import Python Modules
from os.path import exists
import pyscreenshot

screenshot_dir = "screenshots/"
screenshot_name = "screenshot"
screenshot_ext = ".jpg"
n = 0
screenshot = pyscreenshot.grab()

while exists(f"{screenshot_dir}{screenshot_name}{n}{screenshot_ext}"):
    n+=1

screenshot.save(f"{screenshot_dir}{screenshot_name}{n}{screenshot_ext}")
screenshot.show()