# Click CLI Notes

## Installation

```bash
pip install click
```

## Basic Usage

```python
import click

@click.command()
def hello():
    click.echo('Hello World!')

if __name__ == '__main__':
    hello()
```

## Arguments

```python
import click

@click.command()
@click.argument('name')
def hello(name):
    click.echo(f'Hello {name}!')

if __name__ == '__main__':
    hello()
```

## Options

```python
import click

@click.command()
@click.option('--name', default='World')
def hello(name):
    click.echo(f'Hello {name}!')

if __name__ == '__main__':
    hello()
```

## Help Text

```python
import click

@click.command()
@click.option('--name', default='World', help='The person to greet.')
def hello(name):
    click.echo(f'Hello {name}!')

if __name__ == '__main__':
    hello()
```

## Type Conversion

```python
import click

@click.command()
@click.option('--count', default=1, type=int)
def hello(count):
    for _ in range(count):
        click.echo('Hello World!')

if __name__ == '__main__':
    hello()
```
