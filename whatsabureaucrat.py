import random
class GradeTooHighException(Exception):
    pass

class GradeTooLowException(Exception):
    pass

class FormGradeTooLowException(Exception):
    pass

class Bureaucrat:
    def __init__(self, name, grade):
        if grade < 1:
            raise GradeTooHighException("For thee is too powerful")
        if grade > 150:
            raise GradeTooLowException("You're not qualified")
        self.name = name
        self.grade = grade
    def promote(self):
        if self.grade < 2:
            raise GradeTooHighException("For thee is too powerful, hence thou shalt not be promoted to thy higher ranks")
        self.grade =- 1

    def demote(self):
        if self.grade > 149:
            raise GradeTooLowException("For thee lacks basic contempory education, for thou shalt not be unable to be demoted")
        self.grade =+ 1

class Form:
    def __init_(self, name, sign_grade, exec_grade, is_signed):
        self.name = name
        self.sign_grade = sign_grade
        self.exec_grade = exec_grade
        self.is_signed = False
    def be_signed(bureaucrat):
        if grade > self.sign_grade:
            raise FormGradeTooLowException("For thy writing appratus is not worthy, for thee shalt not pass thy gates")
        is_signed = True

class shrubberycreationform(Form):
    def execute():
        print("thy trees shall assault thou")

class robotomyrequestform(Form):
    def execute():
        number = random.randint(0, 1)
        if number == 0:
            print("for thee is now robotic")

class presidentialpardonform(Form):
    def execute():
        print("It is me, william shakespeare. for thee is now excused from thy meeting with thy presidential pardon. thou shalt not infringe upon thy rules of thee president.")


        
    

try:
    grade = int(input("Enter your bureaucrat grade (1-150): "))
    if grade < 1:
        raise GradeTooHighException("For thy grade is extremely, dubiously high, for thee shalt not believe.")
    if grade > 150:
        raise GradeTooLowException("For thee grades are too low, for thou shalt not be believed.")
    print("Thy grades shalt be accepted into thy system.")
except GradeTooHighException or GradeTooLowException as e:
    print("For thee has found thy error, for thou shalt not accept.")

try:
    bob = Bureaucrat("Bob", 99)
    passport_form = Form("PassportApplication", 30, 25)
    passport_form.be_signed(bob)
except Exception as e:
    print("For thee is not able to sign thy form, as thy does not have anything")


