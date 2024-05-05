import psutil

def get_users():
    users = []
    for user in psutil.users():
        user_info = {
            'name': user.name,
            'terminal': user.terminal,
            'host': user.host,
            'started': user.started
        }
        if user.name == 'NT AUTHORITY\\SYSTEM':
            user_info['authorization'] = 'Administrator'
        else:
            user_info['authorization'] = 'Standard User'
        users.append(user_info)
    return users

def main():
    user_list = get_users()
    for user in user_list:
        print(f"Username: {user['name']}, Authorization: {user['authorization']}")

if __name__ == "__main__":
    main()
