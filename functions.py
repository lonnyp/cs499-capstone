from pymongo import MongoClient


connection = MongoClient('localhost', 27017)
db = connection['students']
collection = db['information']


# Creates a document and interacts with the collection
def create_document(document):
    try:
        result = collection.insert(document)
        return result
    except:
        print("Error. Either wrong ID or ID is currently being used.")


# Reads through the database and collection looking for a document(data)
def read_document(document):
    try:
        result = collection.find(document)
        for col in result:
            return col
    except:
        print("Error ")


# Updates document in collection
def update_document(query,new_value):
    try:
        result = collection.update_one(query, new_value)
        return result
    except:
        print("Error")


# removes selected document from collection
def delete_document(document):
    try:
        result = collection.delete_many(document)
        return result
    except:
        print("Incorrect Syntax. please use an integer")

# Allows user to make choices on how they want to interact with the database.
def menu(db, connection, collection):

    user_choice = ''
    user_choice1 = ''
    look_up = ''
    
    while user_choice != 'quit':

        print("\nWelcome to the program!")
        print("\n[1] Enter one to create a database entry.")
        print("[2] Enter two to find a student.")
        print("[3] Enter three to update an item in the database.")
        print("[4] Enter four to delete an item from the database")
        print("[q] Enter quit to exit program.")

        user_choice = input("\nWhat would you like to do: ")
        
        if user_choice == '1':

            for x in collection.find().sort("_id", -1).limit(1):
                print("\nCurrent used ID number: " + str(x['_id'])) 
            while user_choice1 != int:
                try:
                    user_choice1 = int(input("Enter new student ID greater than the current ID.: "))
                    student_id = user_choice1

                    user_choice1 = input("\nEnter new student name.:")
                    student_name = user_choice1
                    new_document = {"_id":student_id, "name": student_name}
                    create_document(new_document)
                    break
                except:
                    print("Incorrect input. Going back to main menu")
                    break

        elif user_choice == '2':
            
            while look_up != None:
                user_choice1 = input("\nEnter the student's first name and last name with proper capitals: ")
                student = {"name": user_choice1}
                look_up = read_document(student)

                if look_up == None:
                    print("Student was not found. Going back to main menu")
                    break
             
                user_choice1 = input("\nDo you want to look up an individual score? Yes or No: ")

                if user_choice1 == 'yes':
                    user_choice1 = input("\nDo you want to see exam, quiz, homework or all of the above?: ")

                if user_choice1 == 'exam':
                    print(look_up['name'], look_up['scores'][0])
                    break

                elif user_choice1 == 'quiz':
                    print(look_up['name'], look_up['scores'][1])
                    break

                elif user_choice1 == 'homework':
                    print(look_up['name'], look_up['scores'][2])
                    break
                else:
                    print(look_up)
                    break
                
           
        elif user_choice == '3':
            print("\nUpdate student information\n")

            user_choice1 = int(input("Enter id of student: "))
            student_id = {"_id":user_choice1}

            user_choice1 = input("Enter new field: ")
            new_field = user_choice1

            user_choice1 = input("Enter field's new value: ")
            new_value = user_choice1
            
            new_update_query = student_id
            new_update_value = {"$set":{new_field: new_value}}

            update_document(new_update_query,new_update_value)

        elif user_choice == '4':
            user_choice1 = int(input("\nEnter the student Id that you want to delete: "))
            delete_value = {"_id": user_choice1}
            delete_document(delete_value)

        elif user_choice == 'quit':
            print("\nHave a nice day.\n")
        
        else:
            print("\nI don't understand that choice, please try again.\n")
        

