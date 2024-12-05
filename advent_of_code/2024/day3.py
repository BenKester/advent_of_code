import re

def calc(s:str) -> int:
    rx = r'mul\(([0-9]+),([0-9]+)\)'
    values = re.findall(rx, s)
    result = sum([int(pair[0]) * int(pair[1]) for pair in values])
    return result


def prob1(data:str) -> str:
    return str(calc(data))


def prob2(data:str) -> str:
    dos = data.split(f'do()')
    total = sum([calc(d.split(f"don't()")[0]) for d in dos])
    return str(total)

