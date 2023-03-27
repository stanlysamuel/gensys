import json
import readline

def run(init, inputs):
  state = 0
  x = init['x']
  y = init['y']
  size = init['size']
  for _input in inputs:
    if state == 0 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and not ((y - 1) >= 0) and (x - 1) >= 0 and y >= 0 and size >= 10 and x >= 0)):
      state_prime = 1
      y_prime = (y + 1)
      size_prime = size
      x_prime = x

    if state == 0 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and not ((y - 1) >= 0) and not ((x - 1) >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and (((y + 1) <= size and (x + 1) <= size and y <= size and x <= size and not (y >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and (((y + 1) <= size and (x + 1) <= size and y <= size and not (x <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and y >= 0 and size >= 10 and not (x >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and ((not ((y + 1) <= size) and (x + 1) <= size and y <= size and x <= size and (y - 1) >= 0 and y >= 0 and not (size >= 10))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and ((not ((y + 1) <= size) and (x + 1) <= size and y <= size and not (x <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and not (y >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and ((not ((y + 1) <= size) and (x + 1) <= size and y <= size and x <= size and not ((y - 1) >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and not ((x - 1) >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and ((not ((y + 1) <= size) and (x + 1) <= size and y <= size and x <= size and (y - 1) >= 0 and not (y >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and x <= size and not ((y - 1) >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and not (y >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and y >= 0 and not (size >= 10))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and not ((y - 1) >= 0) and (x - 1) >= 0 and not (y >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and not ((y - 1) >= 0) and (x - 1) >= 0 and y >= 0 and not (size >= 10))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and y >= 0 and size >= 10 and not (x >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and ((not ((y + 1) <= size) and (x + 1) <= size and y <= size and x <= size and (y - 1) >= 0 and y >= 0 and size >= 10 and not (x >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and ((not ((y + 1) <= size) and (x + 1) <= size and not (y <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and not (x <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and (((y + 1) <= size and (x + 1) <= size and y <= size and x <= size and y >= 0 and size >= 10 and not (x >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and not (y <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and y >= 0 and not (size >= 10))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and (((y + 1) <= size and not ((x + 1) <= size) and not (y <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and (((y + 1) <= size and (x + 1) <= size and y <= size and x <= size and y >= 0 and not (size >= 10))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and ((not ((y + 1) <= size) and (x + 1) <= size and y <= size and x <= size and (y - 1) >= 0 and y >= 0 and size >= 10 and x >= 0)):
      state_prime = 0
      y_prime = y
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and (((y + 1) <= size and (x + 1) <= size and y <= size and x <= size and y >= 0 and size >= 10 and x >= 0)):
      state_prime = 0
      y_prime = y
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and not (x <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and y >= 0 and size >= 10 and x >= 0)):
      state_prime = 1
      y_prime = (y + 1)
      size_prime = size
      x_prime = x

    if state == 0 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and not ((y - 1) >= 0) and (x - 1) >= 0 and y >= 0 and size >= 10 and not (x >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and y >= 0 and size >= 10 and x >= 0)):
      state_prime = 2
      y_prime = (y - 1)
      size_prime = size
      x_prime = x

    if state == 0 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and not ((x - 1) >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and (((y + 1) <= size and (x + 1) <= size and not (y <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and not ((y - 1) >= 0) and (x - 1) >= 0 and y >= 0 and size >= 10 and x >= 0)):
      state_prime = 1
      y_prime = (y + 1)
      size_prime = size
      x_prime = x

    if state == 1 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and not ((y - 1) >= 0) and not ((x - 1) >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and (((y + 1) <= size and (x + 1) <= size and y <= size and x <= size and not (y >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and (((y + 1) <= size and (x + 1) <= size and y <= size and not (x <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and y >= 0 and size >= 10 and not (x >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and ((not ((y + 1) <= size) and (x + 1) <= size and y <= size and x <= size and (y - 1) >= 0 and y >= 0 and not (size >= 10))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and ((not ((y + 1) <= size) and (x + 1) <= size and y <= size and not (x <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and not (y >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and ((not ((y + 1) <= size) and (x + 1) <= size and y <= size and x <= size and not ((y - 1) >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and not ((x - 1) >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and ((not ((y + 1) <= size) and (x + 1) <= size and y <= size and x <= size and (y - 1) >= 0 and not (y >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and x <= size and not ((y - 1) >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and not (y >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and y >= 0 and not (size >= 10))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and not ((y - 1) >= 0) and (x - 1) >= 0 and not (y >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and not ((y - 1) >= 0) and (x - 1) >= 0 and y >= 0 and not (size >= 10))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and y >= 0 and size >= 10 and not (x >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and ((not ((y + 1) <= size) and (x + 1) <= size and y <= size and x <= size and (y - 1) >= 0 and y >= 0 and size >= 10 and not (x >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and ((not ((y + 1) <= size) and (x + 1) <= size and not (y <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and not (x <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and (((y + 1) <= size and (x + 1) <= size and y <= size and x <= size and y >= 0 and size >= 10 and not (x >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and not (y <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and y >= 0 and not (size >= 10))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and (((y + 1) <= size and not ((x + 1) <= size) and not (y <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and (((y + 1) <= size and (x + 1) <= size and y <= size and x <= size and y >= 0 and not (size >= 10))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and ((not ((y + 1) <= size) and (x + 1) <= size and y <= size and x <= size and (y - 1) >= 0 and y >= 0 and size >= 10 and x >= 0)):
      state_prime = 0
      y_prime = y
      size_prime = size
      x_prime = (x + 1)

    if state == 1 and (((y + 1) <= size and (x + 1) <= size and y <= size and x <= size and y >= 0 and size >= 10 and x >= 0)):
      state_prime = 0
      y_prime = y
      size_prime = size
      x_prime = (x + 1)

    if state == 1 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and not (x <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and y >= 0 and size >= 10 and x >= 0)):
      state_prime = 1
      y_prime = (y + 1)
      size_prime = size
      x_prime = x

    if state == 1 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and not ((y - 1) >= 0) and (x - 1) >= 0 and y >= 0 and size >= 10 and not (x >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and y >= 0 and size >= 10 and x >= 0)):
      state_prime = 3
      y_prime = y
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and not ((x - 1) >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 1 and (((y + 1) <= size and (x + 1) <= size and not (y <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and not ((y - 1) >= 0) and (x - 1) >= 0 and y >= 0 and size >= 10 and x >= 0)):
      state_prime = 3
      y_prime = y
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and not ((y - 1) >= 0) and not ((x - 1) >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and (((y + 1) <= size and (x + 1) <= size and y <= size and x <= size and not (y >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and (((y + 1) <= size and (x + 1) <= size and y <= size and not (x <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and y >= 0 and size >= 10 and not (x >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and ((not ((y + 1) <= size) and (x + 1) <= size and y <= size and x <= size and (y - 1) >= 0 and y >= 0 and not (size >= 10))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and ((not ((y + 1) <= size) and (x + 1) <= size and y <= size and not (x <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and not (y >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and ((not ((y + 1) <= size) and (x + 1) <= size and y <= size and x <= size and not ((y - 1) >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and not ((x - 1) >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and ((not ((y + 1) <= size) and (x + 1) <= size and y <= size and x <= size and (y - 1) >= 0 and not (y >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and x <= size and not ((y - 1) >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and not (y >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and y >= 0 and not (size >= 10))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and not ((y - 1) >= 0) and (x - 1) >= 0 and not (y >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and not ((y - 1) >= 0) and (x - 1) >= 0 and y >= 0 and not (size >= 10))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and y >= 0 and size >= 10 and not (x >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and ((not ((y + 1) <= size) and (x + 1) <= size and y <= size and x <= size and (y - 1) >= 0 and y >= 0 and size >= 10 and not (x >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and ((not ((y + 1) <= size) and (x + 1) <= size and not (y <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and not (x <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and (((y + 1) <= size and (x + 1) <= size and y <= size and x <= size and y >= 0 and size >= 10 and not (x >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and not (y <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and y >= 0 and not (size >= 10))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and (((y + 1) <= size and not ((x + 1) <= size) and not (y <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and (((y + 1) <= size and (x + 1) <= size and y <= size and x <= size and y >= 0 and not (size >= 10))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and ((not ((y + 1) <= size) and (x + 1) <= size and y <= size and x <= size and (y - 1) >= 0 and y >= 0 and size >= 10 and x >= 0)):
      state_prime = 0
      y_prime = y
      size_prime = size
      x_prime = (x + 1)

    if state == 2 and (((y + 1) <= size and (x + 1) <= size and y <= size and x <= size and y >= 0 and size >= 10 and x >= 0)):
      state_prime = 0
      y_prime = y
      size_prime = size
      x_prime = (x + 1)

    if state == 2 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and not (x <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and y >= 0 and size >= 10 and x >= 0)):
      state_prime = 2
      y_prime = (y - 1)
      size_prime = size
      x_prime = x

    if state == 2 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and not ((y - 1) >= 0) and (x - 1) >= 0 and y >= 0 and size >= 10 and not (x >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and y >= 0 and size >= 10 and x >= 0)):
      state_prime = 2
      y_prime = (y - 1)
      size_prime = size
      x_prime = x

    if state == 2 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and not ((x - 1) >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 2 and (((y + 1) <= size and (x + 1) <= size and not (y <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and not ((y - 1) >= 0) and (x - 1) >= 0 and y >= 0 and size >= 10 and x >= 0)):
      state_prime = 1
      y_prime = (y + 1)
      size_prime = size
      x_prime = x

    if state == 3 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and not ((y - 1) >= 0) and not ((x - 1) >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and (((y + 1) <= size and (x + 1) <= size and y <= size and x <= size and not (y >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and (((y + 1) <= size and (x + 1) <= size and y <= size and not (x <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and y >= 0 and size >= 10 and not (x >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and ((not ((y + 1) <= size) and (x + 1) <= size and y <= size and x <= size and (y - 1) >= 0 and y >= 0 and not (size >= 10))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and ((not ((y + 1) <= size) and (x + 1) <= size and y <= size and not (x <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and not (y >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and ((not ((y + 1) <= size) and (x + 1) <= size and y <= size and x <= size and not ((y - 1) >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and not ((x - 1) >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and ((not ((y + 1) <= size) and (x + 1) <= size and y <= size and x <= size and (y - 1) >= 0 and not (y >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and x <= size and not ((y - 1) >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and not (y >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and y >= 0 and not (size >= 10))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and not ((y - 1) >= 0) and (x - 1) >= 0 and not (y >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and not ((y - 1) >= 0) and (x - 1) >= 0 and y >= 0 and not (size >= 10))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and y >= 0 and size >= 10 and not (x >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and ((not ((y + 1) <= size) and (x + 1) <= size and y <= size and x <= size and (y - 1) >= 0 and y >= 0 and size >= 10 and not (x >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and ((not ((y + 1) <= size) and (x + 1) <= size and not (y <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and not (x <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and (((y + 1) <= size and (x + 1) <= size and y <= size and x <= size and y >= 0 and size >= 10 and not (x >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and not (y <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and y >= 0 and not (size >= 10))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and (((y + 1) <= size and not ((x + 1) <= size) and not (y <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and (((y + 1) <= size and (x + 1) <= size and y <= size and x <= size and y >= 0 and not (size >= 10))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and ((not ((y + 1) <= size) and (x + 1) <= size and y <= size and x <= size and (y - 1) >= 0 and y >= 0 and size >= 10 and x >= 0)):
      state_prime = 2
      y_prime = (y - 1)
      size_prime = size
      x_prime = x

    if state == 3 and (((y + 1) <= size and (x + 1) <= size and y <= size and x <= size and y >= 0 and size >= 10 and x >= 0)):
      state_prime = 1
      y_prime = (y + 1)
      size_prime = size
      x_prime = x

    if state == 3 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and not (x <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and y >= 0 and size >= 10 and x >= 0)):
      state_prime = 1
      y_prime = (y + 1)
      size_prime = size
      x_prime = x

    if state == 3 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and not ((y - 1) >= 0) and (x - 1) >= 0 and y >= 0 and size >= 10 and not (x >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and ((not ((y + 1) <= size) and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and (x - 1) >= 0 and y >= 0 and size >= 10 and x >= 0)):
      state_prime = 2
      y_prime = (y - 1)
      size_prime = size
      x_prime = x

    if state == 3 and (((y + 1) <= size and not ((x + 1) <= size) and y <= size and x <= size and (y - 1) >= 0 and not ((x - 1) >= 0))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    if state == 3 and (((y + 1) <= size and (x + 1) <= size and not (y <= size))):
      state_prime = 1
      y_prime = (y - 1)
      size_prime = size
      x_prime = (x - 1)

    state = state_prime
    x = x_prime
    y = y_prime
    size = size_prime
    yield {'x':x, 'y':y, 'size':size}


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

