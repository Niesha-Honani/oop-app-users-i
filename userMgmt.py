"""User module"""
class User:
    """User class for user mgmt and posts"""
    registered_users = {}
    users_posts = {}
    user_id_counter = 2
    

    def __init__(self, name, email_address, user_id):
        self.__name = name
        self.__email_address = email_address
        self.__user_id = user_id
        self.__user_messages = []

        User.registered_users[name] = self
    
        
    def __str__(self):
        print("="*30)
        print("User Info")
        print("="*30)
        return(f"User: {self.__name}\n Email: {self.__email_address}\n UID: {self.__user_id}")
    
    @classmethod
    def create_user(cls):
        """create user method"""
        username = input("Enter a user name: ")
        email_add = input("Enter email address: ")
        
        new_id = cls.user_id_counter
        cls.user_id_counter += 1

        new_user = cls(username, email_add, new_id)
        print(f"New user created:{username} User ID: {new_id}")
        print(User.list_users())
        return new_user
    
    def user_post(self, message):
        """Store a post message for this user."""
        self.__user_messages.append(message)
        #store to global posts list
        if self.__name not in User.users_posts:
            #if Key: User is not in users_posts dict create
            User.users_posts[self.__name] = []

        User.users_posts[self.__name].append(message)

    def print_user_posts(self):
        """Prints all posts for a specific user"""
        if not self.__user_messages:
            print(f"{self.__name} has no posts.")
            return
        
        print(f"{self.__name} posts:")
        for index, msg in enumerate(self.__user_messages):
            print(f"{index} - {msg}")

    @classmethod
    def print_all_user_posts(cls):
        """Prints all users posts"""
        print("All Users' Posts\n")
        for key, value in User.users_posts.items():
            print(f"{key}'s Posts:")
            for i in range(len(value)):
                print(f"{i} - {value[i]}")
            print("\n")

    def delete_menu(self):
        """Delete user posts method"""
        self.print_user_posts()
        try:
            selection = int(input("Select a message to delete:"))
        except ValueError:
            print("Invalid input.")
            return
        
        if selection in range(0,len(self.__user_messages)):
            delete_message = self.__user_messages.pop(selection)
            
            print(f"Deleted message: {delete_message}")
            User.users_posts[self.__name] = self.__user_messages
        else:
            print("Invalid selection.")

    @classmethod
    def list_users(cls):
        """list users method"""
        print("User:")
        for index, name in enumerate(cls.registered_users.keys()):
            print(f"{index} - {name}")

    @classmethod
    def select_user(cls):
        """user selection method"""
        cls.list_users()
        selection = int(input("Select a user: "))
        names = list(cls.registered_users.keys())
        selected = names[selection]
        return cls.registered_users[selected]
    
    @classmethod
    def user_interface(cls):
        """user interface method"""
        print("""    
               User Management System""")
        print("""
              1. View User Post
              2. View All User Posts
              3. Create a Post
              4. Delete a Post
              5. Create a New User
              (Q)uit
              """)
