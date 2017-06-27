from BankAccount.FrontEnd import account

user = account.Account("liesse","Philips","bukersmoult",100)
user.database.insert(user.first_name,user.last_name,user.account_number,user.amount,user.address)

print(user.database.get_amount_account(user.account_number))