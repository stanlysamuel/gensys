import json
import readline

def run(init, inputs):
  state = 0
  a = init['a']
  b = init['b']
  c = init['c']
  for _input in inputs:
    if state == 0 and ((not (c >= b) and a >= c and not (a >= b) and not (b >= c) and b >= a)):
      state_prime = 0
      c_prime = b
      a_prime = b
      b_prime = c

    if state == 0 and ((not (c >= b) and a >= c and a >= b and not (b >= c) and b >= a)):
      state_prime = 0
      c_prime = b
      a_prime = b
      b_prime = c

    if state == 0 and ((not (c >= b) and not (a >= c) and not (a >= b) and not (b >= c) and not (b >= a))):
      state_prime = 0
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((c >= b and a >= c and not (a >= b) and not (b >= c) and b >= a)):
      state_prime = 0
      c_prime = c
      a_prime = a
      b_prime = a

    if state == 0 and ((c >= b and not (a >= c) and a >= b and b >= c and not (b >= a))):
      state_prime = 0
      c_prime = c
      a_prime = a
      b_prime = b

    if state == 0 and ((not (c >= b) and a >= c and not (a >= b) and b >= c and not (b >= a))):
      state_prime = 0
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((c >= b and not (a >= c) and not (a >= b) and not (b >= c) and b >= a)):
      state_prime = 0
      c_prime = b
      a_prime = a
      b_prime = c

    if state == 0 and ((c >= b and not (a >= c) and a >= b and not (b >= c) and b >= a)):
      state_prime = 0
      c_prime = b
      a_prime = a
      b_prime = c

    if state == 0 and ((not (c >= b) and not (a >= c) and a >= b and not (b >= c) and b >= a)):
      state_prime = 0
      c_prime = b
      a_prime = b
      b_prime = c

    if state == 0 and ((c >= b and a >= c and a >= b and b >= c and b >= a)):
      state_prime = 0
      c_prime = b
      a_prime = a
      b_prime = c

    if state == 0 and ((c >= b and not (a >= c) and not (a >= b) and b >= c and not (b >= a))):
      state_prime = 0
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((c >= b and a >= c and not (a >= b) and not (b >= c) and not (b >= a))):
      state_prime = 0
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((c >= b and a >= c and not (a >= b) and b >= c and not (b >= a))):
      state_prime = 0
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (c >= b) and not (a >= c) and a >= b and not (b >= c) and not (b >= a))):
      state_prime = 0
      c_prime = b
      a_prime = b
      b_prime = c

    if state == 0 and ((c >= b and a >= c and not (a >= b) and b >= c and b >= a)):
      state_prime = 0
      c_prime = b
      a_prime = a
      b_prime = c

    if state == 0 and ((not (c >= b) and not (a >= c) and not (a >= b) and not (b >= c) and b >= a)):
      state_prime = 0
      c_prime = b
      a_prime = b
      b_prime = c

    if state == 0 and ((not (c >= b) and a >= c and a >= b and b >= c and not (b >= a))):
      state_prime = 0
      c_prime = c
      a_prime = a
      b_prime = b

    if state == 0 and ((c >= b and not (a >= c) and a >= b and not (b >= c) and not (b >= a))):
      state_prime = 0
      c_prime = b
      a_prime = a
      b_prime = c

    if state == 0 and ((not (c >= b) and a >= c and a >= b and b >= c and b >= a)):
      state_prime = 0
      c_prime = c
      a_prime = b
      b_prime = a

    if state == 0 and ((not (c >= b) and a >= c and a >= b and not (b >= c) and not (b >= a))):
      state_prime = 0
      c_prime = b
      a_prime = b
      b_prime = c

    if state == 0 and ((c >= b and not (a >= c) and not (a >= b) and not (b >= c) and not (b >= a))):
      state_prime = 0
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (c >= b) and not (a >= c) and a >= b and b >= c and not (b >= a))):
      state_prime = 0
      c_prime = c
      a_prime = a
      b_prime = b

    if state == 0 and ((c >= b and a >= c and a >= b and not (b >= c) and not (b >= a))):
      state_prime = 0
      c_prime = b
      a_prime = a
      b_prime = c

    if state == 0 and ((c >= b and a >= c and a >= b and not (b >= c) and b >= a)):
      state_prime = 0
      c_prime = b
      a_prime = a
      b_prime = c

    if state == 0 and ((not (c >= b) and not (a >= c) and not (a >= b) and b >= c and b >= a)):
      state_prime = 0
      c_prime = c
      a_prime = b
      b_prime = a

    if state == 0 and ((c >= b and not (a >= c) and not (a >= b) and b >= c and b >= a)):
      state_prime = 0
      c_prime = c
      a_prime = b
      b_prime = a

    if state == 0 and ((not (c >= b) and not (a >= c) and a >= b and b >= c and b >= a)):
      state_prime = 0
      c_prime = c
      a_prime = a
      b_prime = b

    if state == 0 and ((c >= b and not (a >= c) and a >= b and b >= c and b >= a)):
      state_prime = 0
      c_prime = c
      a_prime = a
      b_prime = b

    if state == 0 and ((not (c >= b) and a >= c and not (a >= b) and b >= c and b >= a)):
      state_prime = 0
      c_prime = c
      a_prime = b
      b_prime = a

    if state == 0 and ((c >= b and a >= c and a >= b and b >= c and not (b >= a))):
      state_prime = 0
      c_prime = b
      a_prime = a
      b_prime = c

    if state == 0 and ((not (c >= b) and a >= c and not (a >= b) and not (b >= c) and not (b >= a))):
      state_prime = 0
      c_prime = b
      a_prime = b
      b_prime = a

    if state == 0 and ((not (c >= b) and not (a >= c) and not (a >= b) and b >= c and not (b >= a))):
      state_prime = 0
      c_prime = b
      a_prime = b
      b_prime = a

    state = state_prime
    a = a_prime
    b = b_prime
    c = c_prime
    yield {'a':a, 'b':b, 'c':c}


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

