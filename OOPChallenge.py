
class Account:
	
	def __init__(self,name,balance):
		
		self.name = name
		self.balance = balance
		
	def deposit(self,amt):
		self.balance += amt
		return "Your new balance is: {}".format(self.balance)
		
	def withdraw(self,amt):
		if amt>self.balance:
			return "Overdraft not allowed"
		else:
			self.balance -= amt
			return "Your new balance is: {}".format(self.balance)
			
	def __str__(self):
		return "Account Owner: {}".format(self.name)+"\nAccount Balance: {}".format(self.balance)