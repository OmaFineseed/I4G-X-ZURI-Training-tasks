class Student:
   
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
        self.name= str(name)
        self.age= int(age)
        self.tracks= list(tracks)
        self.score= float(score)

    def change_name(self, new_name):
         self.name= new_name
         print("The student's new name is", new_name)

    def change_age(self, new_age):
        self.age= int(new_age)
        print("Peter is", int(new_age))
        
    def add_track(self, new_track):
           self.tracks= new_track
           print("His new tracks are React.js and", new_track)
       
    def get_score(self):
          print("And his score is", self.score)
          return self.score
      

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()


