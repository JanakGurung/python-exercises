# Create a simple grade checker that allows the user to check the grades for as much as they like.
Score= int(input("Enter the score:"))
if (Score >= 85):
    print("Congratulations you obtained A grade")
elif (Score >70):
    print("Congratulations you obtained B grade")
elif (Score >55):
    print ("Congratulations you obtained C grade")
elif (Score > 35):
    print("Congratulations you obtained D grade")
else:
    print("You Failed.")