import json

filenames = [
    "NASDAQ.txt",
    "NYSE.txt"
]
symbols = {}
for file in filenames:
    with open(file) as f:
        for line in f.readlines():
            try:
                symbol, name = line.rstrip().split("\t")
                symbols[symbol] = name
            except:
                try:
                    line = line.rstrip().split()
                    symbols[line[0]] = "".join(line[1:])
                except:
                    print(f"error processing line: {line}")

with open('symbols.json', 'w') as outfile:
    json.dump(symbols, outfile)