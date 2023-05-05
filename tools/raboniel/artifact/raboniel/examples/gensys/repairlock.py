import json
import readline

def run(init, inputs):
  state = 0
  pc = init['pc']
  l = init['l']
  gl = init['gl']
  for _input in inputs:
    if state == 0 and ((not (l >= 1) and not (l < 0) and not (pc == 5) and not (pc == 6) and not (pc == 4) and pc == 2 and not (pc == 0) and not (l == 1) and not (l == 0))):
      state_prime = 0
      pc_prime = 6
      l_prime = 0
      gl_prime = gl

    if state == 0 and ((not (l >= 1) and not (l < 0) and not (pc == 5) and not (pc == 6) and not (pc == 4) and not (pc == 2) and pc == 0 and not (l == 1) and l == 0)):
      state_prime = 0
      pc_prime = 2
      l_prime = l
      gl_prime = gl

    if state == 0 and ((not (l >= 1) and not (l < 0) and not (pc == 5) and pc == 6 and not (pc == 4) and not (pc == 2) and not (pc == 0) and not (l == 1) and not (l == 0))):
      state_prime = 0
      pc_prime = 6
      l_prime = 0
      gl_prime = gl

    if state == 0 and ((not (l >= 1) and not (l < 0) and not (pc == 5) and not (pc == 6) and not (pc == 4) and pc == 2 and not (pc == 0) and not (l == 1) and l == 0)):
      state_prime = 0
      pc_prime = 4
      l_prime = l
      gl_prime = gl

    if state == 0 and ((not (l >= 1) and not (l < 0) and not (pc == 5) and not (pc == 6) and not (pc == 4) and pc == 2 and pc == 0)):
      state_prime = 0
      pc_prime = 6
      l_prime = 0
      gl_prime = gl

    if state == 0 and ((not (l >= 1) and not (l < 0) and pc == 5)):
      state_prime = 0
      pc_prime = 6
      l_prime = 0
      gl_prime = gl

    if state == 0 and ((not (l >= 1) and not (l < 0) and not (pc == 5) and not (pc == 6) and not (pc == 4) and pc == 2 and not (pc == 0) and l == 1)):
      state_prime = 0
      pc_prime = 6
      l_prime = 0
      gl_prime = gl

    if state == 0 and ((not (l >= 1) and l < 0)):
      state_prime = 0
      pc_prime = 6
      l_prime = 0
      gl_prime = gl

    if state == 0 and ((not (l >= 1) and not (l < 0) and not (pc == 5) and pc == 6 and not (pc == 4) and not (pc == 2) and not (pc == 0) and not (l == 1) and l == 0)):
      state_prime = 0
      pc_prime = 0
      l_prime = l
      gl_prime = gl

    if state == 0 and ((not (l >= 1) and not (l < 0) and not (pc == 5) and pc == 6 and not (pc == 4) and not (pc == 2) and not (pc == 0) and l == 1)):
      state_prime = 0
      pc_prime = 6
      l_prime = 0
      gl_prime = gl

    if state == 0 and ((not (l >= 1) and not (l < 0) and not (pc == 5) and pc == 6 and not (pc == 4) and not (pc == 2) and pc == 0)):
      state_prime = 0
      pc_prime = 6
      l_prime = 0
      gl_prime = gl

    if state == 0 and ((not (l >= 1) and not (l < 0) and not (pc == 5) and not (pc == 6) and pc == 4 and not (pc == 2) and not (pc == 0) and not (l == 1) and l == 0)):
      state_prime = 0
      pc_prime = 6
      l_prime = l
      gl_prime = gl

    if state == 0 and ((not (l >= 1) and not (l < 0) and not (pc == 5) and pc == 6 and not (pc == 4) and pc == 2)):
      state_prime = 0
      pc_prime = 6
      l_prime = 0
      gl_prime = gl

    if state == 0 and ((not (l >= 1) and not (l < 0) and not (pc == 5) and pc == 6 and pc == 4)):
      state_prime = 0
      pc_prime = 6
      l_prime = 0
      gl_prime = gl

    if state == 0 and ((not (l >= 1) and not (l < 0) and not (pc == 5) and not (pc == 6) and pc == 4 and not (pc == 2) and not (pc == 0) and l == 1)):
      state_prime = 0
      pc_prime = 6
      l_prime = 0
      gl_prime = gl

    if state == 0 and ((not (l >= 1) and not (l < 0) and not (pc == 5) and not (pc == 6) and not (pc == 4) and not (pc == 2) and pc == 0 and not (l == 1) and not (l == 0))):
      state_prime = 0
      pc_prime = 6
      l_prime = 0
      gl_prime = gl

    if state == 0 and ((not (l >= 1) and not (l < 0) and not (pc == 5) and not (pc == 6) and pc == 4 and not (pc == 2) and pc == 0)):
      state_prime = 0
      pc_prime = 6
      l_prime = 0
      gl_prime = gl

    if state == 0 and ((not (l >= 1) and not (l < 0) and not (pc == 5) and not (pc == 6) and pc == 4 and pc == 2)):
      state_prime = 0
      pc_prime = 6
      l_prime = 0
      gl_prime = gl

    if state == 0 and ((not (l >= 1) and not (l < 0) and not (pc == 5) and not (pc == 6) and pc == 4 and not (pc == 2) and not (pc == 0) and not (l == 1) and not (l == 0))):
      state_prime = 0
      pc_prime = 6
      l_prime = 0
      gl_prime = gl

    if state == 0 and ((l >= 1)):
      state_prime = 0
      pc_prime = 6
      l_prime = 0
      gl_prime = gl

    if state == 0 and ((not (l >= 1) and not (l < 0) and not (pc == 5) and not (pc == 6) and not (pc == 4) and not (pc == 2) and not (pc == 0))):
      state_prime = 0
      pc_prime = 6
      l_prime = 0
      gl_prime = gl

    if state == 0 and ((not (l >= 1) and not (l < 0) and not (pc == 5) and not (pc == 6) and not (pc == 4) and not (pc == 2) and pc == 0 and l == 1)):
      state_prime = 0
      pc_prime = 6
      l_prime = 0
      gl_prime = gl

    state = state_prime
    pc = pc_prime
    l = l_prime
    gl = gl_prime
    yield {'pc':pc, 'l':l, 'gl':gl}


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

