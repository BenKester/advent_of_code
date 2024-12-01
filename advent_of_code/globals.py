from pathlib import Path
import os

def data_path(year:int=None, day:int=None) -> Path:
    ret = Path(os.path.dirname(__file__)).parent / 'data'
    if not year is None:
        ret = ret / str(year)
        if not day is None:
            ret = ret / str(day)
    else:
        if not day is None:
            raise ValueError('must provide year if day is provided')

    ret.mkdir(parents=True, exist_ok=True)
    return ret

