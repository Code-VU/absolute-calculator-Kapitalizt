def calculateAbsolute():
    
    # This first line is provided for you
    try:
        in_num  = float(input("Enter a number: "))
    except:
        print("Please enter a number.")
        print("---Terminating Program---")
        quit()

    if in_num == 21:
        print("Result: 0")
    elif in_num < 21:
        print(21 - in_num)
    elif in_num > 21:
        print(2*(in_num-21))
    # end assignment




## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculateAbsolute()