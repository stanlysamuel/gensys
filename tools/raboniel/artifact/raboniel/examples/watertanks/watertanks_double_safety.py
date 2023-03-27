import json
import readline

def run(init, inputs):
  state = 0
  r_x1 = init['r_x1']
  r_x2 = init['r_x2']
  for _input in inputs:
    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and r_x2 < 0.2 and not (r_x1 < 0.7))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and r_x2 < 0.2 and not (r_x1 < 0.7))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and r_x1 < 0.2)):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and r_x1 < 0.2)):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and not (r_x2 < 0.7))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and not (r_x1 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and not (r_x2 < 0.7))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = ((0.7916 * r_x2) + (0.1719 * r_x1))
      r_x1_prime = (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and not (r_x2 < 0.7))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and r_x1 < 0.2)):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = r_x2
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = r_x2
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = ((0.7916 * r_x2) + (0.1719 * r_x1))
      r_x1_prime = (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and not (r_x1 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = ((0.7916 * r_x2) + (0.1719 * r_x1))
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and r_x1 < 0.2)):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and r_x1 < 0.2)):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and not (r_x2 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and not (r_x1 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = ((0.7916 * r_x2) + (0.1719 * r_x1))
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = r_x2
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = r_x2
      r_x1_prime = (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = r_x2
      r_x1_prime = (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and not (r_x1 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = r_x2
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not (r_x2 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = ((0.7916 * r_x2) + (0.1719 * r_x1))
      r_x1_prime = (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and not (r_x2 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and not (r_x1 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = r_x2
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and r_x2 >= 0.1 and not (r_x1 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = ((0.7916 * r_x2) + (0.1719 * r_x1))
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = ((0.7916 * r_x2) + (0.1719 * r_x1))
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and r_x1 < 0.2)):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = r_x2
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and not (r_x2 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = ((0.7916 * r_x2) + (0.1719 * r_x1))
      r_x1_prime = (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and not (r_x1 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = r_x1

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = r_x2
      r_x1_prime = (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and r_x2 >= 0.1 and not (r_x1 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and not (r_x2 < 0.7))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and not (r_x2 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and r_x2 < 0.7 and r_x2 < 0.2 and not (r_x1 < 0.7))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = r_x2
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not (r_x2 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = r_x2
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and not (r_x1 < 0.7))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = r_x2
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = r_x1

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and not (r_x2 < 0.2) and not (r_x1 < 0.7))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = r_x1

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and not (r_x1 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and not (r_x1 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and not (r_x2 < 0.2) and not (r_x1 < 0.7))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and r_x2 >= 0.1 and not (r_x1 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and not (r_x2 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = r_x1

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and r_x2 >= 0.1 and not (r_x1 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and not (r_x1 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and not (r_x1 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and not (r_x1 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and r_x2 >= 0.1 and not (r_x1 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and not (r_x2 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and not (r_x2 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = r_x2
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and not (r_x1 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and r_x1 < 0.2)):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and not (r_x2 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and not (r_x2 < 0.2) and not (r_x1 < 0.7))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not (r_x2 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = r_x2
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and r_x1 < 0.2)):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and not (r_x2 < 0.2) and not (r_x1 < 0.7))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and r_x2 < 0.7 and not (r_x2 < 0.2) and not (r_x1 < 0.7))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and r_x2 >= 0.1 and not (r_x1 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and not (r_x1 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and not (r_x2 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and (0.9635 * r_x2) >= 0.1 and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = r_x2
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and not (r_x1 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not (r_x2 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not (r_x2 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and not (r_x2 >= 0.1))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = r_x1

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and not ((((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and not (r_x1 >= 0.2))):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and not (r_x1 < 0.2) and not ((0.9635 * r_x2) >= 0.1) and ((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2 and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = r_x1

    if state == 0 and ((not (((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2) and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = r_x2
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and not (r_x2 < 0.2) and r_x1 < 0.7 and r_x1 < 0.2)):
      state_prime = 0
      r_x2_prime = (0.9635 * r_x2)
      r_x1_prime = ((0.8281 * r_x1) + (0.1719 * r_x2))

    if state == 0 and ((((0.7916 * r_x2) + (0.1719 * r_x1)) < 0.2 and ((0.8281 * r_x1) + (0.1719 * r_x2)) < 0.2 and (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753)) < 0.7 and r_x2 < 0.7 and r_x2 < 0.2 and r_x1 < 0.7 and not (r_x1 < 0.2) and not (((0.8281 * r_x1) + (0.1719 * r_x2)) >= 0.2) and r_x2 >= 0.1 and r_x1 >= 0.1 and r_x1 >= 0.2)):
      state_prime = 0
      r_x2_prime = ((0.7916 * r_x2) + (0.1719 * r_x1))
      r_x1_prime = (((0.8281 * r_x1) + (0.1719 * r_x2)) + (0.0003 * 324.6753))

    state = state_prime
    r_x1 = r_x1_prime
    r_x2 = r_x2_prime
    yield {'r_x1':r_x1, 'r_x2':r_x2}


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

