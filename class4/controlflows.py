# Program to calculate the marks and output the total and percentage
# if percentage is above 75, then print best
# if percentage is above 50 & below 75, then print very good
# if percentage is above 35 & below 50, then print good
# if percentage is below 35, then print fail

marks1 = input("Marks1:")
marks2 = input("Marks1:")
total = int(marks1)+int(marks2)
percentage = int((total/40)*100)

if percentage >= 75:
    print("best")
elif percentage > 50 and percentage < 75:
    print("very good")
elif percentage > 35 and percentage < 50:
    print("good")
elif percentage < 35:
    print("Fail")

#    print("very good")
