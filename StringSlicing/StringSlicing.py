# password = input("Enter your password:")
# if len(password)<8:
#    print("Your password is not long enough!")
   
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# print("The first 5 letters of the alphabet are: " + alphabet[:5])
# print("The last 5 letters of the alphabet are: " + alphabet[-5:])
# print("The letters in between are: "  + alphabet[5:-5])

# date = "05 January 2019"
# day = date[:2]  #First 2 characters
# year = date[-4:] #Last 4 characters
# month = date[3:-5] #The remaining characters in the middle

# dateOfBirth = "15 January 2000"
# if "January" in  dateOfBirth:
#    print("You were born in January!")
   
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# pos = alphabet.find("C")
# print("Letter C is at position: " + str(pos))

print(r"-> Year Group Using two digits (e.g. “07” for year 7, “11” for year 11, “00” for staff members)")
print(r"-> 1 character for their initial (first letter of their firstname)")
print(r"-> The user’s lastname")
print(r"-> A 2-digit code: “_S” for students, “_T” for teachers, “_A” for admin staff.")
username = input("\nType in your school username in the format given above: ")
if len(username) < 6:
    print("Enter a valid username.")
elif username.find("_") == -1:
    print("Enter a valid username.")
else:
    if username[0:2] == "00":
        print("Staff")

    person_type = ""
    if username[-1] == "S":
        person_type = "Student"
    elif username[-1] == "A":
        person_type = "Admin"
    elif username[-1] == "T":
        person_type = "Teacher"
    print(f"Year group for {person_type} {username[2]} {username[3:-2]} = {username[0:2]}")