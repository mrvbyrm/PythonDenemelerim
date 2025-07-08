print("User Login")

sys_name="admin"
sys_password="1234"

user_name=input("Enter Username:")
user_password=input("Enter User Password:")

if(sys_name==user_name and sys_password!=user_password):
    print("Incorrect Password!")
elif(sys_name!=user_name and sys_password==user_password):
    print("Incorrect Username!")
elif(sys_name!=user_name and sys_password!=user_password):
    print("Incorrect Username and Password!")
else:
    print("Logged in to the system successfully!")