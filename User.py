"""user_class used to build new users"""
import userMgmt

print("="*40)
print("Create New User")
print("="*40)
#starter users - User app 1
Tom = userMgmt.User("Tom", "tom@gmail.com", 0)
Jim = userMgmt.User("Jim", "jim@yahoo.com", 1)
#starter posts - User app 1
Tom.user_post("This is a new post")
Tom.user_post("Also a new post")
Jim.user_post("This is a new post")
Jim.user_post("Also a new post")
Tom.print_user_posts()

userMgmt.User.print_all_user_posts()

#User app 2 + 3
QUIT_APP = False
while QUIT_APP is not True:
    userMgmt.User.user_interface()
    option=input("Enter an option: ")
    if option not in ('1','2','3','4', '5', 'Q', 'q'):
        print("Invalid option. Try again.")
        userMgmt.User.user_interface()
    if option == '1':
        name = input("Enter a user: ")
        user = userMgmt.User.registered_users.get(name)
        if user is None:
            print("User is not registered")
        else:
            user.print_user_posts()                             
    if option == '2':
        userMgmt.User.print_all_user_posts()
    if option == '3':
        name = input("Enter user: ")
        message = input("Enter message: ")
        user = userMgmt.User.registered_users.get(name)
        if user is None:
            print("User is not registered")
        else:
            user.user_post(message)
            print(f"{name} message posted: {message}")
    if option == '4':
        user = userMgmt.User.select_user()
        user.delete_menu()
        userMgmt.User.print_all_user_posts()
    if option == '5':
        userMgmt.User.create_user()
    if option == 'q'.lower():
        QUIT_APP = True
