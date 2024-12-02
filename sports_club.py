class Person():
    def __init__(self, name, age, contact_number):
        self.name = name
        self.age = age
        self.contact_number = contact_number

    def set_details(self, name, age, contact_number):
        self.name = name
        self.age = age
        self.contact_number = contact_number
    
    def get_details(self):
        print("Name:",self.name, "¦ Age:",self.age, "¦ Contact Number:",self.contact_number)

class Member(Person):
    def __init__(self, name, age, contact_number):
        super().__init__(name, age, contact_number)

    def set_membership_details(self, membership_id, sport,performace_scores):
        self.membership_id = membership_id
        self.sport = sport
        self.performance_scores = []

    def add_performance_score(self,performace_scores):
        self.performance_scores.append(performace_scores)
        
    
    def calculate_avg_score(self):
        if self.performance_scores != []:
            total = sum(self.performance_scores)
            num_of_grades = len(self.performance_scores)
            average = total / num_of_grades
            return average
        else:
            return 0

    def get_member_summary(self):
        print("Membership ID:",self.membership_id,"¦Sport:",self.sport,"¦Average Performance Score:",self.calculate_avg_score())

class Coach(Person):
    def __init__(self, name, age, contact_number):
        super().__init__(name, age, contact_number)

    def set_coach_details(self,coach_id,specialisation,salary):
        self.coach_id = coach_id
        self.specialisation = specialisation
        self.salary = salary
        self.mentees_list = []

    def assign_mentee(self,member):
        self.mentees_list = [member]
        print("Coach",self.name,"is now mentoring",member.name,"in",member.sport)
        return self.mentees_list

    def get_mentees(self):
        print(self.mentees_list)
        
    def increase_salary(self,incerease):
        multiplier = (100 + incerease)/ 100 
        self.salary = self.salary + (self.salary/multiplier)
        self.salary = round(self.salary, 2)
        return self.salary
    
class Staff(Person):
    def __init__(self, staff_id, postition, yrs_of_service):
        self.staff_id = staff_id
        self.postition = postition
        self.yrs_of_service = yrs_of_service

    def set_staff_details(self, staff_id, postition, yrs_of_service):
        self.staff_id = staff_id
        self.postition = postition
        self.yrs_of_service = yrs_of_service
    
    def increment_service_yrs(self):
        self.yrs_of_service = self.yrs_of_service + 1
        return self.yrs_of_service
    
    def assist_member(self, member):
        print("Staff",self.name,"assisted",member.name,"in resolving an issue")

    def get_staff_summary(self):
        print("Staff ID:",self.staff_id,"Position:",self.postition,"¦Years of service:",self.yrs_of_service)


#----------------------------------------------


tst_1 = Member("Guy",19,"07264 135579")
tst_1.set_membership_details("F12345","Football",0)

tst_1.add_performance_score(70)
tst_1.add_performance_score(56)
tst_1.add_performance_score(96)
tst_1.add_performance_score(12)
tst_1.add_performance_score(45)

tst_1.get_member_summary()

tst_2 = Member("Dude",18,"07285 609339")
tst_2.set_membership_details("B12345","Basketball",0)

tst_2.add_performance_score(28)
tst_2.add_performance_score(94)
tst_2.add_performance_score(96)
tst_2.add_performance_score(83)
tst_2.add_performance_score(82)

tst_2.get_member_summary()

tst_3 = Coach("Gal",30,"07269 146279")
tst_3.set_coach_details("C54321","Football",30000)

print(tst_3.name,"'s old salary: £",tst_3.salary)
tst_3.increase_salary(15)
print(tst_3.name,"'s new salary: £",tst_3.salary)


tst_4 = Coach("Girl",26,"07552 579471")
tst_4.set_coach_details("C54421","Tennis",30000)

tst_5 = Staff("Cool-Name",44,"07896 4521869")
tst_5.set_staff_details("S00001","Owner",10)
tst_5.increment_service_yrs()
tst_5.get_staff_summary()
 