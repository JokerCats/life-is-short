class Student:
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError("score must be an integer!")
        if score < 0 or score > 100:
            raise ValueError("score must between 0 ~ 100!")
        self._score = score


if __name__ == "__main__":
    stu = Student()
    stu.score = 20
    print(f"score is : {stu.score}")
