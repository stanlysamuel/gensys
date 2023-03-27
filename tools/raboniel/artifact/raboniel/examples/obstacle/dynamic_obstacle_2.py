import json
import readline

def run(init, inputs):
  state = 0
  x = init['x']
  y = init['y']
  oldax = init['oldax']
  olday = init['olday']
  for _input in inputs:
    ax = _input['ax']
    ay = _input['ay']
    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and (x + 1) == ax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and (x - 1) == ax and (y + 1) == ay)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and (y + 1) == ay)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and (x + 1) == ax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and y == olday and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and (x + 1) == ax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 0 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 0 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and (x + 1) == ax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and (x - 1) == ax and (y + 1) == ay)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and (y + 1) == ay)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 4
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and (x + 1) == ax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 4
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and y == olday and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 4
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and (x + 1) == ax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 1 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 1 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and (x + 1) == ax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and (x - 1) == ax and (y + 1) == ay)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and (y + 1) == ay)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and (x + 1) == ax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and y == olday and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and (x + 1) == ax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 2 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 2 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and (x + 1) == ax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 3 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and (x - 1) == ax and (y + 1) == ay)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and (y + 1) == ay)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and (x + 1) == ax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and y == olday and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and (x + 1) == ax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 3 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 3 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and (x + 1) == ax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and (x - 1) == ax and (y + 1) == ay)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and (y + 1) == ay)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 4 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and (x + 1) == ax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and x == oldax)):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and not (y == ay) and y == olday and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and (x + 1) == ax and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and (((y - 1) == ay and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 2
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == ay and not (y == olday) and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and not ((y + 1) == ay) and not ((x + 1) == ax) and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and not (x == oldax))):
      state_prime = 3
      olday_prime = ay
      y_prime = y
      oldax_prime = ax
      x_prime = (x + 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and (x + 1) == ax and y == olday and not (x == ax) and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and not (y == olday) and not (x == ax) and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y + 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and x == ax and x == oldax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and y == ay and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and (x + 1) == ax)):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = (x - 1)

    if state == 4 and ((not ((y - 1) == ay) and (x - 1) == ax and (y + 1) == ay and not ((x + 1) == ax) and y == ay and not (y == olday) and x == ax and not (x == oldax))):
      state_prime = 1
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    if state == 4 and (((y - 1) == ay and not ((x - 1) == ax) and not ((y + 1) == ay) and not ((x + 1) == ax) and not (y == ay) and y == olday and not (x == ax) and not (x == oldax))):
      state_prime = 4
      olday_prime = ay
      y_prime = (y - 1)
      oldax_prime = ax
      x_prime = x

    state = state_prime
    x = x_prime
    y = y_prime
    oldax = oldax_prime
    olday = olday_prime
    yield {'x':x, 'y':y, 'oldax':oldax, 'olday':olday}


def main():
  def readInputs():
    while True:
      raw = input("inputs: ")
      if raw == "exit":
        break
      yield json.loads(raw)

  inputs = readInputs()
  raw = input("initial state: ")
  init = json.loads(raw)
  outputs = run(init, inputs)
  for o in outputs:
    print("state: ", o)
    print("-----")

if __name__ == "__main__":
    main()

