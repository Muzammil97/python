print("\n \nGrade & Percentage Calculator \n")
print("All Subject are of 100 Marks \n")


print("Enter 'x' for exit. \nOr Press Enter or any key to Run the Program ");
mark1 = input();
if mark1 == 'x':
    exit();
else:
    print("Enter your Marks in Physics: ")
sub1=int(input())
print("Enter your Marks in Mathamatic: ")
sub2=int(input())
print("Enter your Marks in Computrt Science: ")
sub3=int(input())
print("Enter your Marks in Urdu: ")
sub4=int(input())
print("Enter your Marks in Pakistan Studies: ")
sub5=int(input())
sum = sub1 + sub2 + sub3 + sub4 + sub5;
percentage = (sum/500)*100;
if percentage>100:
    print("Your Percentage is going above 100%")
else:
        print("Your Percentage = ", percentage,"%");
if (percentage >= 80 and percentage<=100):
    print ("Your Grade is A+");
elif (percentage>=70 and percentage<=79):
    print("Your Grade is A");
elif (percentage>=60 and percentage<=69):
    print("Your Grade is B");
elif (percentage>=50 and percentage<=59):
    print("Your Grade is C");
elif (percentage>=40 and percentage<=49):
    print("Your Grade is D");
elif (percentage>=0 and percentage<=40):
    print("Your Grade is F and You're Fail");
else:
        print("Kindly Recheck Your Numbers, You put something wrong..!!");

