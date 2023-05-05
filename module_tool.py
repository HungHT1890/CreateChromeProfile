from os import makedirs , path , listdir , system
from shutil import rmtree
from pathlib import Path



def create_profiles_folder(name_folder="Profiles"):
    if not path.exists(name_folder):
        makedirs(name_folder)

def delete_profile(name_folder):
    profile_path = f'Profiles\\{name_folder}'
    try:
        rmtree(profile_path)
        return True
    except:
        return False
def get_folder_profile_path():
    return str(Path.cwd())

def get_profiles():
    profiles = []
    profiles =  [profile_name for  profile_name  in listdir("Profiles") if not profile_name.endswith('.txt')]
    profile_count = len(profiles)
    print(f"Profiles:  {profile_count}")
    for x in profiles:
        profile_index = profiles.index(x)
        print(f"{profile_index + 1}: {x}")
    return profiles
def clear_chrome_process():
    try:
        system('taskkill /im chrome.exe')
    except:
        pass
    system('cls')
    

if __name__ == "__main__":
    get_profiles()

    