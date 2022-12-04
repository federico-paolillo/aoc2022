# Advent of Code 2022 in Python

The exercises from [Advent of Code 2022](https://adventofcode.com/2022) solved in Python. Fun.

[![Continuous Integration](https://github.com/federico-paolillo/aoc2022/actions/workflows/ci.yml/badge.svg)](https://github.com/federico-paolillo/aoc2022/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/federico-paolillo/aoc2022/branch/main/graph/badge.svg?token=U9V6AVCF8T)](https://codecov.io/gh/federico-paolillo/aoc2022)

## Usage

Requires Python 3.11

There is one file for each day (`day_01.py`, `day_02.py`, etc...) with its corresponding unit test (`test_day_01.py`, `test_day_02.py`, etc...).

To run the project, execute its unit tests using `python3 -m unittest` from the repo root.

The project has no dependencies except for development tools like [`coverage.py`](https://coverage.readthedocs.io) and [`black`](https://github.com/psf/black).  
I manage my virtual env with [Pipenv](https://pipenv.pypa.io/en/latest/), if you have Pipenv installed just run `pipenv install` from the repo root to get the tools.

## Entries

- [Day One](docs/day_01.md)
- [Day Two](docs/day_02.md)
- [Day Three](docs/day_03.md)
- [Day Four](docs/day_04.md)
