import click
from bs4 import BeautifulSoup
import os
import shutil
from pathlib import Path

from globals import get_config, code_path
from download import load_from_config


@click.command()
@click.option('--year', default=None, help='Competition year. Example: 2024')
@click.option('--day', default=None, help='Competition day. Example: 1')
def init(year, day):
    """Load the problem, identify sample input and sample output."""
    kwargs = {}
    if not year is None:
        kwargs['year'] = year
    if not day is None:
        kwargs['day'] = day
    start_day(**kwargs)


def start_day(**kwargs) -> None:
    config = get_config(**kwargs)
    path = load_from_config(config)
    get_sample_from_problem(path)
    copy_template(config)


def get_sample_from_problem(path:str) -> None:
    with open((path / 'problem.html'), 'r') as f:
        html = f.read()

    candidates = get_sample_candidates(html)
    print_candidates(candidates)
    selections = select_candidates()
    for s in selections:
        save_selection(path, candidates, s)
    print('Ready to go.')


def get_sample_candidates(problem_html:str) -> list[str]:
    soup = BeautifulSoup(problem_html, features='html.parser')
    tags = soup.find_all('code')
    candidates = [t.text for t in tags]
    return candidates

def print_candidates(candidates:list[str]) -> None:
    for i, c in enumerate(candidates):
        print('----------------')
        print(f'{i}:')
        print(c)
        print('----------------')

def select_candidates() -> list[int]:
    selections = [{'prompt': 'Which candidate is the sample input?',  'file': 'input_sample.txt'},
                  {'prompt': 'Which candidate is the sample output?', 'file': 'output_sample.txt'}]
    for s in selections:
        s['choice'] = get_candidate(s['prompt'])
    return selections

def get_candidate(prompt:str) -> int:
    s = None
    while True:
        s = input(prompt + '    ')
        try:
            s = int(s.strip())
            break
        except:
            print('Not an integer, please try again')
    return s


def save_selection(path:str, candidates:list[str], s:dict) -> None:
    with open(path / s['file'], 'w') as f:
        f.write(candidates[s['choice']])


def copy_template(config) -> None:
    dest = code_path(config['year'], config['day'])
    src = Path(os.path.dirname(__file__)) / '__template.py'
    if not dest.exists():
        shutil.copy(str(src), str(dest))
    print(f'created {dest}')

if __name__ == '__main__':
    init()
