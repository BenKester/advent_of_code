from globals import data_path

def load(year:int, day:int) -> str:
    path = data_path(year, day)
    download = [
        {
            'url': fr'https://adventofcode.com/{year}/day/{day}',
            'out_file': path / 'problem.html'
        }
    ]

    for d in download:
        if not d['url'].exists():
            download_file(**d)

    return path



def download_file(url:str, out:str) -> None:
    pass


def get_agent_header() -> str:
    return 'https://github.com/BenKester/advent_of_code by kester.ben@gmail.com'


def manualDownloadFunction() -> None:
    raise NotImplementedError('function not implemented')

