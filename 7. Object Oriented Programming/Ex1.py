class Student():
    def __init__(self, name, score) -> None:
        self._name = name
        self._score = score

    def result(self):
        approved = True if self._score > 65 else False
        if approved:
            print('The student {} has approved the course with a grade of: {}'.format(self._name, self._score))
        else:
            print('The student {} has failed the course with a grade of: {}'.format(self._name, self._score))

student1 = Student('Daniel', 50)
student1.result()

student2 = Student('Karla', 80)
student2.result()