class Student:
    def __init__(self):
        self._score = 0

    def get_score(self):
        return self._score

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError("score must be an integer!")
        if score < 0 or score > 100:
            raise ValueError("score must between 0 - 100!")
        else:
            self._score = score


if __name__ == "__main__":
    stu = Student()
    # stu.set_score("")

    stu.set_score(60)
    print(stu.get_score())

    # stu.set_score(321)
    # print(stu.get_score())
