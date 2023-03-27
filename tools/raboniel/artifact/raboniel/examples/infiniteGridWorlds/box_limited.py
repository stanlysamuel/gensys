import json
import readline

def run(init, inputs):
  state = 0
  x = init['x']
  y = init['y']
  for _input in inputs:
    env_x_move = _input['env_x_move']
    env_y_move = _input['env_y_move']
    if state == 0 and ((not (y >= 0))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = (y - 1)

    if state == 0 and ((y >= 0 and not (y <= 3))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = (y - 1)

    if state == 0 and ((y >= 0 and y <= 3)):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = y

    state = state_prime
    x = x_prime
    y = y_prime
    yield {'x':x, 'y':y}


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

