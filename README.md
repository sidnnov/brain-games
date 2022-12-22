### Hexlet tests and linter status:
[![Actions Status](https://github.com/sidnnov/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/sidnnov/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/eee64bcfeffb6b6b3b78/maintainability)](https://codeclimate.com/github/sidnnov/python-project-49/maintainability)

### A little about the project:
-------------------------------
This is the educational project of the 1st module, the training program for Nehlet, the Python developer profession. Contains five games with similar logic.

### Install hexlet-code
-----------------------

python 3.8+ is required to install hexlet-code. And also need poetry for the assembly of the project.

```
$ poetry build

$ python3 -m pip install --user dist/*.whl
```

#### Description of the Make commands:
```
install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

reinstall:
	pip install --user --force-reinstall dist/*.whl

lint: 
	poetry run flake8 brain_games
```

#### Running games:
```
$ brain-even

$ brain-calc

$ brain-gcd

$ brain-progression

$ brain-prime
```

#### Setup example:
[![asciicast](https://asciinema.org/a/aJabawAlJeIfCBinHn2CEEnvy.svg)](https://asciinema.org/a/aJabawAlJeIfCBinHn2CEEnvy)


#### My examples of games:
Parity check game 🡾
[![asciicast](https://asciinema.org/a/PU3ygUfzV1zHpvycDfAkFhJBh.svg)](https://asciinema.org/a/PU3ygUfzV1zHpvycDfAkFhJBh)

Calculator game 🡾
[![asciicast](https://asciinema.org/a/vsGOAlBm8wzR1Yp2S3dyFweHA.svg)](https://asciinema.org/a/vsGOAlBm8wzR1Yp2S3dyFweHA)

Greatest common divisor 🡾
[![asciicast](https://asciinema.org/a/RnwTUZT66G4HWKQFGjD48OUfZ.svg)](https://asciinema.org/a/RnwTUZT66G4HWKQFGjD48OUfZ)

Arithmetic progression 🡾
[![asciicast](https://asciinema.org/a/6RZBHIS8RiZQt571pI2YuoTWL.svg)](https://asciinema.org/a/6RZBHIS8RiZQt571pI2YuoTWL)

Is it a prime number? 🡾
[![asciicast](https://asciinema.org/a/xqEDDEIMOHi0d4Ptys2yVLVs6.svg)](https://asciinema.org/a/xqEDDEIMOHi0d4Ptys2yVLVs6)
