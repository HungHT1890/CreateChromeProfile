from os import path
from time import sleep
from undetected_chromedriver import Chrome
from selenium.webdriver.chrome.options import Options



from module_tool import get_folder_profile_path


def create_profile(profile_name):
    profile_path = get_folder_profile_path() + '\\' + f'Profiles\\{profile_name}'
    if path.exists(profile_path):
        print(f"Profile {profile_name} Exist !")
        sleep(3)
    else:
        options = Options()
        options.add_argument(f"--user-data-dir={profile_path}")
        try:
            driver = Chrome(options=options ,use_subprocess=True)
            driver.close()
        except:
            if not path.exists(profile_path):
                print(f"Create Profile Fail: {profile_name}")


def manager_profiles(profile_name): # Về cách làm thì chả khác gì vs việc tạo profile căn bản là mình k báo lỗi thôi ahihihi
    profile_path = get_folder_profile_path() + '\\' + f'Profiles\\{profile_name}'
    # profile_path = get_folder_profile_path() + '\\' + f'Profiles\\{profile_name}'
    if path.exists(profile_path):
        options = Options()
        options.add_argument(f"--user-data-dir={profile_path}")
        try:
            driver = Chrome(options=options ,use_subprocess=True)
            driver.get("https://google.com")
        except:
            pass

