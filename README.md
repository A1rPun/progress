# progress

Simple progress indicator module written in python
[![asciicast](https://asciinema.org/a/ePEurSIHUzw2WSpXoaysTSTzv.png)](https://asciinema.org/a/ePEurSIHUzw2WSpXoaysTSTzv)

## Usage

### Import the module
```python
from progress import Progress
```

### Single string
```python
spin = Progress("0123456789")
print(spin.next()) # -> 0
print(spin.next()) # -> 1
print(spin.next()) # -> 2
```

### Array of strings
```python
spin = Progress([":|", ":P"])
print(spin.next()) # -> :|
print(spin.next()) # -> :P
print(spin.next()) # -> :|
```

## Pre-defined Spinners
```python
from progress import Progress, Spin

spin = Progress(Spin["pipe"])
print(spin.next()) # -> |
print(spin.next()) # -> /
print(spin.next()) # -> -
```

## Print on the same line
```python
def printSameLine(msg):
  print(msg, end="\r")
```

