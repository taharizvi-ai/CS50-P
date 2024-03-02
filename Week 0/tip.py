def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    nd=d.replace("$","")
    fd=float(nd)
    return fd

def percent_to_float(p):
    np=p.replace("%","")
    fp=float(np)/100
    return fp

main()