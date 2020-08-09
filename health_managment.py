def gettime():
    import datetime
    return datetime.datetime.now()

def log(k):
    if k==1:
        c=int(input("Enter 1 for EXERCISE \n\t  2 for Food\n"))
        if c==1:
            value=input("Type here:- ")
            with open("harry-ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully written")
        elif c==2:
            value = input("Type here:- ")
            with open("harry-food.txt", "a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully written")

    elif k==2:
        c = int(input("Enter 1 for EXERCISE \n\t  2 for Food\n"))
        if c==1:
            value = input("Type here:- ")
            with open("rohan-ex.txt", "a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully written")
        elif c==2:
            value = input("Type here:- ")
            with open("rohan-food.txt", "a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully written")

    elif k==3:
        c = int(input("Enter 1 for EXERCISE \n\t  2 for Food\n"))
        if c == 1:
            value = input("Type here:- ")
            with open("hammad-ex.txt", "a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully written")
        elif c == 2:
            value = input("Type here:- ")
            with open("hammad-food.txt", "a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully written")
    else:
        print("Please enter valid input.\n 1 for HARRY \n 2 for ROHAN \n # for HAMMAD")


def retrieve(k):
    if k==1:
        c = int(input("Enter 1 for EXERCISE \n\t  2 for Food\n"))
        if c==1:
            with open("harry-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open("harry-food.txt") as op:
                for i in op:
                    print(i,"end")

    elif k == 2:
        c = int(input("Enter 1 for EXERCISE \n\t  2 for Food\n"))
        if c==1:
            with open("rohan-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open("rohan-food.txt") as op:
                for i in op:
                    print(i,end="")

    elif k==3:
        c = int(input("Enter 1 for EXERCISE \n\t  2 for Food\n"))
        if c == 1:
            with open("hammad-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif c == 2:
            with open("hammad-food.txt") as op:
                for i in op:
                    print(i,end="")
    else:
        print("Please enter valid input.\n 1 for HARRY \n 2 for ROHAN \n 3 for HAMMAD")


print("\n\t\tHealth Management System\n")
end=1
while(end==1):
    a=int(input("\nPress 1 for LOG \n\t  2 for RETRIEVE\n\t  3 for EXIT\n"))
    if a==1:
        b=int(input("Press 1 for HARRY\n\t  2 for ROHAN\n\t  3 for HAMMAD\n"))
        log(b)
    elif a==2:
        b = int(input("Press 1 for HARRY\n\t  2 for ROHAN\n\t  3 for HAMMAD\n"))
        retrieve(b)
    elif a==3:
        exit()