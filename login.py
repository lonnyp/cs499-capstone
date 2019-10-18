
def login():

    import bcrypt
    import getpass
    from pymongo import MongoClient

    connection = MongoClient('localhost', 27017)
    db_two = connection['Administrators']
    collection_two = db_two['login']

    password = ''
    user_name = ''
    user_choice = ''

    while user_choice != 'quit':
        print("Welcome to the login screen")
        user_choice = input("\nHave you created a login? yes, no, quit: ")

        if user_choice == 'quit':
            break

        if user_choice == 'no':
            
            print("Please create a username and password: ")
            
            user_name = input("Enter username: ")
            password = getpass.getpass("Enter password: ").encode('utf-8')
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password, salt)

            result = collection_two.insert({"username": user_name, "password": hashed})

        elif user_choice == 'yes':
            user_name = input("Enter username: ")
            password = getpass.getpass("Enter password: ")

            try:
                look_up = {"username": user_name}
                result = collection_two.find(look_up)
                for col in result:
                    result = col
            
                hashed = result['password']
            
                if user_name == result['username'] and bcrypt.checkpw(password.encode('utf-8'), hashed) :
                    result = True
                    return result
                
                else:
                    print("Wrong password. Try again.")
                     
            except:
                print("Could not find user. Please try again")
    
        else:
            print("Incorrect input. Please try again.")



