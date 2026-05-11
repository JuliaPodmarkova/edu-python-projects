from datetime import datetime

import DateTime
import json
from random import randint

res = []
files = ["file1.json", "file2.json", "file3.json", "file4.json"]

'''for file in files:
    for _ in range(100_000):
        res.append(randint(0, 10000))
    with open(file, 'w') as f:
        json.dump(res, f)
    res = []'''

res_to_count = []
start = datetime.now()
for file in files:
    with open(file, 'r') as f:
        date = json.load(f)
        res_to_count.extend(date)
print(sum(res_to_count))
end = datetime.now()
print(end - start)