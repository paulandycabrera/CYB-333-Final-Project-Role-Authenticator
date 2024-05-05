import psutil

#retrieves current logged-in users and creates a list, a dictionary is created based on the parameters listed below
def get_users():
    users = []
    for user in psutil.users():
        user_info = {
            'name': user.name,
            'terminal': user.terminal,
            'host': user.host,
            'started': user.started
        }
        #checks each user.name for the tag 'NT AUTHORITY\\SYSTEM' which denotes ADMIN priveleges.
        if user.name == 'NT AUTHORITY\\SYSTEM':
            user_info['authorization'] = 'Administrator'
        else:
            user_info['authorization'] = 'Standard User'
        users.append(user_info)
    return users

#retrieves the user list and prints out the user authorization level
def main():
    user_list = get_users()
    for user in user_list:
        print(f"Username: {user['name']}, Authorization: {user['authorization']}")

if __name__ == "__main__":
    main()
