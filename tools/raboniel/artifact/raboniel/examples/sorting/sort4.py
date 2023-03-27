import json
import readline

def run(init, inputs):
  state = 0
  a = init['a']
  b = init['b']
  c = init['c']
  d = init['d']
  for _input in inputs:
    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and a >= d and a >= c and a >= b and b >= d and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and not (a >= d) and not (a >= c) and not (a >= b) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and not (a >= d) and a >= c)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and a >= d and not (a >= c) and not (a >= b) and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and a >= d and not (a >= c) and not (a >= b) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and a >= d and not (a >= c) and not (a >= b) and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and not (a >= c) and not (a >= b) and not (b >= d) and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and a >= d and a >= c and not (a >= b) and b >= d and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and c >= d and c >= b and a >= d and a >= c and a >= b and b >= d and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and a >= c and not (a >= b) and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and not (a >= c) and not (a >= b) and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and not (a >= c) and not (a >= b) and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and c >= d and c >= b and a >= d and not (a >= c) and not (a >= b) and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and a >= c and a >= b and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = a

    if state == 0 and ((d >= c and c >= d and c >= b and a >= d and a >= c and a >= b and not (b >= d) and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and a >= d and a >= c and not (a >= b) and not (b >= d) and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and a >= c and a >= b and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = b

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and not (a >= d) and not (a >= c) and a >= b and b >= d)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and not (a >= d) and a >= c and a >= b and b >= d)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and a >= c and not (a >= b) and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and not (a >= d) and a >= c and not (a >= b) and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and a >= d and not (a >= c) and not (a >= b) and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and c >= d and c >= b and a >= d and a >= c and a >= b and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and not (a >= c) and a >= b and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and c >= d and not (c >= b) and a >= d and not (a >= c) and not (a >= b) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and not (a >= c) and a >= b and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and c >= d and not (c >= b) and a >= d and a >= c and a >= b and b >= d and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and c >= d and not (c >= b) and a >= d and a >= c and a >= b and not (b >= d) and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and a >= c and not (a >= b) and b >= d and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and c >= d and not (c >= b) and a >= d and a >= c and not (a >= b) and b >= d and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and a >= d and a >= c and not (a >= b) and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and c >= d and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and a >= d and a >= c and a >= b and not (b >= d) and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and a >= c and not (a >= b) and b >= d and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and c >= d and not (c >= b) and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and a >= d and a >= c and not (a >= b) and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and a >= d and not (a >= c) and not (a >= b) and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and a >= d and a >= c and a >= b and b >= d and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and not (a >= d) and not (a >= b) and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and a >= d and a >= c and not (a >= b) and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and a >= c and not (a >= b) and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and a >= d and not (a >= c) and a >= b and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and a >= d and not (a >= c) and a >= b and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and c >= d and c >= b and a >= d and a >= c and not (a >= b) and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and c >= d and c >= b and a >= d and not (a >= c) and not (a >= b) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and a >= d and not (a >= c) and a >= b and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and a >= d and not (a >= c) and not (a >= b) and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and a >= c and not (a >= b) and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = c
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and not (a >= c) and not (a >= b) and b >= d and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and c >= d and not (c >= b) and a >= d and a >= c and not (a >= b) and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and a >= d and not (a >= c) and a >= b and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and c >= d and c >= b and a >= d and a >= c and a >= b and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = b

    if state == 0 and ((d >= c and c >= d and c >= b and a >= d and not (a >= c) and a >= b and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and not (a >= d) and a >= b and not (b >= d) and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and a >= c and a >= b and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and not (a >= d) and a >= c and a >= b and not (b >= d) and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and not (a >= c) and a >= b and b >= d and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and c >= d and c >= b and not (a >= d) and not (a >= c) and a >= b and not (b >= d) and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = b

    if state == 0 and ((d >= c and c >= d and c >= b and a >= d and a >= c and a >= b and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and c >= d and not (c >= b) and a >= d and a >= c and not (a >= b) and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and a >= c and not (a >= b) and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and a >= c and not (a >= b) and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and a >= c and a >= b and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = c
      a_prime = a
      b_prime = b

    if state == 0 and ((d >= c and c >= d and not (c >= b) and a >= d and not (a >= c) and a >= b and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and not (a >= d) and a >= c and a >= b and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and a >= c and not (a >= b) and not (b >= d) and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and c >= d and not (c >= b) and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and a >= c and a >= b and b >= d and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and a >= c and not (a >= b) and not (b >= d) and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and not (a >= d) and a >= c and not (a >= b) and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and not (a >= d) and a >= c and not (a >= b) and b >= d and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and a >= c and not (a >= b) and not (b >= d) and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = a
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and c >= b and not (a >= d) and not (a >= c) and a >= b and b >= d)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and a >= d and a >= c and a >= b and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and a >= c and a >= b and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and not (a >= c) and not (a >= b) and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = b

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and not (a >= c) and a >= b and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and not (a >= c) and not (a >= b) and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = c
      a_prime = a
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and a >= c and not (a >= b) and not (b >= d) and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and not (a >= c) and a >= b and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and a >= d and not (a >= c) and not (a >= b) and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = c
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and a >= b and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and a >= d and a >= c and a >= b and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and not (a >= d) and a >= c and not (a >= b) and b >= d and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and a >= b and not (b >= d) and not (b >= c))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and a >= d and not (a >= c) and a >= b and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and a >= c and not (a >= b) and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = c
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and a >= d and a >= c and a >= b and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = c
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and c >= d and c >= b and a >= d and a >= c and not (a >= b) and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and a >= d and a >= c and a >= b and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = c
      a_prime = a
      b_prime = b

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and a >= c and not (a >= b) and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = a

    if state == 0 and ((d >= c and c >= d and c >= b and a >= d and not (a >= c) and not (a >= b) and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = a
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and not (a >= c) and not (a >= b) and not (b >= d) and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and a >= b and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and c >= d and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and not (a >= c) and not (a >= b) and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = c
      a_prime = a
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and a >= c and not (a >= b) and b >= d and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and c >= d and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and c >= d and c >= b and a >= d and a >= c and a >= b and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and a >= c and a >= b and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and not (a >= c) and not (a >= b) and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and a >= d and a >= c and not (a >= b) and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and not (a >= c) and a >= b and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and a >= c and not (a >= b) and not (b >= d) and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and a >= d and a >= c and a >= b and not (b >= d) and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and not (a >= d) and a >= c and a >= b and b >= d)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and a >= d and a >= c and not (a >= b) and b >= d and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and c >= d and c >= b and not (a >= d) and not (a >= c) and a >= b and b >= d)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and a >= d and not (a >= c) and not (a >= b) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = c
      a_prime = a
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and not (a >= c) and a >= b and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and a >= c and not (a >= b) and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and not (a >= c) and not (a >= b) and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = a
      b_prime = b

    if state == 0 and ((d >= c and c >= d and c >= b and a >= d and a >= c and not (a >= b) and b >= d and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and not (a >= d) and not (a >= c) and a >= b and not (b >= d) and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and c >= d and c >= b and a >= d and not (a >= c) and not (a >= b) and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = a

    if state == 0 and ((d >= c and c >= d and c >= b and a >= d and not (a >= c) and a >= b and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = c
      a_prime = a
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and a >= d and a >= c and not (a >= b) and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and c >= b and not (a >= d) and not (a >= c) and a >= b and not (b >= d) and b >= c)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and c >= d and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and not (a >= d) and a >= c and not (a >= b) and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and a >= c and not (a >= b) and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and not (a >= d) and not (a >= c) and a >= b and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and c >= d and c >= b and a >= d and not (a >= c) and a >= b and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and not (a >= d) and a >= c and a >= b and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and c >= d and c >= b and a >= d and a >= c and not (a >= b) and not (b >= d) and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and not (a >= c) and not (a >= b) and b >= d and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = c
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and a >= c and a >= b and b >= d and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and not (a >= d) and a >= b and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and not (a >= d) and not (a >= b) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and c >= d and not (c >= b) and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and a >= c and a >= b and not (b >= d) and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and not (a >= d) and a >= c and not (a >= b) and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and c >= d and c >= b and not (a >= d) and not (a >= c) and a >= b and not (b >= d) and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and not (a >= c) and not (a >= b) and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and not (a >= d) and a >= c and not (a >= b) and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and not (a >= d) and a >= c and not (a >= b) and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = c
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and not (a >= c) and a >= b and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and c >= d and not (c >= b) and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and c >= d and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and a >= c and a >= b and b >= d)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and not (a >= c) and not (a >= b) and not (b >= d) and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and a >= d and a >= c and not (a >= b) and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and a >= d and a >= c and a >= b and not (b >= d) and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and a >= c and not (a >= b) and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = c
      a_prime = a
      b_prime = a

    if state == 0 and ((d >= c and c >= d and c >= b and a >= d and a >= c and not (a >= b) and b >= d and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and not (a >= c) and not (a >= b) and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = c
      a_prime = a
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and a >= d and a >= c and a >= b and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = b

    if state == 0 and ((d >= c and c >= d and not (c >= b) and a >= d and not (a >= c) and not (a >= b) and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and c >= d and not (c >= b) and a >= d and a >= c and not (a >= b) and not (b >= d) and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and c >= d and not (c >= b) and a >= d and not (a >= c) and a >= b and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and a >= d and a >= c and a >= b and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and not (a >= c) and not (a >= b) and not (b >= d) and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and a >= d and not (a >= c) and not (a >= b) and b >= d and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and a >= c and not (a >= b) and b >= d and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and not (a >= c) and a >= b and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and c >= d and not (c >= b) and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and a >= d and a >= c and not (a >= b) and not (b >= d) and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and not (a >= c) and not (a >= b) and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = a

    if state == 0 and ((d >= c and c >= d and c >= b and not (a >= d) and a >= c)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and a >= d and not (a >= c) and not (a >= b) and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = c
      a_prime = a
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and a >= d and not (a >= c) and not (a >= b) and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and a >= d and not (a >= c) and not (a >= b) and not (b >= d) and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and a >= d and a >= c and not (a >= b) and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = b

    if state == 0 and ((d >= c and c >= d and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and c >= d and not (c >= b) and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and a >= c and not (a >= b) and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and a >= d and a >= c and not (a >= b) and b >= d and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and c >= d and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and not (a >= c) and a >= b and not (b >= d) and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and a >= d and not (a >= c) and not (a >= b) and b >= d and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and a >= d and not (a >= c) and a >= b and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and c >= d and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and a >= c and a >= b and b >= d and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and a >= c and not (a >= b) and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and a >= d and a >= c and a >= b and b >= d and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and a >= c and a >= b and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and a >= d and not (a >= c) and a >= b and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = c
      a_prime = a
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and not (a >= d) and a >= b and b >= d)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and c >= d and not (c >= b) and a >= d and a >= c and not (a >= b) and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = c
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and a >= c and a >= b and b >= d and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and a >= c and a >= b and not (b >= d) and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = b

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and a >= c and not (a >= b) and b >= d and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and not (a >= c) and a >= b and b >= d and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = c
      a_prime = a
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and a >= c and a >= b and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = b

    if state == 0 and ((d >= c and c >= d and c >= b and a >= d and a >= c and not (a >= b) and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and not (a >= c) and not (a >= b) and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = c
      a_prime = a
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and a >= d and a >= c and a >= b and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and c >= d and not (c >= b) and not (a >= d) and a >= c)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and a >= c and not (a >= b) and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and a >= d and a >= c and not (a >= b) and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = c
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and a >= d and a >= c and not (a >= b) and not (b >= d) and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and a >= c and not (a >= b) and not (b >= d) and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and a >= c and not (a >= b) and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and a >= b and not (b >= d) and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and not (a >= d) and not (a >= c) and a >= b and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and not (a >= d) and a >= c and not (a >= b) and not (b >= d) and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and a >= c and not (a >= b) and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = c
      a_prime = a
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and a >= b and b >= d)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and not (a >= d) and not (a >= c) and a >= b)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and a >= d and a >= c and not (a >= b) and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and not (a >= c) and a >= b and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and c >= d and c >= b and not (a >= d) and not (a >= c) and a >= b and not (b >= d) and b >= c)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and a >= b and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and c >= d and c >= b and a >= d and a >= c and not (a >= b) and not (b >= d) and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and not (a >= d) and a >= c and not (a >= b) and not (b >= d) and not (b >= c))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and a >= b and not (b >= d) and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and c >= d and not (c >= b) and not (a >= d) and not (a >= c) and a >= b)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and not (a >= c) and a >= b and not (b >= d) and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and c >= b and not (a >= d) and not (a >= c) and a >= b and not (b >= d) and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and a >= c and a >= b and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = a
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and a >= c and a >= b and not (b >= d) and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and c >= d and not (c >= b) and a >= d and a >= c and not (a >= b) and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and not (a >= c) and a >= b and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = c
      a_prime = a
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and a >= d and not (a >= c) and a >= b and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and not (a >= c) and a >= b and not (b >= d) and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and c >= d and c >= b and a >= d and a >= c and not (a >= b) and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and not (a >= c) and not (a >= b) and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = c
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and not (a >= c) and not (a >= b) and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = a
      b_prime = b

    if state == 0 and ((d >= c and c >= d and not (c >= b) and a >= d and a >= c and a >= b and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and a >= c and a >= b and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and a >= c and not (a >= b) and b >= d and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and a >= c and a >= b and not (b >= d) and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and a >= c and a >= b and b >= d and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and a >= c and a >= b and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = c
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and a >= d and a >= c and a >= b and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and a >= c and a >= b and not (b >= d) and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and a >= c and a >= b and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and c >= d and c >= b and a >= d and a >= c and a >= b and b >= d and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and a >= c and not (a >= b) and not (b >= d) and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and a >= c and not (a >= b) and not (b >= d) and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and not (a >= c) and a >= b and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and a >= d and not (a >= c) and not (a >= b) and not (b >= d) and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and c >= d and c >= b and not (a >= d) and not (a >= c) and a >= b and not (b >= d) and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and a >= d and not (a >= c) and not (a >= b) and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = c
      a_prime = a
      b_prime = a

    if state == 0 and ((d >= c and c >= d and c >= b and a >= d and not (a >= c) and a >= b and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = a
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and a >= c and a >= b and not (b >= d) and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and a >= c and a >= b and not (b >= d) and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and a >= b and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and a >= d and a >= c and a >= b and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = a

    if state == 0 and ((d >= c and c >= d and c >= b and a >= d and a >= c and a >= b and not (b >= d) and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and c >= d and not (c >= b) and a >= d and not (a >= c) and a >= b and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and not (a >= d) and a >= c and a >= b and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and a >= c and not (a >= b) and b >= d and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and a >= c and not (a >= b) and b >= d and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and a >= c and a >= b and b >= d and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = a

    if state == 0 and ((d >= c and c >= d and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and c >= d and not (c >= b) and a >= d and a >= c and a >= b and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = c
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and a >= c and a >= b and not (b >= d) and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = b

    if state == 0 and ((d >= c and c >= d and not (c >= b) and a >= d and a >= c and a >= b and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = b

    if state == 0 and ((d >= c and c >= d and not (c >= b) and a >= d and not (a >= c) and not (a >= b) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = c
      a_prime = a
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and not (a >= d) and a >= c and not (a >= b) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = c
      a_prime = a
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and a >= d and not (a >= c) and a >= b and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and a >= d and not (a >= c) and not (a >= b) and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and not (a >= d) and not (a >= c) and a >= b and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = c
      a_prime = a
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and not (a >= d) and a >= c and a >= b and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and not (a >= d) and a >= c and a >= b and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and a >= c and a >= b and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and a >= d and a >= c and a >= b and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and a >= d and a >= c and not (a >= b) and b >= d and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and a >= d and a >= c and a >= b and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and a >= c and a >= b and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = b

    if state == 0 and ((not (d >= c) and not (c >= d) and c >= b and not (a >= d) and a >= c and a >= b and not (b >= d) and not (b >= c))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    if state == 0 and ((not (d >= c) and c >= d and c >= b and not (a >= d) and a >= c)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and c >= d and c >= b and not (a >= d) and not (a >= c) and not (a >= b) and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = c
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and not (a >= d) and a >= c and not (a >= b) and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = b

    if state == 0 and ((d >= c and not (c >= d) and c >= b and a >= d and not (a >= c) and not (a >= b) and b >= d and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and c >= d and not (c >= b) and a >= d and a >= c and a >= b and b >= d and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = c
      a_prime = b
      b_prime = a

    if state == 0 and ((not (d >= c) and not (c >= d) and not (c >= b) and a >= d and a >= c and not (a >= b) and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = a
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and not (a >= d) and a >= c and not (a >= b) and b >= d and not (b >= c))):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and not (a >= d) and a >= c and not (a >= b) and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and not (a >= d) and not (a >= c) and not (a >= b) and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and not (c >= d) and not (c >= b) and a >= d and a >= c and not (a >= b) and not (b >= d) and b >= c and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = b
      b_prime = b

    if state == 0 and ((d >= c and not (c >= d) and c >= b and not (a >= d) and not (a >= c) and a >= b and b >= d)):
      state_prime = 0
      d_prime = d
      c_prime = d
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and not (a >= c) and a >= b and b >= d and not (b >= c) and b >= a)):
      state_prime = 0
      d_prime = d
      c_prime = b
      a_prime = a
      b_prime = c

    if state == 0 and ((not (d >= c) and c >= d and c >= b and a >= d and not (a >= c) and not (a >= b) and b >= d and not (b >= c) and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((d >= c and c >= d and not (c >= b) and a >= d and a >= c and a >= b and not (b >= d) and b >= c and not (b >= a))):
      state_prime = 0
      d_prime = c
      c_prime = d
      a_prime = b
      b_prime = b

    state = state_prime
    a = a_prime
    b = b_prime
    c = c_prime
    d = d_prime
    yield {'a':a, 'b':b, 'c':c, 'd':d}


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

