import json
import random

train = list()
valid = list()

with open("/usr/cs/public/brmijo/zipQA3.txt", "r") as f:
    for i, line in enumerate(f):
        if i == 0:
            continue
        zip_sep = line.find("|ZIP_SEP|")
        prompt = line[:zip_sep]
        response = line.strip()[zip_sep + len("|ZIP_SEP|"):]
        if random.random() < 0.7:
            train.append({
                "prompt": prompt,
                "response": response
            })
        else:
            valid.append({
                "prompt": prompt,
                "response": response
            })


with open("zipQA3.json", "w") as g:
    g.write(json.dumps({
        "train": train,
        "valid": valid
    }))
