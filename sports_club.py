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

    def set_membership_details(self, membership_id, sport, performace_scores):
        self.membership_id = membership_id
        self.sport = sport
        self.performance_scores = []

    def add_performance_score(self):
        print("somehting")
        
    
    def calculate_avg_score(self):
        if self.score != 0:
            score_total = [self.score]
            score_avg = sum(score_total) / len(score_total)
            return score_avg
        
    def get_member_summary(self):
        print("Membership ID:",self.membership_id,"¦Sport:",self.sport,"¦Average Performance Score:",self.calculate_avg_score())

tst_1 = Person("Guy",19,"07264135579")
tst_1.set_details("Guy",19,"07264 135579")
tst_1.get_details()

tst_1 = Member("Guy",19,"07264135579")
tst_1.set_membership_details("F12345","Football",0)

tst_1.add_performance_score(70)
tst_1.add_performance_score(56)
tst_1.add_performance_score(96)
tst_1.add_performance_score(12)
tst_1.add_performance_score(45)

tst_1.calculate_avg_score()


