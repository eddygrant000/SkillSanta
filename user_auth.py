database = {
    1001:{
        'name': 'Sachin',
        'age': 22,
        'email': 'eddygrant000@gmail.com',
        'password': 'red@123',
    },
    1002:{
        'name': 'Tanuj',
        'age': 25,
        'email': 'tanuj@gmail.com',
        'password': 'tanu123',
    }
}
# data = {key: value, key2: value2}
# database.
account = int(input("Enter account number: "))
passwd = input("Enter password: ")

if account in database.keys():
    if passwd == database[account]['password']:
        print(f"Login Success\nWelcome {database[account]['name']}")
    else:
        print("Password FAiled")
else:
    print("Account is Not Exist")