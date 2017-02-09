from typing import List, Mapping, Sequence, Tuple

from collections import Counter

from raguel.votingmethod import VotingMethod
from raguel.question import Question, Response


class WriteInException(RuntimeError):
    pass


class FptpQuestion(Question):
    def __init__(self, description, candidates, seats=1, reverse=False, write_ins=True):
        super().__init__(FptpMethod(), description)

        self.candidates = set(candidates)
        self.seats = min(seats, 1)
        self.reverse = reverse
        self.write_ins = write_ins

    def answer(self, candidate: str):
        if not self.write_ins and candidate not in self.candidates:
            raise WriteInException(candidate)

        return FptpResponse(self, candidate, write_in=(candidate not in self.candidates))


class FptpResponse(Response):
    def __init__(self, question: FptpQuestion, candidate: str, write_in=False):
        super(FptpResponse, self).__init__(question)

        self.candidate = candidate
        self.write_in = write_in


class FptpMethod(VotingMethod):
    def tabulate(self, question: FptpQuestion, responses: Sequence[FptpResponse], write_in_transform=lambda r: r)\
            -> Tuple[List[str], Mapping[str, int]]:
        counts = Counter()

        for response in responses:
            candidate = response.candidate
            if response.write_in:
                candidate = write_in_transform(response.candidate)

            counts[candidate] += 1

        if question.reverse:
            return reversed(counts.most_common())[:question.seats]
        else:
            return counts.most_common(question.seats)
