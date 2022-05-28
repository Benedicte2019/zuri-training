class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        pass
    def change_name(self, name):
        self.name = name
        return self.name
    def change_age(self, age):
        self.age = int(age)
        return self.age
    def add_track(self, tracks):
        # self.tracks = self.tracks + [tracks]
        return self.tracks + [tracks]
    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

# print(Bob.change_age(34.5))