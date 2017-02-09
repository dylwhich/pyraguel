from typing import Sequence

from raguel.question import Question, Response


class Vote:
    def __init__(self, responses: Sequence[Response]):
        self.responses = responses


class Ballot:
    def __init__(self, questions: Sequence[Question]):
        self.questions = questions

    def cast(self, responses: Sequence[Response]) -> Vote:
        pass
