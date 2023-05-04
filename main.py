from module_tool import create_profiles_folder , get_profiles
from create_profiles import create_profile , manager_profiles
from os import system
system("title Create Chrome Profile - Manager Chrome Profile ^| Code Buy T.ME/HUNGHT1890")
def main():
    try:
        create_profiles_folder() #Kiểm tra và tạo folder chứa các profile
        option_choice = int(input("1:Create-Profile\n2:Open-Profile\n=> "))
        system('cls')
        if option_choice == 1:
            profile_name = input("Enter Profile Name: ")
            create_profile(profile_name)
            system('cls')
        else:
            profiles = get_profiles()
            profile_index = int(input("Enter Profile Index: "))
            profile_name_open = profiles[profile_index - 1]
            print(profile_name_open)
            manager_profiles(profile_name_open)
            system('cls')
    except Exception as f:
        print(f"Error: {f}")


if __name__ == "__main__":
    while True:
        main()