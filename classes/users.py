class Users():

	def __init__(self,first_name,last_name,email, phone_number, age):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.phone_number = phone_number
		self.age = age
		self.login_attempts = 0

	def describe_user(self):
		print("These are the user's details: ")
		print(self.first_name)
		print(self.last_name)
		print(self.email)
		print((self.phone_number))
		print(str(self.age))

	def greet_user(self):
		print("Hello " + self.first_name.title() + " " + self.last_name.title())

	def increment_login_attempts(self):
		self.login_attempts += 1
		print(str(self.login_attempts))

	def reset_login_attempts(self):
		self.login_attempts = 0
		print(str(self.login_attempts))

class Admin(Users):

	def __init__(self,first_name,last_name,email, phone_number, age):
	
		super().__init__(first_name,last_name,email, phone_number, age)
		self.privileges = []

	def list_privileges(self):
		print("\nPrivileges: ")
		for privilege in self.privileges:
			print("- " + privilege)


user_1 = Admin('greg','evans','greg@me', 2948920102, 23)
user_1.describe_user()

user_1.privileges = [
	'can add post',
	'can delete post',
	'can ban user']

user_1.list_privileges()

