marks1 = int(input("Enter the marks 1: "))
marks2 = int(input("Enter the marks 2: "))
marks3 = int(input("Enter the marks 3: "))

#check for total percentage 
total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Your are pass ")

else:
    print("You are fail try again next year😂")