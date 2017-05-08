from collections import Counter

from raguel.question import Question, Response
from raguel.votingmethod import VotingMethod


class WriteInException(RuntimeError):
    pass


class IrvQuestion(Question):
    def __init__(self, description, candidates, write_ins=False, seats=1):
        super(IrvQuestion, self).__init__(IrvMethod(), description)

        self.candidates = set(candidates)
        self.write_ins = write_ins
        self.seats = seats

    def answer(self, candidates) -> 'IrvResponse':
        if not self.write_ins:
            for candidate in candidates:
                if candidate not in self.candidates:
                    raise WriteInException(candidate + " is not on the ballot")

        return IrvResponse(self, candidates)


class IrvResponse(Response):
    def __init__(self, question, candidates):
        super(IrvResponse, self).__init__(question)
        self.candidates = candidates


class IrvMethod(VotingMethod):
    def tabulate(self, question: IrvQuestion, responses):
        #: Candidates that have been dropped out
        eliminated = set()
        winners = set()

        counts = Counter()

        for resp in responses:
            if len(resp.candidates):
                counts[resp.candidates[0]] += 1

        # FIXME: Ties in the final round result in undefined behavior

        # TODO: Add support for specifying an alternate cutoff than 50%+1
        # While the most common candidate hasn't received more than half the votes
        while len(winners) < question.seats and len(winners) + len(eliminated) != len(question.candidates):
            while counts.most_common()[0][1] < int(sum(counts.values())/(question.seats+1))+1:
                lowest = counts.most_common()[-1][0]
                print(counts)
                print("Eliminating {lowest}".format(**locals()))

                counts.clear()
                eliminated.add(lowest)

                for resp in responses:
                    for candidate in resp.candidates:
                        if candidate in eliminated:
                            continue

                        if candidate not in winners:
                            counts[candidate] += 1
                        break
            winners.add(counts.most_common()[0][1])

        return counts.most_common()[:question.seats]
