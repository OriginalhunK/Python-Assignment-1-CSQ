class multi():
    def Subfields():
        subfields = ["Machine Learning", "Neural Network", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Subfields in AI are:")
        for field in subfields:
              print(field)


    def OddEven():
        num=int(input("Enter Your Number: "))
        if((num%2)==1):
             print("is Odd Number")
             message="Odd Number"
        else:
             print("is Even Number")
             message="Even Number"
        return message


    def eligibility():
        gender = str(input("Enter your Gender (male/female): "))
        age = int(input("Enter your age: "))
        if gender == 'male' and age >= 21:
               print("Eligible")
        elif gender == 'female' and age >= 18:
               print("Eligible")
        elif gender == 'male' and age < 21:
               print("Not Eligible")
        elif gender == 'female' and age < 18:
               print("Not Eligible")
        else:
               print("Invalid Input")


    def subjects():
        subject1 = int(input("Enter Your subject1 Mark: "))
        subject2 = int(input("Enter Your subject2 Mark: "))
        subject3 = int(input("Enter Your subject3 Mark: "))
        subject4 = int(input("Enter Your subject4 Mark: "))
        subject5 = int(input("Enter Your subject5 Mark: "))
        Total =  subject1 + subject2 + subject3 + subject4 + subject5
        maxmark = 500
        ftotal = Total/maxmark
        percentage = ftotal * 100
        print("Your Total Percentage is: ",percentage)
        
           

    def AOtriangle():
        height = int(input("Enter the Height:"))
        breadth = int(input("Enter the Breadth:"))
        AOtriangle = (height*breadth)/2
        print("Area of Triangle: ",AOtriangle)

          
    
    def perimeter():
        height1 = int(input("Enter height1: "))
        height2 = int(input("Enter height2: "))
        Breadth = int(input("Enter Breadth: "))
        periofTriangle = height1 + height2 + Breadth
        print("Perimeter of Triangle: ",periofTriangle)     
        
    


    

    
    
          
    


    


   