class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, score, tracks=[]):
        self.name=name
        self.age=age
        self.tracks=tracks
        self.score=score
        #pass

    # Expected methods
    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        self.age = age

    def add_track(self, tracks):
        self.tracks.append(tracks)

    def get_score(self):
        return self.score

#test create instance of class
Bob = Student(name="Bob", score=20.90, age=26, tracks=["FE","BE"])

#test class methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

#print results
print(Bob.name)
print(Bob.age)
print(Bob.tracks)
print(Bob.get_score())



