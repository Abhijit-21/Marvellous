def Div(val):
    if val % 5 ==0:
        print("True")
    else :
        print(False)
def main():
    print("Enter the number : ")
    no1 = int(input())
    Div(no1)


if __name__ =="__main__":
    main()