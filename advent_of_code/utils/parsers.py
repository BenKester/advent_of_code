from typing import Callable

def listv(input:str, vsep='\n', hsep=',', element_transform:Callable=None) -> list[list]:
    lists = listh(input, vsep, hsep)
    ret = list(map(list, zip(*lists)))
    if not element_transform is None:
        ret = [[element_transform(col) for col in row] for row in ret]
    return ret


def listh(input:str, vsep='\n', hsep=',') -> list[list]:
    return [x.split(hsep) for x in input.split(vsep)]
