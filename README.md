# hipy

Convert Ruby output of older Hiera versions to equivalent Python or JSON data structures.

## Usage

```bash
Usage: hipy [OPTIONS]

  Convert Hiera output to JSON/Python

Options:
  --json / --python  Format output as JSON/Python (default: JSON)
  --debug            Show debug output (mainly from parser)
  --help             Show this message and exit.
```

## Examples

### Standalone CLI script

```bash
$ echo nil | hipy
null
$ echo nil | hipy --json
null
$ echo nil | hipy --python
None
$ echo nil | hipy --python --debug
In: nil
<Node called "nil" matching "nil">
Out: None
```


For more examples (and possible limitations), cf. the test examples.


### Library

```python
>>> from hipy.parser import HieraOutputParser
>>> parser = HieraOutputParser(text='nil')

>>> parser.get_json()
'null'

>>> parser.get_python() is None
True

>>> parser = HieraOutputParser(text='nil', debug=True)
<Node called "nil" matching "nil">
```

## Tests

Run `python setup.py nosetests`.

## Installation

### PyPI

Use `pip install hipy` (WIP).

### Locally

Run `python setup.py install`.
