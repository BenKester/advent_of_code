import requests
from typing import Union
from aocd import get_data

from globals import data_path


def load_from_config(config:dict) -> str:
    return load(config['year'], config['day'])


def load(year:Union[str, int], day:Union[str, int]) -> str:
    path = data_path(year, day)
    d = {
            'url': fr'https://adventofcode.com/{year}/day/{day}',
            'out_path': path / 'problem.html'
    }

    if not d['out_path'].exists():
        download_file(**d)

    input_path = path / 'input.txt'
    if not (input_path).exists():
        with open(input_path, 'w') as f:
            f.write(get_data(day=day, year=year))
        print(f'downloaded {input_path}')

    return path


def download_file(url:str, out_path:str) -> None:
    packet = requests.get(url, headers={'User-agent': get_agent_header()})
    with open(out_path, 'w') as f:
        f.write(packet.text)
    print(f'downloaded {out_path}')


def get_agent_header() -> str:
    return 'https://github.com/BenKester/advent_of_code by kester.ben@gmail.com'


def manualDownloadFunction() -> None:
    raise NotImplementedError('function not implemented')

