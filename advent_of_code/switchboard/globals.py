from pathlib import Path
import os
import json
from typing import Union

def data_path(year:Union[str, int]=None, day:Union[str, int]=None) -> Path:
    ret = Path(os.path.dirname(__file__)).parent.parent / 'data'
    if not year is None:
        ret = ret / str(year)
        if not day is None:
            ret = ret / str(day)
    else:
        if not day is None:
            raise ValueError('must provide year if day is provided')

    ret.mkdir(parents=True, exist_ok=True)
    return ret

def code_path(year:Union[str, int]=None, day:Union[str, int]=None) -> Path:
    return Path(os.path.dirname(__file__)).parent / str(year) / f'day{day}.py'

def get_config(**overrides):
    path = Path(os.path.dirname(__file__)) / 'config.json'
    if path.exists():
        with open(path, 'r') as f:
            config = json.load(f)
    else:
        config = {}

    config.update(overrides)
    with open(path, 'w') as f:
        json.dump(config, f)

    return config
