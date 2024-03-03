def main():
    time_str = input("Enter the time: ")

    time_in_hours = convert(time_str)

    if 7.0 <= time_in_hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_in_hours <= 13.0:
        print("lunch time")
    elif 18.0 <= time_in_hours <= 19.0:
        print("dinner time")

def convert(time):
    hours, mint = map(int, time.split(':'))


    time_hrs = hours + (mint / 60)

    return time_hrs

if __name__ == "__main__":
    main()
