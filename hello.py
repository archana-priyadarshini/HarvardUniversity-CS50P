#ask user for their name
name=input("Whats your name? ").strip().title()
#get user's first name
first=name.split(" ")[0]
#say hello to the user
print(f"hello, {first}.")
