import json
import readline

def run(init, inputs):
  state = 0
  x = init['x']
  y = init['y']
  ax = init['ax']
  ay = init['ay']
  for _input in inputs:
    dax = _input['dax']
    day = _input['day']
    if state == 0 and ((day == -1 and not (day == 0) and not (day == 1) and not (dax == -1) and dax == 0 and not (dax == 1) and not (y == ay) and x == ax)):
      state_prime = 2
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x + 1)

    if state == 0 and ((not (day == -1) and day == 0 and not (day == 1) and dax == -1 and not (dax == 0) and not (dax == 1) and y == ay and x == ax)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 0 and ((not (day == -1) and not (day == 0) and not (day == 1))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 0 and ((not (day == -1) and day == 0 and not (day == 1) and not (dax == -1) and not (dax == 0) and dax == 1 and not (y == ay) and x == ax)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x + 1)

    if state == 0 and ((not (day == -1) and not (day == 0) and day == 1 and not (dax == -1) and dax == 0 and not (dax == 1) and not (y == ay) and x == ax)):
      state_prime = 2
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x + 1)

    if state == 0 and ((not (day == -1) and day == 0 and not (day == 1) and dax == -1 and not (dax == 0) and dax == 1)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 0 and ((not (day == -1) and day == 0 and not (day == 1) and not (dax == -1) and dax == 0)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 0 and ((not (day == -1) and not (day == 0) and day == 1 and not (dax == -1) and not (dax == 0))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 0 and ((not (day == -1) and day == 0 and not (day == 1) and not (dax == -1) and not (dax == 0) and dax == 1 and not (y == ay) and not (x == ax))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x + 1)

    if state == 0 and ((not (day == -1) and day == 0 and not (day == 1) and not (dax == -1) and not (dax == 0) and dax == 1 and y == ay and x == ax)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 0 and ((not (day == -1) and not (day == 0) and day == 1 and not (dax == -1) and dax == 0 and not (dax == 1) and y == ay and x == ax)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 0 and ((not (day == -1) and not (day == 0) and day == 1 and dax == -1)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 0 and ((day == -1 and day == 0)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 0 and ((not (day == -1) and day == 0 and not (day == 1) and dax == -1 and dax == 0)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 0 and ((day == -1 and not (day == 0) and not (day == 1) and not (dax == -1) and not (dax == 0))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 0 and ((day == -1 and not (day == 0) and not (day == 1) and not (dax == -1) and dax == 0 and not (dax == 1) and y == ay and x == ax)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 0 and ((day == -1 and not (day == 0) and not (day == 1) and not (dax == -1) and dax == 0 and dax == 1)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 0 and ((day == -1 and not (day == 0) and not (day == 1) and not (dax == -1) and dax == 0 and not (dax == 1) and not (y == ay) and not (x == ax))):
      state_prime = 0
      ay_prime = (ay + day)
      y_prime = (y + 1)
      ax_prime = (ax + dax)
      x_prime = x

    if state == 0 and ((not (day == -1) and day == 0 and day == 1)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 0 and ((day == -1 and not (day == 0) and not (day == 1) and dax == -1)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 0 and ((day == -1 and not (day == 0) and day == 1)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 0 and ((not (day == -1) and day == 0 and not (day == 1) and not (dax == -1) and not (dax == 0) and not (dax == 1))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 0 and ((not (day == -1) and day == 0 and not (day == 1) and dax == -1 and not (dax == 0) and not (dax == 1) and not (y == ay) and not (x == ax))):
      state_prime = 2
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x + 1)

    if state == 0 and ((not (day == -1) and not (day == 0) and day == 1 and not (dax == -1) and dax == 0 and not (dax == 1) and not (y == ay) and not (x == ax))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y + 1)
      ax_prime = (ax + dax)
      x_prime = x

    if state == 0 and ((not (day == -1) and day == 0 and not (day == 1) and dax == -1 and not (dax == 0) and not (dax == 1) and y == ay and not (x == ax))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 0 and ((day == -1 and not (day == 0) and not (day == 1) and not (dax == -1) and dax == 0 and not (dax == 1) and y == ay and not (x == ax))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x + 1)

    if state == 0 and ((not (day == -1) and not (day == 0) and day == 1 and not (dax == -1) and dax == 0 and dax == 1)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 0 and ((not (day == -1) and day == 0 and not (day == 1) and not (dax == -1) and not (dax == 0) and dax == 1 and y == ay and not (x == ax))):
      state_prime = 2
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x + 1)

    if state == 0 and ((not (day == -1) and not (day == 0) and day == 1 and not (dax == -1) and dax == 0 and not (dax == 1) and y == ay and not (x == ax))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x + 1)

    if state == 0 and ((not (day == -1) and day == 0 and not (day == 1) and dax == -1 and not (dax == 0) and not (dax == 1) and not (y == ay) and x == ax)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x + 1)

    if state == 1 and ((day == -1 and not (day == 0) and not (day == 1) and not (dax == -1) and dax == 0 and not (dax == 1) and not (y == ay) and x == ax)):
      state_prime = 2
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x + 1)

    if state == 1 and ((not (day == -1) and day == 0 and not (day == 1) and dax == -1 and not (dax == 0) and not (dax == 1) and y == ay and x == ax)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 1 and ((not (day == -1) and not (day == 0) and not (day == 1))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 1 and ((not (day == -1) and day == 0 and not (day == 1) and not (dax == -1) and not (dax == 0) and dax == 1 and not (y == ay) and x == ax)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x + 1)

    if state == 1 and ((not (day == -1) and not (day == 0) and day == 1 and not (dax == -1) and dax == 0 and not (dax == 1) and not (y == ay) and x == ax)):
      state_prime = 2
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x + 1)

    if state == 1 and ((not (day == -1) and day == 0 and not (day == 1) and dax == -1 and not (dax == 0) and dax == 1)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 1 and ((not (day == -1) and day == 0 and not (day == 1) and not (dax == -1) and dax == 0)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 1 and ((not (day == -1) and not (day == 0) and day == 1 and not (dax == -1) and not (dax == 0))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 1 and ((not (day == -1) and day == 0 and not (day == 1) and not (dax == -1) and not (dax == 0) and dax == 1 and not (y == ay) and not (x == ax))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x + 1)

    if state == 1 and ((not (day == -1) and day == 0 and not (day == 1) and not (dax == -1) and not (dax == 0) and dax == 1 and y == ay and x == ax)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 1 and ((not (day == -1) and not (day == 0) and day == 1 and not (dax == -1) and dax == 0 and not (dax == 1) and y == ay and x == ax)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 1 and ((not (day == -1) and not (day == 0) and day == 1 and dax == -1)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 1 and ((day == -1 and day == 0)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 1 and ((not (day == -1) and day == 0 and not (day == 1) and dax == -1 and dax == 0)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 1 and ((day == -1 and not (day == 0) and not (day == 1) and not (dax == -1) and not (dax == 0))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 1 and ((day == -1 and not (day == 0) and not (day == 1) and not (dax == -1) and dax == 0 and not (dax == 1) and y == ay and x == ax)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 1 and ((day == -1 and not (day == 0) and not (day == 1) and not (dax == -1) and dax == 0 and dax == 1)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 1 and ((day == -1 and not (day == 0) and not (day == 1) and not (dax == -1) and dax == 0 and not (dax == 1) and not (y == ay) and not (x == ax))):
      state_prime = 0
      ay_prime = (ay + day)
      y_prime = (y + 1)
      ax_prime = (ax + dax)
      x_prime = x

    if state == 1 and ((not (day == -1) and day == 0 and day == 1)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 1 and ((day == -1 and not (day == 0) and not (day == 1) and dax == -1)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 1 and ((day == -1 and not (day == 0) and day == 1)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 1 and ((not (day == -1) and day == 0 and not (day == 1) and not (dax == -1) and not (dax == 0) and not (dax == 1))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 1 and ((not (day == -1) and day == 0 and not (day == 1) and dax == -1 and not (dax == 0) and not (dax == 1) and not (y == ay) and not (x == ax))):
      state_prime = 2
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x + 1)

    if state == 1 and ((not (day == -1) and not (day == 0) and day == 1 and not (dax == -1) and dax == 0 and not (dax == 1) and not (y == ay) and not (x == ax))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y + 1)
      ax_prime = (ax + dax)
      x_prime = x

    if state == 1 and ((not (day == -1) and day == 0 and not (day == 1) and dax == -1 and not (dax == 0) and not (dax == 1) and y == ay and not (x == ax))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 1 and ((day == -1 and not (day == 0) and not (day == 1) and not (dax == -1) and dax == 0 and not (dax == 1) and y == ay and not (x == ax))):
      state_prime = 0
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = x

    if state == 1 and ((not (day == -1) and not (day == 0) and day == 1 and not (dax == -1) and dax == 0 and dax == 1)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 1 and ((not (day == -1) and day == 0 and not (day == 1) and not (dax == -1) and not (dax == 0) and dax == 1 and y == ay and not (x == ax))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y + 1)
      ax_prime = (ax + dax)
      x_prime = x

    if state == 1 and ((not (day == -1) and not (day == 0) and day == 1 and not (dax == -1) and dax == 0 and not (dax == 1) and y == ay and not (x == ax))):
      state_prime = 0
      ay_prime = (ay + day)
      y_prime = (y + 1)
      ax_prime = (ax + dax)
      x_prime = x

    if state == 1 and ((not (day == -1) and day == 0 and not (day == 1) and dax == -1 and not (dax == 0) and not (dax == 1) and not (y == ay) and x == ax)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x + 1)

    if state == 2 and ((day == -1 and not (day == 0) and not (day == 1) and not (dax == -1) and dax == 0 and not (dax == 1) and not (y == ay) and x == ax)):
      state_prime = 2
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x + 1)

    if state == 2 and ((not (day == -1) and day == 0 and not (day == 1) and dax == -1 and not (dax == 0) and not (dax == 1) and y == ay and x == ax)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 2 and ((not (day == -1) and not (day == 0) and not (day == 1))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 2 and ((not (day == -1) and day == 0 and not (day == 1) and not (dax == -1) and not (dax == 0) and dax == 1 and not (y == ay) and x == ax)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x + 1)

    if state == 2 and ((not (day == -1) and not (day == 0) and day == 1 and not (dax == -1) and dax == 0 and not (dax == 1) and not (y == ay) and x == ax)):
      state_prime = 2
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x + 1)

    if state == 2 and ((not (day == -1) and day == 0 and not (day == 1) and dax == -1 and not (dax == 0) and dax == 1)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 2 and ((not (day == -1) and day == 0 and not (day == 1) and not (dax == -1) and dax == 0)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 2 and ((not (day == -1) and not (day == 0) and day == 1 and not (dax == -1) and not (dax == 0))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 2 and ((not (day == -1) and day == 0 and not (day == 1) and not (dax == -1) and not (dax == 0) and dax == 1 and not (y == ay) and not (x == ax))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x + 1)

    if state == 2 and ((not (day == -1) and day == 0 and not (day == 1) and not (dax == -1) and not (dax == 0) and dax == 1 and y == ay and x == ax)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 2 and ((not (day == -1) and not (day == 0) and day == 1 and not (dax == -1) and dax == 0 and not (dax == 1) and y == ay and x == ax)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 2 and ((not (day == -1) and not (day == 0) and day == 1 and dax == -1)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 2 and ((day == -1 and day == 0)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 2 and ((not (day == -1) and day == 0 and not (day == 1) and dax == -1 and dax == 0)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 2 and ((day == -1 and not (day == 0) and not (day == 1) and not (dax == -1) and not (dax == 0))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 2 and ((day == -1 and not (day == 0) and not (day == 1) and not (dax == -1) and dax == 0 and not (dax == 1) and y == ay and x == ax)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 2 and ((day == -1 and not (day == 0) and not (day == 1) and not (dax == -1) and dax == 0 and dax == 1)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 2 and ((day == -1 and not (day == 0) and not (day == 1) and not (dax == -1) and dax == 0 and not (dax == 1) and not (y == ay) and not (x == ax))):
      state_prime = 0
      ay_prime = (ay + day)
      y_prime = (y + 1)
      ax_prime = (ax + dax)
      x_prime = x

    if state == 2 and ((not (day == -1) and day == 0 and day == 1)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 2 and ((day == -1 and not (day == 0) and not (day == 1) and dax == -1)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 2 and ((day == -1 and not (day == 0) and day == 1)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 2 and ((not (day == -1) and day == 0 and not (day == 1) and not (dax == -1) and not (dax == 0) and not (dax == 1))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 2 and ((not (day == -1) and day == 0 and not (day == 1) and dax == -1 and not (dax == 0) and not (dax == 1) and not (y == ay) and not (x == ax))):
      state_prime = 2
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x + 1)

    if state == 2 and ((not (day == -1) and not (day == 0) and day == 1 and not (dax == -1) and dax == 0 and not (dax == 1) and not (y == ay) and not (x == ax))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y + 1)
      ax_prime = (ax + dax)
      x_prime = x

    if state == 2 and ((not (day == -1) and day == 0 and not (day == 1) and dax == -1 and not (dax == 0) and not (dax == 1) and y == ay and not (x == ax))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y + 1)
      ax_prime = (ax + dax)
      x_prime = x

    if state == 2 and ((day == -1 and not (day == 0) and not (day == 1) and not (dax == -1) and dax == 0 and not (dax == 1) and y == ay and not (x == ax))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x + 1)

    if state == 2 and ((not (day == -1) and not (day == 0) and day == 1 and not (dax == -1) and dax == 0 and dax == 1)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = (y - 1)
      ax_prime = (ax + dax)
      x_prime = (x - 1)

    if state == 2 and ((not (day == -1) and day == 0 and not (day == 1) and not (dax == -1) and not (dax == 0) and dax == 1 and y == ay and not (x == ax))):
      state_prime = 2
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x + 1)

    if state == 2 and ((not (day == -1) and not (day == 0) and day == 1 and not (dax == -1) and dax == 0 and not (dax == 1) and y == ay and not (x == ax))):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x + 1)

    if state == 2 and ((not (day == -1) and day == 0 and not (day == 1) and dax == -1 and not (dax == 0) and not (dax == 1) and not (y == ay) and x == ax)):
      state_prime = 1
      ay_prime = (ay + day)
      y_prime = y
      ax_prime = (ax + dax)
      x_prime = (x + 1)

    state = state_prime
    x = x_prime
    y = y_prime
    ax = ax_prime
    ay = ay_prime
    yield {'x':x, 'y':y, 'ax':ax, 'ay':ay}


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

