lives = 30
for i in range(1, 101):
    if lives == 0:
        print("game over.")
        break
    x = input("Type the input: ")
    if i % 3 == 0:
        if i % 5 == 0:
            # print("fizz-buzz")
            if x == "fizz-buzz":
                print("Correct")
            else:
                print(f"Incorrect. Expected = fizz-buzz")
                lives -= 10
        else:
            # print("fizz")
            if x == "fizz":
                print("Correct")
            else:
                print(f"Incorrect. Expected = fizz")
                lives -= 10
    elif i % 5 == 0:
        # print("buzz")
        if x == "buzz":
            print("Correct")
        else:
            print(f"Incorrect. Expected = buzz")
            lives -= 10
    else:
        # print(i)
        if int(x) == i:
            print("Correct")
        else:
            print(f"Incorrect. Expected = {i}")
            lives -= 10