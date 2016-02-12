# hipy

Convert Ruby output of older Hiera versions to equivalent Python or JSON data structures.

## Usage

```bash
Usage: hipy [OPTIONS]

  Convert Hiera output to JSON/Python

Options:
  --json / --python  Format output as JSON/Python
  --debug            Show debug output (mainly from parser)
  --help             Show this message and exit.
```

## Examples

### Standalone CLI script


For more examples, look at the test examples.


### Library

```python
from hipy import parser

parser.get_json()
parser.get_python()
```

## Installing

### PyPI

Use `pip install hipy`.

### Locally

Run `python setup.py`.
