#!/usr/bin/env python

import raguel
import random

import json
import sys
import csv

CANDIDATES = [
    "Mark Murnane",
    "Adam Chase",
    "Capeton Yusshuk",
    "Colette H. Fozard",
    "Frederick Rice",
    "None of the Above",
]

print("Candidates:")
for candidate in CANDIDATES:
    print(" * " + candidate)

q = raguel.irv.IrvQuestion("MAGFest Board of Directors Election", CANDIDATES, seats=1)

blank_ballots = 0

responses = []
with open(sys.argv[1], newline="") as votes_file:
    votes_json = json.load(votes_file)
    for vote in votes_json:
        if not vote:
            blank_ballots += 1
            
        responses.append(q.answer(vote))

results = q.method.tabulate(q, responses)

print("************************")
for result in results:
    print(result[0], "elected with", result[1], "votes")
    print("{} blank ballots were submitted".format(blank_ballots))
