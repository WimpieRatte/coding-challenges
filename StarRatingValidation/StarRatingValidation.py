starRating = int(input("Enter a star rating between 0 and 5? "))
while starRating < 0 or starRating > 5:
    print("Invalid Star Rating - Try Again!")
    starRating = int(input("Enter a star rating between 0 and 5? "))
print("Thank you!")