# Pydra, a visual synthesizer written in Python

`pip install pydrasynth`

Pydra (inspired by [Hydra](https://github.com/ojack/hydra)) is a visual synthesizer that is able to generate beautiful visual patterns. You have a wide range of functions available that interact with eachother and allows for endless posibilities. Below, a few examples are given to get you started. 

## Getting started

First, install the package using `pip`:

`pip install pydrasynth`

Import the package and initialize the display

```
from pydrasynth import init, osc
init(width=200,height=200)
```

## The oscillator and its functions

A simple oscillator can be created and displayed like this

```
osc().out()
```

Also the period, speed and offset of the oscillator can be changed

```
osc(speed=0.2, period=50, offset=0).out()
```

Oscillators can be rotated


```
osc().rotate(degrees=45).out()
```

And added to other oscillators


```
osc().rotate(degrees=45).add(osc()).out()
```

Also subtraction and multiplication is possible

```
osc().rotate(degrees=45).diff(osc()).out()
```

```
osc().rotate(degrees=45).mult(osc()).out()
```

Furthermore, the position of certain pixels can be shifted based on the color of another oscillator using modulation:

```
osc().modulate(degrees=45).modulate(osc()).out()
```

Chaining a couple of oscillators and functions together can result in amazing stuff:

All functions can be found in [Pydra.py](https://github.com/daanklijn/pydra/blob/master/pydrasynth/Pydra.py)
