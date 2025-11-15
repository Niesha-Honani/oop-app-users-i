
class User:
    """Class User to handle user sign up information"""
    def __init__(self, name, user_name, email, drivers_license) -> None:
        self.name = name
        self.user_name = user_name
        self.email = email
        self.drivers_license_num = drivers_license

    def __str__(self):
        """function to create new user and print out"""
        return (f"User: {self.name}\n"
                f"User Name: {self.user_name}\n" 
                f"Email: {self.email}\n"
                f"Drivers License: {self.drivers_license_num}\n"
        )

new_user1 = User("Vee", "vee_test", "v@email.com", "ZZZ11DL")
new_user2 = User("Doug", "dg001", "d@email.com", "xsssd")
new_user3 = User("Rex", "trex001", "dino@email.com", "XGL-1")
print(new_user1)
print(new_user2)
print(new_user3)
