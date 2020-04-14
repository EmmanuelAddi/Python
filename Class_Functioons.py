
class Functions:

    def __init__(self, names, reg_no, course, gpa, is_on_session):
        self.names = names
        self.reg_no = reg_no
        self.course = course
        self.gpa = gpa
        self.is_on_session = is_on_session

    def on_honor_roll(self):
        if self.gpa >= 4:
            return True
        else:
            return False