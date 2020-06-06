```
osc().mult(osc().rotate(10)).modulate(osc(speed=0.5).rotate(130).add(osc().rotate(60))).out()

osc(0.25,150).modulate(osc().rotate()).highpass().modulate(osc(0.1,5).rotate(-45)).out()

osc(period=200).rotate().mult(osc(period=200)).rotate().mult(osc(period=200)).rotate().mult(osc(period=200)).out()

osc(0.1,140).rotate(-45).highpass().modulate(osc(0.05,40).rotate()).out()
osc().modulate().modulate(osc()).out()
```

![](https://raw.githubusercontent.com/daanklijn/pydra/master/gifs/pydra1.gif)
![](https://raw.githubusercontent.com/daanklijn/pydra/master/gifs/pydra4.gif)
![](https://raw.githubusercontent.com/daanklijn/pydra/master/gifs/pydra3.gif)
![](https://raw.githubusercontent.com/daanklijn/pydra/master/gifs/pydra2.gif)

