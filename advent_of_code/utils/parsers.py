from typing import Callable

def listv(data:str, vsep='\n', hsep=',', element_transform:Callable=None) -> list[list]:
    lists = listh(data, vsep, hsep)
    ret = list(map(list, zip(*lists)))
    if not element_transform is None:
        ret = [[element_transform(col) for col in row] for row in ret]
    return ret


def listh(data:str, vsep='\n', hsep=',', element_transform:Callable=None) -> list[list]:
    ret = [x.split(hsep) for x in data.split(vsep)]
    if not element_transform is None:
        ret = [[element_transform(col) for col in row] for row in ret]
    return ret
