<div>
<img width="200" src="https://raw.githubusercontent.com/daanklijn/pydra/master/gifs/pydra1.gif">
<img width="200" src="https://raw.githubusercontent.com/daanklijn/pydra/master/gifs/pydra4.gif">
<img width="200"  src="https://raw.githubusercontent.com/daanklijn/pydra/master/gifs/pydra2.gif">
<img width="200"  src="https://raw.githubusercontent.com/daanklijn/pydra/master/gifs/pydra3.gif">
</div>


# Pydra, a visual synthesizer written in Python

Pydra (inspired by [Hydra](https://github.com/ojack/hydra)) is a visual synthesizer that is able to generate beautiful visual patterns. You have a wide range of functions available that interact with each other and will allow for endless posibilities. Below, a few examples are given to get you started. 

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

![](https://raw.githubusercontent.com/daanklijn/pydra/master/gifs/osc1.gif)

Also the period, speed and offset of the oscillator can be changed

```
osc(speed=0.2, period=50, offset=0).out()
```

![](https://raw.githubusercontent.com/daanklijn/pydra/master/gifs/osc3.gif)

Oscillators can be rotated


```
osc().rotate(degrees=45).out()
```

![](https://raw.githubusercontent.com/daanklijn/pydra/master/gifs/osc2.gif)


And added to other oscillators


```
osc().rotate().add(osc()).out()
```

![](https://raw.githubusercontent.com/daanklijn/pydra/master/gifs/osc4.gif)

Also subtraction and multiplication is possible

```
osc().rotate().diff(osc()).out()
```

![](https://raw.githubusercontent.com/daanklijn/pydra/master/gifs/osc5.gif)


```
osc().rotate().mult(osc()).out()
```

![](https://raw.githubusercontent.com/daanklijn/pydra/master/gifs/osc6.gif)

Furthermore, the position of certain pixels can be shifted based on the color of another oscillator using modulation

```
osc().modulate(osc().rotate()).out()
```

![](https://raw.githubusercontent.com/daanklijn/pydra/master/gifs/osc7.gif)

<!--- Chaining a couple of oscillators and functions together can result in amazing stuff --->

All functions can be found in [Pydra.py](https://github.com/daanklijn/pydra/blob/master/pydrasynth/Pydra.py)
