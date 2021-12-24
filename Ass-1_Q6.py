def Check(val):
    if val > 0:
        print("Possitive Number")
    elif val < 0:
        print("Negative Number")
    else :
        print("Zero")
def main():
    print("Enter the number : ")
    no1 = int(input())
    Check(no1)


if __name__ =="__main__":
    main()