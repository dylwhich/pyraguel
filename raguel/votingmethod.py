from typing import Any, List

from raguel.question import Question, Response


class VotingMethod:
    def __init__(self):
        pass

    def question(self) -> Question:
        pass

    def tabulate(self, question: Question, responses: List[Response]) -> Any:
        pass
