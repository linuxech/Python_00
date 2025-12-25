#Ask user for their name
name =  input("What's is your name? ").strip().title()

#Remove whitespace from str and capitalize the user's name

#Split user's name into first and last name
first, last = name.split(" ")

#Say hello to user first name
print (f"hello, {last}")        #call the first/last function to call the user
 