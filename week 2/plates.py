
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid" ,end='')
    else:
        print("Invalid", end='')

def is_valid(s):
    valid = True
    dig= 0
    if(len(s) < 2 or len(s) > 6 ):
        valid = False
        return valid
    if(s[0].isdigit() or s[1].isdigit()):
        valid= False
        return valid
    for char in s:
          if( not char.isalnum()):
            valid = False
            return valid
          if(dig > 1 and char.isalpha()):
            valid = False
            return valid
          if(char.isdigit()):
            dig += 1
          if(dig == 1 and char == "0"):
            valid = False
            return valid
    return valid

main()