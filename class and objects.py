
class Student:
    # [assignment] Skeleton class. Add your code here

    def __init__(self,name,age,tracks,score):
        self.name=str(name)
        self.age=int(age)
        self.track=list(str(tracks))
        self.score=float(score)

    def change_name(self,change_name):     
        self.name = change_name
        print("This student new name is",self.name)


    def change_age(self,change_age):    
        self.age = change_age
        print("This student new age is",self.age)


    def add_track(self,add_track):     
        self.track = add_track
        print("This student new name is",self.track)

    def get_score(self):
        print("This student new score is",self.score)
         
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()  
    




  
    
