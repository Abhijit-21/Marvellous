def Add(val1,val2):
    result = val1 + val2
    return result

def main():
    print("Enter the first number is : ")
    no1 = int(input())
    print("Enter the second number is : ")
    no2 = int(input())
    ret = Add(no1,no2)
    print("Addition is " , ret)

if __name__ == "__main__":
    main()