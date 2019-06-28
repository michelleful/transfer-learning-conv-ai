import json
import random

from collections import defaultdict


NUM_DISTRACTORS = 4
responses = defaultdict(list)

train = list()
valid = list()

with open("zipQA3.txt", "r") as f:
    for i, line in enumerate(f):
        if i == 0:
            continue
        zip_sep = line.find("|ZIP_SEP|")
        prompt = line[:zip_sep]
        response = line.strip()[zip_sep + len("|ZIP_SEP|"):]
        responses[prompt].append(response)


for prompt, resps in responses.items():
    for resp in resps:

        def get_random_response():
            random_prompt = None

            while random_prompt is None:
                random_prompt = random.choice(list(responses.keys()))
                if random_prompt == prompt:
                    random_prompt = None
            return random.choice(responses[random_prompt])

        # get 4 random other responses from different prompts
        distractors = [get_random_response() for i in range(NUM_DISTRACTORS)]

    if random.random() < 0.7:
        train.append({
            "history": [prompt],
            "candidates": distractors + [resp]
        })
    else:
        valid.append({
            "history": [prompt],
            "candidates": distractors + [resp]
        })

with open("zipQA3.json", "w") as g:
    g.write(json.dumps({
        "train": train,
        "valid": valid
    }, indent=2))
