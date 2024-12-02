import click
import importlib

from globals import get_config, data_path


@click.command()
@click.option('--part', default='1', type=click.Choice(['1', '2']), help='Problem part 1 or 2')
@click.option('--scope', default='both', type=click.Choice(['sample', 'actual', 'both'], case_sensitive=False))
@click.option('--strip/--no-strip', default=True)
def go(part, scope, strip):
    part = int(part)
    if scope in ['sample', 'both']:
        go_check(part, True, strip)
    if scope in ['actual', 'both']:
        go_check(part, False, strip)


def go_check(part:int, sample:bool, strip:bool) -> None:
    print(f'Part {part}, sample {sample}')
    config = get_config()
    module = importlib.import_module(f'advent_of_code.{config["year"]}.day{config["day"]}')
    method = getattr(module, f'part{part}')

    path = data_path(config["year"], config["day"])
    input_file = 'input_sample.txt' if sample else 'input.txt'
    with open(path / input_file, 'r') as f:
        input_text = f.read()
    if strip:
        input_text = input_text.strip()
    result = method(input_text)

    if sample:
        with open(path / 'output_sample.txt', 'r') as f:
            sample_result = f.read()
        
        print(f'"{result}" {"matches" if sample_result==result else "does not match"} sample "{sample_result}"')
    else:
        print(result)

if __name__ == '__main__':
    go()
