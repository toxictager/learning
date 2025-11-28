def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO

    #remove the $
    d= d.replace("$", "")
    d =float(d)
    return d
    # convert to float

    # return the result


def percent_to_float(p):
    # TODO
    p = p.replace("%", "")
    #remove %
    # convert to float
    p =float(p)
    #return value
    p =p/100
    return p
main()