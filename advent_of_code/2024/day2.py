from advent_of_code.utils.parsers import listh

def part1(data:str) -> str:
    reports = listh(data, hsep=' ', element_transform=lambda x:int(x))
    total_safe = 0
    for report in reports:
        diffs = [report[i+1]-report[i] for i in range(0, len(report) - 1)]
        min_diff, max_diff = min(diffs), max(diffs)
        if (0 < abs(max_diff) < 4) and (0 < abs(min_diff) < 4) and (max_diff * min_diff > 0):
            total_safe += 1
    return str(total_safe)


def part2(data:str) -> str:
    reports = listh(data, hsep=' ', element_transform=lambda x:int(x))
    total_safe = 0
    for report in reports:
        safe = False
        for i in range(0, len(report)):
            report_adjusted = report[:i] + report[i+1:]
            diffs = [report_adjusted[i+1]-report_adjusted[i] for i in range(0, len(report_adjusted) - 1)]
            min_diff, max_diff = min(diffs), max(diffs)
            if (0 < abs(max_diff) < 4) and (0 < abs(min_diff) < 4) and (max_diff * min_diff > 0):
                safe = True
        total_safe += 1 if safe else 0
    return str(total_safe)
