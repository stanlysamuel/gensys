import json
import readline

def run(init, inputs):
  state = 0
  x = init['x']
  y = init['y']
  for _input in inputs:
    env_x_move = _input['env_x_move']
    if state == 0 and ((not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and y <= (x + 2) and y <= (x + 1) and not (y >= (x - 2)))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = (y + 1)

    if state == 0 and ((not (env_x_move == 0) and not (env_x_move == -1) and not (env_x_move == 1))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = (y + 1)

    if state == 0 and ((env_x_move == 0 and not (env_x_move == -1) and not (env_x_move == 1) and y <= (x + 2) and y <= (x + 1) and y >= (x - 2) and y >= (x - 1))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = y

    if state == 0 and ((not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and y <= (x + 2) and not (y <= (x + 1)))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = (y + 1)

    if state == 0 and ((env_x_move == 0 and not (env_x_move == -1) and env_x_move == 1 and y <= (x + 2) and y <= (x + 1) and y >= (x - 2) and y >= (x - 1))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = y

    if state == 0 and ((not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and y <= (x + 2) and y <= (x + 1) and y >= (x - 2) and not (y >= (x - 1)))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = (y + 1)

    if state == 0 and ((env_x_move == 0 and not (env_x_move == -1) and y <= (x + 2) and not (y <= (x + 1)))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = (y + 1)

    if state == 0 and ((not (env_x_move == 0) and env_x_move == -1 and env_x_move == 1 and y <= (x + 2) and y <= (x + 1) and y >= (x - 2) and y >= (x - 1))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = y

    if state == 0 and ((env_x_move == 0 and not (env_x_move == -1) and not (y <= (x + 2)))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = (y + 1)

    if state == 0 and ((not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and not (y <= (x + 2)))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = (y + 1)

    if state == 0 and ((not (env_x_move == 0) and env_x_move == -1 and env_x_move == 1 and y <= (x + 2) and y <= (x + 1) and not (y >= (x - 2)))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = (y + 1)

    if state == 0 and ((env_x_move == 0 and env_x_move == -1)):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = (y + 1)

    if state == 0 and ((not (env_x_move == 0) and env_x_move == -1 and not (env_x_move == 1) and y <= (x + 2) and not (y <= (x + 1)))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = (y + 1)

    if state == 0 and ((env_x_move == 0 and not (env_x_move == -1) and not (env_x_move == 1) and y <= (x + 2) and y <= (x + 1) and y >= (x - 2) and not (y >= (x - 1)))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = (y + 1)

    if state == 0 and ((env_x_move == 0 and not (env_x_move == -1) and env_x_move == 1 and y <= (x + 2) and y <= (x + 1) and y >= (x - 2) and not (y >= (x - 1)))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = (y + 1)

    if state == 0 and ((not (env_x_move == 0) and env_x_move == -1 and not (env_x_move == 1) and y <= (x + 2) and y <= (x + 1) and y >= (x - 2) and not (y >= (x - 1)))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = (y + 1)

    if state == 0 and ((env_x_move == 0 and not (env_x_move == -1) and not (env_x_move == 1) and y <= (x + 2) and y <= (x + 1) and not (y >= (x - 2)))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = (y + 1)

    if state == 0 and ((env_x_move == 0 and not (env_x_move == -1) and env_x_move == 1 and y <= (x + 2) and y <= (x + 1) and not (y >= (x - 2)))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = (y + 1)

    if state == 0 and ((not (env_x_move == 0) and env_x_move == -1 and not (env_x_move == 1) and y <= (x + 2) and y <= (x + 1) and not (y >= (x - 2)))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = (y + 1)

    if state == 0 and ((not (env_x_move == 0) and env_x_move == -1 and env_x_move == 1 and y <= (x + 2) and y <= (x + 1) and y >= (x - 2) and not (y >= (x - 1)))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = (y + 1)

    if state == 0 and ((not (env_x_move == 0) and env_x_move == -1 and env_x_move == 1 and y <= (x + 2) and not (y <= (x + 1)))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = (y + 1)

    if state == 0 and ((not (env_x_move == 0) and env_x_move == -1 and not (env_x_move == 1) and not (y <= (x + 2)))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = (y + 1)

    if state == 0 and ((not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and y <= (x + 2) and y <= (x + 1) and y >= (x - 2) and y >= (x - 1))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = (y + 1)

    if state == 0 and ((not (env_x_move == 0) and env_x_move == -1 and not (env_x_move == 1) and y <= (x + 2) and y <= (x + 1) and y >= (x - 2) and y >= (x - 1))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = (y - 1)

    if state == 0 and ((not (env_x_move == 0) and env_x_move == -1 and env_x_move == 1 and not (y <= (x + 2)))):
      state_prime = 0
      x_prime = (x + env_x_move)
      y_prime = (y + 1)

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

