import json

f = open('weak_dir_patterns.json','r')
patterns = json.load(f)
f.close()

print(patterns)