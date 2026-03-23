import os

# Determine a path to store/read user info next to this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USER_FILE = os.path.join(BASE_DIR, 'user_info.txt')

user_name = input("Enter your name to store in file or enter to proceed: ")
if user_name:
    # append the entered name to the file
    with open(USER_FILE, 'a') as file:
        file.write(user_name + "\n")

show_info = input("Do you want to see all user names? y/n: ")
if show_info == 'y':
    try:
        with open(USER_FILE, 'r') as file:
            content = file.readlines()
    except Exception as e:
        print(e, type(e))
    else:
        for line in content:
            print(f'{line.rstrip()}')

# docker run -it --rm -v myvolume:/myapp --name interactive-python-container itcontainer:01
# docker run -it --rm -v myvolume:/myapp/ cff4e11724d4