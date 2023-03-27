import json
import readline

def run(init, inputs):
  state = 0
  x = init['x']
  y = init['y']
  size = init['size']
  width = init['width']
  for _input in inputs:
    if state == 0 and ((not (r_y <= (size - width)) and not (r_x <= (size - width)) and width <= 10 and y <= size and x <= size and not (r_y >= width))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and r_x <= (size - width) and width <= 10 and y <= size and not (x <= size))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and r_x <= (size - width) and not (width <= 10))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((not (r_y <= (size - width)) and not (r_x <= (size - width)) and width <= 10 and y <= size and x <= size and r_y >= width and r_x >= width and not (width >= 5))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((not (r_y <= (size - width)) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and r_y >= width and not (r_x >= width) and width >= 5 and not (y >= 0))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and not (r_y >= width) and not (r_x >= width) and width >= 5 and y >= 0 and size >= 50 and x >= 0)):
      state_prime = 0
      width_prime = width
      y_prime = y
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and not (r_x <= (size - width)) and width <= 10 and y <= size and not (x <= size))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and not (r_x <= (size - width)) and not (width <= 10))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and not (r_x <= (size - width)) and width <= 10 and not (y <= size))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((not (r_y <= (size - width)) and not (r_x <= (size - width)) and not (width <= 10))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and r_y >= width and not (r_x >= width) and width >= 5 and not (y >= 0))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((not (r_y <= (size - width)) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and not (r_y >= width))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((not (r_y <= (size - width)) and not (r_x <= (size - width)) and width <= 10 and not (y <= size))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((not (r_y <= (size - width)) and r_x <= (size - width) and not (width <= 10))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and not (r_x <= (size - width)) and width <= 10 and y <= size and x <= size and not (r_y >= width) and not (r_x >= width))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and not (r_x <= (size - width)) and width <= 10 and y <= size and x <= size and r_y >= width and r_x >= width and width >= 5 and y >= 0 and size >= 50 and not (x >= 0))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((not (r_y <= (size - width)) and not (r_x <= (size - width)) and width <= 10 and y <= size and x <= size and r_y >= width and not (r_x >= width))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((not (r_y <= (size - width)) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and r_y >= width and not (r_x >= width) and width >= 5 and y >= 0 and size >= 50 and x >= 0)):
      state_prime = 0
      width_prime = width
      y_prime = (y - 1)
      size_prime = size
      x_prime = x

    if state == 0 and ((r_y <= (size - width) and not (r_x <= (size - width)) and width <= 10 and y <= size and x <= size and r_y >= width and r_x >= width and width >= 5 and y >= 0 and size >= 50 and x >= 0)):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = x

    if state == 0 and ((r_y <= (size - width) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and not (r_y >= width) and not (r_x >= width) and not (width >= 5))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and not (r_y >= width) and r_x >= width and width >= 5 and y >= 0 and not (size >= 50))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((not (r_y <= (size - width)) and not (r_x <= (size - width)) and width <= 10 and y <= size and not (x <= size))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and not (r_y >= width) and not (r_x >= width) and width >= 5 and y >= 0 and not (size >= 50))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((not (r_y <= (size - width)) and r_x <= (size - width) and width <= 10 and not (y <= size))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((not (r_y <= (size - width)) and not (r_x <= (size - width)) and width <= 10 and y <= size and x <= size and r_y >= width and r_x >= width and width >= 5 and y >= 0 and not (size >= 50))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((not (r_y <= (size - width)) and not (r_x <= (size - width)) and width <= 10 and y <= size and x <= size and r_y >= width and r_x >= width and width >= 5 and y >= 0 and size >= 50 and not (x >= 0))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and not (r_x <= (size - width)) and width <= 10 and y <= size and x <= size and r_y >= width and r_x >= width and width >= 5 and y >= 0 and not (size >= 50))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and not (r_x <= (size - width)) and width <= 10 and y <= size and x <= size and r_y >= width and not (r_x >= width))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((not (r_y <= (size - width)) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and r_y >= width and r_x >= width and width >= 5 and y >= 0 and not (size >= 50))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and not (r_y >= width) and r_x >= width and width >= 5 and y >= 0 and size >= 50 and not (x >= 0))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and not (r_x <= (size - width)) and width <= 10 and y <= size and x <= size and not (r_y >= width) and r_x >= width and not (width >= 5))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and not (r_x <= (size - width)) and width <= 10 and y <= size and x <= size and r_y >= width and r_x >= width and width >= 5 and not (y >= 0))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((not (r_y <= (size - width)) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and r_y >= width and not (r_x >= width) and not (width >= 5))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((not (r_y <= (size - width)) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and r_y >= width and r_x >= width and not (width >= 5))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((not (r_y <= (size - width)) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and r_y >= width and r_x >= width and width >= 5 and not (y >= 0))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((not (r_y <= (size - width)) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and r_y >= width and r_x >= width and width >= 5 and y >= 0 and size >= 50 and not (x >= 0))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and not (r_y >= width) and not (r_x >= width) and width >= 5 and not (y >= 0))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and not (r_y >= width) and not (r_x >= width) and width >= 5 and y >= 0 and size >= 50 and not (x >= 0))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((not (r_y <= (size - width)) and not (r_x <= (size - width)) and width <= 10 and y <= size and x <= size and r_y >= width and r_x >= width and width >= 5 and y >= 0 and size >= 50 and x >= 0)):
      state_prime = 0
      width_prime = width
      y_prime = y
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and ((r_y <= (size - width) and not (r_x <= (size - width)) and width <= 10 and y <= size and x <= size and not (r_y >= width) and r_x >= width and width >= 5 and y >= 0 and size >= 50 and not (x >= 0))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((not (r_y <= (size - width)) and not (r_x <= (size - width)) and width <= 10 and y <= size and x <= size and r_y >= width and r_x >= width and width >= 5 and not (y >= 0))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and not (r_y >= width) and r_x >= width and not (width >= 5))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and not (r_y >= width) and r_x >= width and width >= 5 and y >= 0 and size >= 50 and x >= 0)):
      state_prime = 0
      width_prime = width
      y_prime = y
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((not (r_y <= (size - width)) and r_x <= (size - width) and width <= 10 and y <= size and not (x <= size))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and not (r_x <= (size - width)) and width <= 10 and y <= size and x <= size and not (r_y >= width) and r_x >= width and width >= 5 and y >= 0 and size >= 50 and x >= 0)):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = x

    if state == 0 and ((r_y <= (size - width) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and r_y >= width and not (r_x >= width) and width >= 5 and y >= 0 and size >= 50 and x >= 0)):
      state_prime = 0
      width_prime = width
      y_prime = (y - 1)
      size_prime = size
      x_prime = x

    if state == 0 and ((not (r_y <= (size - width)) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and r_y >= width and not (r_x >= width) and width >= 5 and y >= 0 and size >= 50 and not (x >= 0))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and not (r_x <= (size - width)) and width <= 10 and y <= size and x <= size and not (r_y >= width) and r_x >= width and width >= 5 and y >= 0 and not (size >= 50))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and r_y >= width and not (r_x >= width) and width >= 5 and y >= 0 and size >= 50 and not (x >= 0))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and r_y >= width and not (r_x >= width) and width >= 5 and y >= 0 and not (size >= 50))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and r_y >= width and not (r_x >= width) and not (width >= 5))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and not (r_y >= width) and r_x >= width and width >= 5 and not (y >= 0))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and not (r_x <= (size - width)) and width <= 10 and y <= size and x <= size and r_y >= width and r_x >= width and not (width >= 5))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and r_x <= (size - width) and width <= 10 and not (y <= size))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and r_y >= width and r_x >= width)):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((not (r_y <= (size - width)) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and r_y >= width and r_x >= width and width >= 5 and y >= 0 and size >= 50 and x >= 0)):
      state_prime = 0
      width_prime = width
      y_prime = y
      size_prime = size
      x_prime = (x - 1)

    if state == 0 and ((not (r_y <= (size - width)) and r_x <= (size - width) and width <= 10 and y <= size and x <= size and r_y >= width and not (r_x >= width) and width >= 5 and y >= 0 and not (size >= 50))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    if state == 0 and ((r_y <= (size - width) and not (r_x <= (size - width)) and width <= 10 and y <= size and x <= size and not (r_y >= width) and r_x >= width and width >= 5 and not (y >= 0))):
      state_prime = 0
      width_prime = width
      y_prime = (y + 1)
      size_prime = size
      x_prime = (x + 1)

    state = state_prime
    x = x_prime
    y = y_prime
    size = size_prime
    width = width_prime
    yield {'x':x, 'y':y, 'size':size, 'width':width}


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

