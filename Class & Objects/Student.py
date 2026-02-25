# Create a Student class:
# Attributes: name, roll_no, marks
# Method: display_details()
# Method: is_pass() (pass if marks >= 40)


# without constructor

class Student:       # class
    name="Jacky"
    rolll_no=101
    marks=46
    
    def display_details(self):            #method
        print(f"My name is {self.name} and roll no is {self.rolll_no}. I scored {self.marks} marks")
        
    def is_Pass(self):             #method
        if self.marks >=40:
            print('Pass')
        else:
            print("Fail")

a=Student()            # Object
a.display_details()    # method call using Object
a.is_Pass()             # method call using Object
