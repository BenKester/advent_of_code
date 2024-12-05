from advent_of_code.utils.parsers import *

def get_middle_page(rules:dict, p:list[str]):
    printed = set()
    for page in p:
        for rule in rules.get(page, []):
            if rule in printed:
                return 0
        printed.add(page)
    middle_page = int(p[int((len(p)-1)/2)])
    return middle_page


def part1(data:str) -> str:
    rules_section, print_section = data.strip().split('\n\n')
    rules = {}
    for r in rules_section.split('\n'):
        a, b = r.split('|')
        rules[a] = rules.get(a, []) + [b,]
    n = sum([get_middle_page(rules, p.split(',')) for p in print_section.split('\n')])
    return str(n)


def part2(data:str) -> str:
    rules_section, print_section = data.strip().split('\n\n')
    rules = {}
    for r in rules_section.split('\n'):
        a, b = r.split('|')
        rules[a] = rules.get(a, []) + [b,]
    n = 0
    for p in print_section.split('\n'):
        pages = p.split(',')
        if get_middle_page(rules, p.split(',')) == 0:
            for k, v in rules.items():
                if k in pages:
                    for v_i in v:
                        if v_i in pages and pages.index(k) > pages.index(v_i):
                            pages.remove(k)
                            pages.insert(pages.index(v_i), k)
            n += int(pages[int((len(pages)-1)/2)])
    return str(n)