def think():

    # ask the user for the amount of minutes it has studied, separated by a comma ",";
    input_str = input("Paste the times separated by ntg but a conmma:-")

    # split the input string based on commas ","; and return it as a string;
    input_str1 = input_str.split(",")

    #convert contents of the input_str1 list into integers using string concatenation
    integer_list = [int(i) for i in input_str1]


    # add all the integers from the integer list together and divide it by 60  to get an hour value
    P = sum(integer_list)
    Q = P/60
    return Q, "hours"


print(think())
