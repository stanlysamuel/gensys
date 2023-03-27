import json
import readline

def run(init, inputs):
  state = 0
  x = init['x']
  y = init['y']
  xe = init['xe']
  ye = init['ye']
  for _input in inputs:
    env_x_move = _input['env_x_move']
    env_y_move = _input['env_y_move']
    if state == 0 and ((not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and env_x_move == 0 and not (env_x_move == -1) and not (y == ye) and not (x == xe))):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)
      xe_prime = (xe + env_x_move)
      x_prime = x

    if state == 0 and ((not (env_y_move == 0) and env_y_move == -1 and not (env_x_move == 0) and env_x_move == -1 and not (y == ye) and x == xe)):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((env_y_move == 0 and not (env_y_move == -1) and env_x_move == 0 and not (env_x_move == -1) and not (y == ye) and not (x == xe))):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = y
      xe_prime = (xe + env_x_move)
      x_prime = x

    if state == 0 and ((not (env_y_move == 0) and env_y_move == -1 and not (env_x_move == 0) and env_x_move == -1 and not (y == ye) and not (x == xe))):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((env_y_move == 0 and env_y_move == -1)):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and not (y == ye) and x == xe)):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and not (env_x_move == 0) and env_x_move == -1 and not (y == ye) and not (x == xe))):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((env_y_move == 0 and not (env_y_move == -1) and env_x_move == 0 and not (env_x_move == -1) and y == ye)):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((env_y_move == 0 and not (env_y_move == -1) and not (env_x_move == 0) and env_x_move == -1 and not (y == ye) and x == xe)):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and env_x_move == 0 and env_x_move == -1)):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and not (env_x_move == 0) and env_x_move == -1 and y == ye)):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and not (env_x_move == 0) and not (env_x_move == -1) and not (env_x_move == 1))):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and env_x_move == 0 and not (env_x_move == -1) and not (y == ye) and x == xe)):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and y == ye)):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and not (y == ye) and not (x == xe))):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)

    if state == 0 and ((not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and env_x_move == 0 and not (env_x_move == -1) and y == ye)):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((env_y_move == 0 and not (env_y_move == -1) and not (env_x_move == 0) and env_x_move == -1 and not (y == ye) and not (x == xe))):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = y
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((not (env_y_move == 0) and env_y_move == -1 and env_x_move == 0 and not (env_x_move == -1) and y == ye)):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((env_y_move == 0 and not (env_y_move == -1) and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and not (y == ye) and not (x == xe))):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = y
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)

    if state == 0 and ((not (env_y_move == 0) and env_y_move == -1 and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and not (y == ye) and not (x == xe))):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)

    if state == 0 and ((not (env_y_move == 0) and env_y_move == -1 and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and y == ye)):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((not (env_y_move == 0) and env_y_move == -1 and not (env_x_move == 0) and not (env_x_move == -1) and not (env_x_move == 1))):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((not (env_y_move == 0) and not (env_y_move == -1) and not (env_y_move == 1))):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((env_y_move == 0 and not (env_y_move == -1) and not (env_x_move == 0) and env_x_move == -1 and y == ye)):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((not (env_y_move == 0) and env_y_move == -1 and not (env_x_move == 0) and env_x_move == -1 and y == ye)):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and not (env_x_move == 0) and env_x_move == -1 and not (y == ye) and x == xe)):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((not (env_y_move == 0) and env_y_move == -1 and env_x_move == 0 and not (env_x_move == -1) and not (y == ye) and x == xe)):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((not (env_y_move == 0) and env_y_move == -1 and env_x_move == 0 and not (env_x_move == -1) and not (y == ye) and not (x == xe))):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = x

    if state == 0 and ((not (env_y_move == 0) and env_y_move == -1 and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and not (y == ye) and x == xe)):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((env_y_move == 0 and not (env_y_move == -1) and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and not (y == ye) and x == xe)):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((not (env_y_move == 0) and env_y_move == -1 and env_x_move == 0 and env_x_move == -1)):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((env_y_move == 0 and not (env_y_move == -1) and not (env_x_move == 0) and not (env_x_move == -1) and not (env_x_move == 1))):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((env_y_move == 0 and not (env_y_move == -1) and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and y == ye)):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((env_y_move == 0 and not (env_y_move == -1) and env_x_move == 0 and env_x_move == -1)):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    if state == 0 and ((env_y_move == 0 and not (env_y_move == -1) and env_x_move == 0 and not (env_x_move == -1) and not (y == ye) and x == xe)):
      state_prime = 0
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)

    state = state_prime
    x = x_prime
    y = y_prime
    xe = xe_prime
    ye = ye_prime
    yield {'x':x, 'y':y, 'xe':xe, 'ye':ye}


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

