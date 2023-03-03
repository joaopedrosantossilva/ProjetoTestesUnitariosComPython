# ETA

## Relatorio dos testes
![image](https://user-images.githubusercontent.com/63526312/222855496-327c42b6-2969-4252-87f3-3397bba45f7a.png)


## Setup

```bash
pip install -r requirements.txt
```

## Unittest

```bash
python -m unittest -v
```

## Pytest

```bash
pytest .
```

## Test Coverage

- `coverage` and `pytest-cov` packages are required
- Add `pragma: no cover` to exclude code from coverage report

### With `pytest`

Terminal report:

 ```bash
pytest --cov-report term-missing --cov .
 ```

HTML report:

```bash
pytest --cov-report html --cov .
```

### With `unittest`

To generate report:

```bash
python -m coverage run -m unittest
```

To view report in terminal:

```bash
python -m coverage report
```

To view report in HTML:

```bash
python -m coverage html
```

