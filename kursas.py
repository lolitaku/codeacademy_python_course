class Course:
    def __init__(self, name: str, lecturer: str, time: int):
        self.name = name
        self.lecturer = lecturer
        self.time = time

    def teacth(self):
        print("Lets_teacth")
