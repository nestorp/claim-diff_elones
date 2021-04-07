from json import JSONEncoder

default_rating = 1000
init_k = 40
standard_k = 20
master_k = 10
scale_factor = 400
base_n = 10.0


class Statement:
    "A statement to be ranked"

    def __init__(self, id, text, label, rating=1000, num_matches=0):
        self.id = id
        self.text = text
        self.label = label
        self.rating = rating
        self.num_matches = num_matches
        self.k = standard_k
        self.update_k()

    def __str__(self):
        return "Statement: " + str(self.__dict__)

    def __repr__(self):
        return "Statement: " + str(self.__dict__)

    def update_k(self):
        if self.num_matches <= 30:
            self.k = init_k
        elif self.rating >= 2400:
            self.k = master_k
        else:
            self.k = standard_k


# subclass JSONEncoder
class StatementEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__


def expected_score(statement1, statement2):
    return 1 / (base_n ** ((statement2.rating - statement1.rating) / scale_factor) + 1)


def new_rating(statement, actual_score, expected_score):
    return statement.rating + statement.k * (actual_score - expected_score)
    pass


def process_match(samples, stat1, stat2, easier, harder, tie, correct_only=False, is_correct=None):
    if not tie:
        statementA = samples[easier]
        statementB = samples[harder]
    else:
        statementA = samples[stat1]
        statementB = samples[stat2]

    sA_expected = expected_score(statementA, statementB)
    sB_expected = expected_score(statementB, statementA)

    if tie:
        sA_next_rating = new_rating(statementA, 0.5, sA_expected)
        sB_next_rating = new_rating(statementB, 0.5, sB_expected)
    else:
        sA_next_rating = new_rating(statementA, 0, sA_expected)
        sB_next_rating = new_rating(statementB, 1, sB_expected)

    statementA.num_matches += 1
    statementB.num_matches += 1

    statementA.rating = sA_next_rating
    statementB.rating = sB_next_rating

    statementA.update_k()
    statementB.update_k()

    samples[statementA.id] = statementA
    samples[statementB.id] = statementB

    return samples