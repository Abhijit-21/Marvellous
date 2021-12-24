def ChkNum(val):
    #val = 0
    if val % 2 ==0:
        print("Even Number")
    else:
        print("Odd Number")


def main():
    print("Enter the number : ")
    no1 = int(input())
    ret = ChkNum(no1)
    print("Result is : ", ret)

if __name__ =="__main__":
    main()