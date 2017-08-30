# progress

## Basics
```python
from progress import Progress

spin = Progress("0123456789")
print(spin.next()) # -> 0
print(spin.next()) # -> 1
print(spin.next()) # -> 2
```

## Spin
```python
from progress import Progress, Spin

spin = Progress(Spin.phases[0])
print(spin.next(), end="\r") # -> |
```
