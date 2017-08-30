# progress
```python
from progress import Progress, Spin

spin = Progress(Spin.phases[0])
print(spin.next(), end="\r")
```
