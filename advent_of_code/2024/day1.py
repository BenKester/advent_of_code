from advent_of_code.utils.parsers import listv

def part1(str) -> str:
    a, b = listv(str, hsep='   ', element_transform=lambda x: int(x))
    a.sort()
    b.sort()
    distance = sum([abs(a[i]-b[i]) for i in range(0, len(a))])
    return f'{distance}'



def part2(str) -> str:
    a, b = listv(str, hsep='   ', element_transform=lambda x: int(x))
    counts = {}
    for b_i in b:
        counts[b_i] = counts.get(b_i, 0) + 1
    similarity_score = sum([a_i * counts.get(a_i, 0) for a_i in a])
    return f'{similarity_score}'

