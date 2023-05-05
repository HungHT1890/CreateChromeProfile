from module_tool import create_profiles_folder , get_profiles , clear_chrome_process , delete_profile
from create_profiles import create_profile , manager_profiles
from os import system
system("title Create Chrome Profile - Manager Chrome Profile ^| Code Buy T.ME/HUNGHT1890")
def main():
    try:
        create_profiles_folder() #Kiểm tra và tạo folder chứa các profile
        option_choice = int(input("1:Create-Profile\n2:Open-Profile\n3:Delete Profile\n4:Close All Chrome \n=> "))
        system('cls')
        if option_choice == 1:
            option_create = int(input("1: Create By Name\n2: Create By List\n=> "))
            if option_create == 1:
                profile_name = input("Enter Profile Name: ")
                create_profile(profile_name)
            else:
                list_name_path = 'Profiles\\list_name.txt'
                list_name = open(list_name_path , 'r', encoding='utf-8').readlines()
                for name in list_name:
                    create_profile(name.strip())

            system('cls')
        elif option_choice == 2:
            profiles = get_profiles()
            if len(profiles) != 0:
                profile_index = int(input("Enter Profile Index: "))
                profile_name_open = profiles[profile_index - 1]
                system('cls')
                print(f'Open: {profile_name_open}')
                manager_profiles(profile_name_open)
                system('cls')
            else:
                print("NOT FOUND CHROME PROFILES => CREATE !")
                return main()
        elif option_choice == 3:
            profiles = get_profiles()
            if len(profiles) != 0:
                profile_index = int(input("Enter Profile Index: "))
                profile_name = profiles[profile_index - 1]
                system('cls')
                delete_profile(profile_name)

        elif option_choice == 4:
            clear_chrome_process()
        else:
            return main()
    except Exception as f:
        print(f"Error: {f}")


if __name__ == "__main__":
    while True:
        main()