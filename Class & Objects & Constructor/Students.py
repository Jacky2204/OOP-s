# Create a Student class:
# Attributes: name, roll_no, marks
# Method: display_details()
# Method: is_pass() (pass if marks >= 40)


# with constructor

class Students:       # class
    
    def __init__(self,name,roll_no,marks):      # Constructor
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
        
    
    def display_details(self):            #method
        print(f"My name is {self.name} and roll no is {self.roll_no}. I scored {self.marks} marks.")
        
    def is_Pass(self):             #method
        if self.marks >=40:
            print('I am Pass')
        else:
            print("I am Fail")

a=Students("John",102,39)            # Object
a.display_details()    # method call using Object
a.is_Pass()             # method call using Object


b=Students("Jony",103,89)            # Object
b.display_details()    # method call using Object
b.is_Pass()             # method call using Object
