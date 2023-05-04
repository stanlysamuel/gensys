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
    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and env_x_move == 0 and not (env_x_move == -1) and env_x_move == 1 and x == xe and y == ye)):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = x
      ye_prime = ye
      y_prime = y

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and not (x == xe))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and x == xe and y == ye)):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and not ((ye - y) == 0))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and not (env_y_move == 1) and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and x == xe and y == ye)):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and not (env_y_move == 1) and env_x_move == 0 and not (env_x_move == -1) and env_x_move == 1 and x == xe and y == ye)):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = x
      ye_prime = ye
      y_prime = y

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and env_x_move == 0 and env_x_move == -1)):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and not (env_y_move == 1) and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and x == xe and y == ye)):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = y

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and not (env_y_move == 1) and not (env_x_move == 0) and env_x_move == -1 and not (env_x_move == 1) and x == xe and y == ye)):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and env_y_move == 1 and env_x_move == 0 and not (env_x_move == -1) and x == xe and y == ye)):
      state_prime = 0
      xe_prime = xe
      x_prime = x
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and not ((ye - y) <= 1))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and not ((ye - y) <= 2))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and env_y_move == 1 and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and x == xe and y == ye)):
      state_prime = 0
      xe_prime = xe
      x_prime = x
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and env_y_move == 1 and not (env_x_move == 0) and env_x_move == -1 and x == xe and y == ye)):
      state_prime = 0
      xe_prime = xe
      x_prime = x
      ye_prime = (ye + env_y_move)
      y_prime = y

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and env_x_move == 0 and not (env_x_move == -1) and not (env_x_move == 1) and x == xe and y == ye)):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = x
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and env_y_move == 1 and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and x == xe and y == ye)):
      state_prime = 0
      xe_prime = xe
      x_prime = x
      ye_prime = (ye + env_y_move)
      y_prime = y

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and env_x_move == 0 and not (env_x_move == -1) and x == xe and y == ye)):
      state_prime = 0
      xe_prime = xe
      x_prime = (x - 1)
      ye_prime = ye
      y_prime = y

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and x == xe and y == ye)):
      state_prime = 0
      xe_prime = xe
      x_prime = (x - 1)
      ye_prime = ye
      y_prime = y

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and env_x_move == 0 and not (env_x_move == -1) and x == xe and y == ye)):
      state_prime = 0
      xe_prime = xe
      x_prime = (x - 1)
      ye_prime = ye
      y_prime = y

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and x == xe and y == ye)):
      state_prime = 0
      xe_prime = xe
      x_prime = (x - 1)
      ye_prime = ye
      y_prime = y

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and not (env_x_move == 0) and env_x_move == -1 and x == xe and not (y == ye))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and env_y_move == 0 and env_y_move == -1)):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and not (env_y_move == 1) and not (env_x_move == 0) and env_x_move == -1 and not (env_x_move == 1) and x == xe and y == ye)):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)
      ye_prime = (ye + env_y_move)
      y_prime = y

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and env_x_move == 0 and not (env_x_move == -1) and x == xe and y == ye)):
      state_prime = 0
      xe_prime = xe
      x_prime = (x - 1)
      ye_prime = ye
      y_prime = y

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and not (env_x_move == 0) and env_x_move == -1 and x == xe and y == ye)):
      state_prime = 0
      xe_prime = xe
      x_prime = (x - 1)
      ye_prime = ye
      y_prime = y

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and x == xe and y == ye)):
      state_prime = 0
      xe_prime = xe
      x_prime = (x - 1)
      ye_prime = ye
      y_prime = y

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and not (env_y_move == 1) and env_x_move == 0 and not (env_x_move == -1) and not (env_x_move == 1) and x == xe and y == ye)):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = x
      ye_prime = (ye + env_y_move)
      y_prime = y

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and not (x == xe))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and x == xe and not (y == ye))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and not (env_y_move == 1))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and env_y_move == 1 and not (env_x_move == 0) and env_x_move == -1 and x == xe and y == ye)):
      state_prime = 0
      xe_prime = xe
      x_prime = x
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and not (env_x_move == 0) and env_x_move == -1 and not (env_x_move == 1) and x == xe and y == ye)):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x - 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and x == xe and not (y == ye))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and not (env_x_move == 0) and env_x_move == -1 and x == xe and not (y == ye))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and not (env_x_move == 0) and env_x_move == -1 and x == xe and y == ye)):
      state_prime = 0
      xe_prime = xe
      x_prime = (x - 1)
      ye_prime = ye
      y_prime = y

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and not (env_y_move == 1) and env_x_move == 0 and not (env_x_move == -1) and not (env_x_move == 1) and x == xe and y == ye)):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = x
      ye_prime = (ye + env_y_move)
      y_prime = (y - 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and not (env_y_move == 1) and not (env_x_move == 0) and env_x_move == -1 and env_x_move == 1 and x == xe and y == ye)):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = x
      ye_prime = ye
      y_prime = y

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and env_y_move == 1 and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and x == xe and not (y == ye))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and env_y_move == 1 and env_x_move == 0 and not (env_x_move == -1) and x == xe and y == ye)):
      state_prime = 0
      xe_prime = xe
      x_prime = x
      ye_prime = (ye + env_y_move)
      y_prime = y

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and x == xe and not (y == ye))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and env_x_move == 0 and not (env_x_move == -1) and x == xe and not (y == ye))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and x == xe and not (y == ye))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and not (env_x_move == 0) and env_x_move == -1 and not (x == xe))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and not (env_x_move == 0) and env_x_move == -1 and x == xe and not (y == ye))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and env_x_move == 0 and not (env_x_move == -1) and x == xe and not (y == ye))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and not (x == xe))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and env_x_move == 0 and not (env_x_move == -1) and not (x == xe))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and not (env_x_move == 0) and env_x_move == -1 and not (x == xe))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and not (x == xe))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and not (env_x_move == 0) and env_x_move == -1 and x == xe and not (y == ye))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and not (env_y_move == 1) and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and not (x == xe))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and env_y_move == 1 and not (env_x_move == 0) and not (env_x_move == -1) and not (env_x_move == 1))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and env_x_move == 0 and not (env_x_move == -1) and not (x == xe))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and env_y_move == 1 and not (env_x_move == 0) and env_x_move == -1 and not (x == xe))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and not (env_y_move == 1) and env_x_move == 0 and not (env_x_move == -1) and not (x == xe))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and env_x_move == 0 and env_x_move == -1)):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and not (env_y_move == 1) and env_x_move == 0 and not (env_x_move == -1) and x == xe and not (y == ye))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and not (env_y_move == 1) and env_x_move == 0 and not (env_x_move == -1) and env_x_move == 1 and x == xe and y == ye)):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = x
      ye_prime = ye
      y_prime = y

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and env_y_move == 1 and env_x_move == 0 and not (env_x_move == -1) and x == xe and not (y == ye))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and not (env_y_move == 1) and env_x_move == 0 and env_x_move == -1)):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and not (env_x_move == 0) and not (env_x_move == -1) and not (env_x_move == 1))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and not (env_y_move == 1) and not (env_x_move == 0) and env_x_move == -1 and not (env_x_move == 1) and x == xe and not (y == ye))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and not (env_y_move == 1) and not (env_x_move == 0) and env_x_move == -1 and env_x_move == 1 and x == xe and not (y == ye))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and not (env_x_move == 0) and not (env_x_move == -1) and not (env_x_move == 1))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and not (env_y_move == 1) and not (env_x_move == 0) and not (env_x_move == -1) and not (env_x_move == 1))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and env_y_move == 1 and not (env_x_move == 0) and env_x_move == -1 and x == xe and not (y == ye))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and not (env_y_move == 1) and not (env_x_move == 0) and env_x_move == -1 and env_x_move == 1 and not (x == xe))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and env_x_move == 0 and not (env_x_move == -1) and not (x == xe))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and not (x == xe))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and env_y_move == 1 and env_x_move == 0 and not (env_x_move == -1) and not (x == xe))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and not (env_x_move == 0) and not (env_x_move == -1) and not (env_x_move == 1))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and not (env_y_move == 1) and not (env_x_move == 0) and env_x_move == -1 and not (env_x_move == 1) and not (x == xe))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and x == xe and not (y == ye))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and env_x_move == 0 and env_x_move == -1)):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and env_x_move == 0 and env_x_move == -1)):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and env_x_move == 0 and not (env_x_move == -1) and x == xe and not (y == ye))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and env_x_move == 0 and not (env_x_move == -1) and x == xe and not (y == ye))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and not (env_x_move == 0) and env_x_move == -1 and x == xe and not (y == ye))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and not (env_x_move == 0) and env_x_move == -1 and not (x == xe))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and env_x_move == 0 and env_x_move == -1)):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and env_x_move == 0 and not (env_x_move == -1) and x == xe and not (y == ye))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and not (env_x_move == 0) and env_x_move == -1 and not (x == xe))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and not (env_x_move == 0) and env_x_move == -1 and not (x == xe))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and env_y_move == 0 and env_y_move == -1)):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and not (env_x_move == 0) and not (env_x_move == -1) and not (env_x_move == 1))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and not (env_y_move == 1))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and env_y_move == 1 and env_x_move == 0 and env_x_move == -1)):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and not ((ye - y) == 0))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and not (env_y_move == 1) and not (env_x_move == 0) and env_x_move == -1 and env_x_move == 1 and x == xe and y == ye)):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = x
      ye_prime = ye
      y_prime = y

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and env_x_move == 0 and not (env_x_move == -1) and not (x == xe))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and ((not ((xe - x) <= 2))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and not (env_x_move == 0) and env_x_move == -1 and x == xe and y == ye)):
      state_prime = 0
      xe_prime = xe
      x_prime = (x - 1)
      ye_prime = ye
      y_prime = y

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and (xe - x) == 1 and (ye - y) == 0 and env_y_move == 0 and not (env_y_move == -1) and env_x_move == 0 and not (env_x_move == -1) and not (x == xe))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and not (env_x_move == 0) and not (env_x_move == -1) and not (env_x_move == 1))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and env_y_move == 1 and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and not (x == xe))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and not ((xe - x) == 0))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and env_y_move == -1 and not (env_y_move == 1) and not (env_x_move == 0) and not (env_x_move == -1) and env_x_move == 1 and x == xe and not (y == ye))):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = (x + 1)
      ye_prime = (ye + env_y_move)
      y_prime = (y + 1)

    if state == 0 and (((xe - x) <= 2 and (ye - y) <= 2 and (ye - y) <= 1 and (xe - x) == 0 and not ((xe - x) == 1) and (ye - y) == 0 and not (env_y_move == 0) and not (env_y_move == -1) and env_y_move == 1 and not (env_x_move == 0) and env_x_move == -1 and env_x_move == 1 and x == xe and y == ye)):
      state_prime = 0
      xe_prime = (xe + env_x_move)
      x_prime = x
      ye_prime = ye
      y_prime = y

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

