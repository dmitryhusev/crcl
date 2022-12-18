
with open('res.txt') as f:
    print(f.readlines()[-1].replace('=', '').lstrip())
