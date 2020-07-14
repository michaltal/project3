grade = int(input("enter grade: "))

if grade>=0 and grade<=100:
    if grade>=90:
        print("very good")
    if grade<90 and grade>=80:
        print("good")
    if grade<80 and grade>=70:
        print("ok")
    if grade<70:
        print("failed")
else:
    print("invalid grade")


if grade>=0 and grade<=100:
    if grade>=90:
        print("very good")
    else:
        if grade>=80:
            print("good")
        else:
            if grade>=70:
                print("ok")
            else:
                print("failed")
else:
   print("invalid grade")

if grade>=0 and grade<=100:
    if grade>=90:
        print("very good")
    elif grade>=80:
        print("good")
    elif grade>=70:
        print("ok")
    else:
        print("failed")
else:
   print("invalid grade")