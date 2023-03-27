import json
import readline

def run(init, inputs):
  state = 0
  counter = init['counter']
  for _input in inputs:
    i = _input['i']
    if state == 0 and ((not ((i + counter) <= 100) and not (i <= 5))):
      state_prime = 1
      counter_prime = (counter - i)

    if state == 0 and (((i + counter) <= 100 and not (i <= 5))):
      state_prime = 1
      counter_prime = (counter - i)

    if state == 0 and (((i + counter) <= 100 and i <= 5 and counter <= 100 and not (((i * -1) + counter) >= 0) and not (i >= 0))):
      state_prime = 1
      counter_prime = (counter - i)

    if state == 0 and ((not ((i + counter) <= 100) and i <= 5 and counter <= 100 and not (((i * -1) + counter) >= 0))):
      state_prime = 1
      counter_prime = (counter - i)

    if state == 0 and ((not ((i + counter) <= 100) and i <= 5 and counter <= 100 and ((i * -1) + counter) >= 0 and not (i >= 0))):
      state_prime = 1
      counter_prime = (counter - i)

    if state == 0 and ((not ((i + counter) <= 100) and i <= 5 and counter <= 100 and ((i * -1) + counter) >= 0 and i >= 0 and not (counter >= 0))):
      state_prime = 1
      counter_prime = (counter - i)

    if state == 0 and (((i + counter) <= 100 and i <= 5 and counter <= 100 and not (((i * -1) + counter) >= 0) and i >= 0 and counter >= 0)):
      state_prime = 0
      counter_prime = (counter + i)

    if state == 0 and (((i + counter) <= 100 and i <= 5 and not (counter <= 100))):
      state_prime = 1
      counter_prime = (counter - i)

    if state == 0 and (((i + counter) <= 100 and i <= 5 and counter <= 100 and ((i * -1) + counter) >= 0 and not (i >= 0))):
      state_prime = 1
      counter_prime = (counter - i)

    if state == 0 and ((not ((i + counter) <= 100) and i <= 5 and not (counter <= 100))):
      state_prime = 1
      counter_prime = (counter - i)

    if state == 0 and ((not ((i + counter) <= 100) and i <= 5 and counter <= 100 and ((i * -1) + counter) >= 0 and i >= 0 and counter >= 0)):
      state_prime = 1
      counter_prime = (counter - i)

    if state == 0 and (((i + counter) <= 100 and i <= 5 and counter <= 100 and ((i * -1) + counter) >= 0 and i >= 0 and counter >= 0)):
      state_prime = 0
      counter_prime = (counter + i)

    if state == 0 and (((i + counter) <= 100 and i <= 5 and counter <= 100 and ((i * -1) + counter) >= 0 and i >= 0 and not (counter >= 0))):
      state_prime = 1
      counter_prime = (counter - i)

    if state == 0 and (((i + counter) <= 100 and i <= 5 and counter <= 100 and not (((i * -1) + counter) >= 0) and i >= 0 and not (counter >= 0))):
      state_prime = 1
      counter_prime = (counter - i)

    if state == 1 and ((not ((i + counter) <= 100) and not (i <= 5))):
      state_prime = 1
      counter_prime = (counter - i)

    if state == 1 and (((i + counter) <= 100 and not (i <= 5))):
      state_prime = 1
      counter_prime = (counter - i)

    if state == 1 and (((i + counter) <= 100 and i <= 5 and counter <= 100 and not (((i * -1) + counter) >= 0) and not (i >= 0))):
      state_prime = 1
      counter_prime = (counter - i)

    if state == 1 and ((not ((i + counter) <= 100) and i <= 5 and counter <= 100 and not (((i * -1) + counter) >= 0))):
      state_prime = 1
      counter_prime = (counter - i)

    if state == 1 and ((not ((i + counter) <= 100) and i <= 5 and counter <= 100 and ((i * -1) + counter) >= 0 and not (i >= 0))):
      state_prime = 1
      counter_prime = (counter - i)

    if state == 1 and ((not ((i + counter) <= 100) and i <= 5 and counter <= 100 and ((i * -1) + counter) >= 0 and i >= 0 and not (counter >= 0))):
      state_prime = 1
      counter_prime = (counter - i)

    if state == 1 and (((i + counter) <= 100 and i <= 5 and counter <= 100 and not (((i * -1) + counter) >= 0) and i >= 0 and counter >= 0)):
      state_prime = 0
      counter_prime = (counter + i)

    if state == 1 and (((i + counter) <= 100 and i <= 5 and not (counter <= 100))):
      state_prime = 1
      counter_prime = (counter - i)

    if state == 1 and (((i + counter) <= 100 and i <= 5 and counter <= 100 and ((i * -1) + counter) >= 0 and not (i >= 0))):
      state_prime = 1
      counter_prime = (counter - i)

    if state == 1 and ((not ((i + counter) <= 100) and i <= 5 and not (counter <= 100))):
      state_prime = 1
      counter_prime = (counter - i)

    if state == 1 and ((not ((i + counter) <= 100) and i <= 5 and counter <= 100 and ((i * -1) + counter) >= 0 and i >= 0 and counter >= 0)):
      state_prime = 1
      counter_prime = (counter - i)

    if state == 1 and (((i + counter) <= 100 and i <= 5 and counter <= 100 and ((i * -1) + counter) >= 0 and i >= 0 and counter >= 0)):
      state_prime = 1
      counter_prime = (counter - i)

    if state == 1 and (((i + counter) <= 100 and i <= 5 and counter <= 100 and ((i * -1) + counter) >= 0 and i >= 0 and not (counter >= 0))):
      state_prime = 1
      counter_prime = (counter - i)

    if state == 1 and (((i + counter) <= 100 and i <= 5 and counter <= 100 and not (((i * -1) + counter) >= 0) and i >= 0 and not (counter >= 0))):
      state_prime = 1
      counter_prime = (counter - i)

    state = state_prime
    counter = counter_prime
    yield {'counter':counter}


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

