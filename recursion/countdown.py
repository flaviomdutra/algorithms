def countdown(i):

    print(i)

    # base case
    if i <= 1:
        return
    
    # recursive case
    else:
        countdown(i-1)


countdown(5) # 5 4 3 2 1
countdown(10) # 10 9 8 7 6 5 4 3 2 1