class student:
    def __init__(self,name,roll_no, marks):
        self.name=name
        self.roll_no=roll_no
        self.mark=marks
    def calculate_total(self):
        return sum(self.mark.values())
    def average(self):
        return self.calculate_total()/len(self.mark)
    def is_pass(self):
        for mark in self.mark.values():
            if mark<35:
                return False
        return True
    def grade(self):
        avg=self.average()
        if avg>=90:
            return "A"
        elif avg>=75:
            return"B"
        elif avg>=60:
            return "C"
        else:
            return "D"
    def report_card(self):
        print("-----------REPORT CARD-----------")
        print(f"NAME: {self.name}")
        print(f"ROLL NO: {self.roll_no}")
        print("------------MARKS------------")
        for subject,mark in self.mark.items():
            print(f"{subject}: {mark}")
        print(f"RESULT: {'PASS' if self.is_pass() else 'FAIL'}")       
        print(f"TOTAL: {self.calculate_total()}")
        print(f"AVERAGE: {round(self.average(),2)}")
        print(f"GRADE: {self.grade()}")

marks={"ENGLISH":93, "MATHS":67,"SCIENCE":88}


name=input("NAME: ").upper()
roll_no=input("roll num: ")
s1=student(name,roll_no,marks)
s1.report_card()