class Question:
    def __init__(self, method: 'VotingMethod', description: str):
        self.method = method
        self.description = description

    def answer(self, *args, **kwargs) -> 'Response':
        pass


class Response:
    def __init__(self, question: Question):
        self.question = question
