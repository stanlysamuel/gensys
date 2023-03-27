import json
import readline

def run(init, inputs):
  state = 0
  counter = init['counter']
  buttonUp = init['buttonUp']
  buttonDown = init['buttonDown']
  for _input in inputs:
    buttonPressedUp = _input['buttonPressedUp']
    buttonPressedDown = _input['buttonPressedDown']
    if state == 0 and ((buttonPressedDown == 1 and buttonPressedDown == 0)):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and not (buttonPressedUp == 1) and buttonPressedUp == 0 and (counter + 2) <= 100 and (counter + 1) <= 100 and counter <= 100 and not ((counter - 2) >= 0) and (counter - 1) >= 0 and counter >= 0)):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = counter

    if state == 0 and ((buttonPressedDown == 1 and not (buttonPressedDown == 0) and buttonPressedUp == 1)):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((buttonPressedDown == 1 and not (buttonPressedDown == 0) and not (buttonPressedUp == 1) and not (buttonPressedUp == 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and buttonPressedUp == 1 and not (buttonPressedUp == 0) and (counter + 2) <= 100 and (counter + 1) <= 100 and counter <= 100 and not ((counter - 2) >= 0) and (counter - 1) >= 0 and not (counter >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and not (buttonPressedUp == 1) and buttonPressedUp == 0 and (counter + 2) <= 100 and (counter + 1) <= 100 and counter <= 100 and not ((counter - 2) >= 0) and (counter - 1) >= 0 and not (counter >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and buttonPressedUp == 1 and not (buttonPressedUp == 0) and (counter + 2) <= 100 and (counter + 1) <= 100 and not (counter <= 100))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and buttonPressedUp == 1 and not (buttonPressedUp == 0) and not ((counter + 2) <= 100) and (counter + 1) <= 100 and not (counter <= 100))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and buttonPressedUp == 1 and not (buttonPressedUp == 0) and (counter + 2) <= 100 and (counter + 1) <= 100 and counter <= 100 and (counter - 2) >= 0 and not ((counter - 1) >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and buttonPressedUp == 1 and not (buttonPressedUp == 0) and (counter + 2) <= 100 and not ((counter + 1) <= 100))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and buttonPressedUp == 1 and not (buttonPressedUp == 0) and not ((counter + 2) <= 100) and (counter + 1) <= 100 and counter <= 100 and not ((counter - 2) >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and not (buttonPressedUp == 1) and buttonPressedUp == 0 and (counter + 2) <= 100 and (counter + 1) <= 100 and counter <= 100 and (counter - 2) >= 0 and (counter - 1) >= 0 and counter >= 0)):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = counter

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and not (buttonPressedUp == 1) and buttonPressedUp == 0 and not ((counter + 2) <= 100) and (counter + 1) <= 100 and counter <= 100 and (counter - 2) >= 0 and (counter - 1) >= 0 and counter >= 0)):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = counter

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and not (buttonPressedUp == 1) and buttonPressedUp == 0 and not ((counter + 2) <= 100) and not ((counter + 1) <= 100) and counter <= 100 and not ((counter - 2) >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and not (buttonPressedUp == 1) and buttonPressedUp == 0 and not ((counter + 2) <= 100) and (counter + 1) <= 100 and counter <= 100 and not ((counter - 2) >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and buttonPressedUp == 1 and buttonPressedUp == 0)):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and not (buttonPressedUp == 1) and buttonPressedUp == 0 and not ((counter + 2) <= 100) and not ((counter + 1) <= 100) and counter <= 100 and (counter - 2) >= 0 and (counter - 1) >= 0 and counter >= 0)):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 0
      counter_prime = counter

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and buttonPressedUp == 1 and not (buttonPressedUp == 0) and (counter + 2) <= 100 and (counter + 1) <= 100 and counter <= 100 and not ((counter - 2) >= 0) and (counter - 1) >= 0 and counter >= 0)):
      state_prime = 0
      buttonDown_prime = 0
      buttonUp_prime = 1
      counter_prime = (counter + 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and not (buttonPressedUp == 1) and buttonPressedUp == 0 and not ((counter + 2) <= 100) and (counter + 1) <= 100 and not (counter <= 100))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and not (buttonPressedUp == 1) and buttonPressedUp == 0 and (counter + 2) <= 100 and (counter + 1) <= 100 and counter <= 100 and not ((counter - 2) >= 0) and not ((counter - 1) >= 0) and counter >= 0)):
      state_prime = 0
      buttonDown_prime = 0
      buttonUp_prime = 1
      counter_prime = counter

    if state == 0 and ((not (buttonPressedDown == 1) and not (buttonPressedDown == 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and not (buttonPressedUp == 1) and not (buttonPressedUp == 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((buttonPressedDown == 1 and not (buttonPressedDown == 0) and not (buttonPressedUp == 1) and buttonPressedUp == 0 and (counter + 2) <= 100 and (counter + 1) <= 100 and counter <= 100 and not ((counter - 2) >= 0) and (counter - 1) >= 0 and counter >= 0)):
      state_prime = 0
      buttonDown_prime = 0
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((buttonPressedDown == 1 and not (buttonPressedDown == 0) and not (buttonPressedUp == 1) and buttonPressedUp == 0 and not ((counter + 2) <= 100) and (counter + 1) <= 100 and counter <= 100 and (counter - 2) >= 0 and (counter - 1) >= 0 and not (counter >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and not (buttonPressedUp == 1) and buttonPressedUp == 0 and (counter + 2) <= 100 and (counter + 1) <= 100 and counter <= 100 and (counter - 2) >= 0 and (counter - 1) >= 0 and not (counter >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and buttonPressedUp == 1 and not (buttonPressedUp == 0) and (counter + 2) <= 100 and (counter + 1) <= 100 and counter <= 100 and not ((counter - 2) >= 0) and not ((counter - 1) >= 0) and counter >= 0)):
      state_prime = 0
      buttonDown_prime = 0
      buttonUp_prime = 1
      counter_prime = (counter + 1)

    if state == 0 and ((buttonPressedDown == 1 and not (buttonPressedDown == 0) and not (buttonPressedUp == 1) and buttonPressedUp == 0 and (counter + 2) <= 100 and not ((counter + 1) <= 100))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and buttonPressedUp == 1 and not (buttonPressedUp == 0) and (counter + 2) <= 100 and (counter + 1) <= 100 and counter <= 100 and (counter - 2) >= 0 and (counter - 1) >= 0 and counter >= 0)):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter + 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and buttonPressedUp == 1 and not (buttonPressedUp == 0) and (counter + 2) <= 100 and (counter + 1) <= 100 and counter <= 100 and not ((counter - 2) >= 0) and not ((counter - 1) >= 0) and not (counter >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((buttonPressedDown == 1 and not (buttonPressedDown == 0) and not (buttonPressedUp == 1) and buttonPressedUp == 0 and not ((counter + 2) <= 100) and not ((counter + 1) <= 100) and not (counter <= 100))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and buttonPressedUp == 1 and not (buttonPressedUp == 0) and not ((counter + 2) <= 100) and not ((counter + 1) <= 100))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and buttonPressedUp == 1 and not (buttonPressedUp == 0) and not ((counter + 2) <= 100) and (counter + 1) <= 100 and counter <= 100 and (counter - 2) >= 0 and (counter - 1) >= 0 and not (counter >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and not (buttonPressedUp == 1) and buttonPressedUp == 0 and not ((counter + 2) <= 100) and (counter + 1) <= 100 and counter <= 100 and (counter - 2) >= 0 and (counter - 1) >= 0 and not (counter >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and buttonPressedUp == 1 and not (buttonPressedUp == 0) and not ((counter + 2) <= 100) and (counter + 1) <= 100 and counter <= 100 and (counter - 2) >= 0 and not ((counter - 1) >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and not (buttonPressedUp == 1) and buttonPressedUp == 0 and (counter + 2) <= 100 and (counter + 1) <= 100 and counter <= 100 and (counter - 2) >= 0 and not ((counter - 1) >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((buttonPressedDown == 1 and not (buttonPressedDown == 0) and not (buttonPressedUp == 1) and buttonPressedUp == 0 and not ((counter + 2) <= 100) and not ((counter + 1) <= 100) and counter <= 100 and (counter - 2) >= 0 and (counter - 1) >= 0 and not (counter >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((buttonPressedDown == 1 and not (buttonPressedDown == 0) and not (buttonPressedUp == 1) and buttonPressedUp == 0 and not ((counter + 2) <= 100) and not ((counter + 1) <= 100) and counter <= 100 and not ((counter - 2) >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and buttonPressedUp == 1 and not (buttonPressedUp == 0) and (counter + 2) <= 100 and (counter + 1) <= 100 and counter <= 100 and (counter - 2) >= 0 and (counter - 1) >= 0 and not (counter >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and buttonPressedUp == 1 and not (buttonPressedUp == 0) and not ((counter + 2) <= 100) and (counter + 1) <= 100 and counter <= 100 and (counter - 2) >= 0 and (counter - 1) >= 0 and counter >= 0)):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 0
      counter_prime = (counter + 1)

    if state == 0 and ((buttonPressedDown == 1 and not (buttonPressedDown == 0) and not (buttonPressedUp == 1) and buttonPressedUp == 0 and not ((counter + 2) <= 100) and (counter + 1) <= 100 and counter <= 100 and (counter - 2) >= 0 and (counter - 1) >= 0 and counter >= 0)):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((buttonPressedDown == 1 and not (buttonPressedDown == 0) and not (buttonPressedUp == 1) and buttonPressedUp == 0 and not ((counter + 2) <= 100) and not ((counter + 1) <= 100) and counter <= 100 and (counter - 2) >= 0 and (counter - 1) >= 0 and counter >= 0)):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 0
      counter_prime = (counter - 1)

    if state == 0 and ((buttonPressedDown == 1 and not (buttonPressedDown == 0) and not (buttonPressedUp == 1) and buttonPressedUp == 0 and (counter + 2) <= 100 and (counter + 1) <= 100 and counter <= 100 and (counter - 2) >= 0 and (counter - 1) >= 0 and not (counter >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((buttonPressedDown == 1 and not (buttonPressedDown == 0) and not (buttonPressedUp == 1) and buttonPressedUp == 0 and (counter + 2) <= 100 and (counter + 1) <= 100 and counter <= 100 and (counter - 2) >= 0 and (counter - 1) >= 0 and counter >= 0)):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((buttonPressedDown == 1 and not (buttonPressedDown == 0) and not (buttonPressedUp == 1) and buttonPressedUp == 0 and (counter + 2) <= 100 and (counter + 1) <= 100 and counter <= 100 and (counter - 2) >= 0 and not ((counter - 1) >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and not (buttonPressedUp == 1) and buttonPressedUp == 0 and not ((counter + 2) <= 100) and not ((counter + 1) <= 100) and counter <= 100 and (counter - 2) >= 0 and (counter - 1) >= 0 and not (counter >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and not (buttonPressedUp == 1) and buttonPressedUp == 0 and not ((counter + 2) <= 100) and (counter + 1) <= 100 and counter <= 100 and (counter - 2) >= 0 and not ((counter - 1) >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((buttonPressedDown == 1 and not (buttonPressedDown == 0) and not (buttonPressedUp == 1) and buttonPressedUp == 0 and not ((counter + 2) <= 100) and not ((counter + 1) <= 100) and counter <= 100 and (counter - 2) >= 0 and not ((counter - 1) >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((buttonPressedDown == 1 and not (buttonPressedDown == 0) and not (buttonPressedUp == 1) and buttonPressedUp == 0 and not ((counter + 2) <= 100) and (counter + 1) <= 100 and counter <= 100 and not ((counter - 2) >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and not (buttonPressedUp == 1) and buttonPressedUp == 0 and not ((counter + 2) <= 100) and not ((counter + 1) <= 100) and not (counter <= 100))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((buttonPressedDown == 1 and not (buttonPressedDown == 0) and not (buttonPressedUp == 1) and buttonPressedUp == 0 and (counter + 2) <= 100 and (counter + 1) <= 100 and counter <= 100 and not ((counter - 2) >= 0) and not ((counter - 1) >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((buttonPressedDown == 1 and not (buttonPressedDown == 0) and not (buttonPressedUp == 1) and buttonPressedUp == 0 and (counter + 2) <= 100 and (counter + 1) <= 100 and not (counter <= 100))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((buttonPressedDown == 1 and not (buttonPressedDown == 0) and not (buttonPressedUp == 1) and buttonPressedUp == 0 and not ((counter + 2) <= 100) and (counter + 1) <= 100 and counter <= 100 and (counter - 2) >= 0 and not ((counter - 1) >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((buttonPressedDown == 1 and not (buttonPressedDown == 0) and not (buttonPressedUp == 1) and buttonPressedUp == 0 and not ((counter + 2) <= 100) and (counter + 1) <= 100 and not (counter <= 100))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and not (buttonPressedUp == 1) and buttonPressedUp == 0 and (counter + 2) <= 100 and (counter + 1) <= 100 and not (counter <= 100))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((buttonPressedDown == 1 and not (buttonPressedDown == 0) and not (buttonPressedUp == 1) and buttonPressedUp == 0 and (counter + 2) <= 100 and (counter + 1) <= 100 and counter <= 100 and not ((counter - 2) >= 0) and (counter - 1) >= 0 and not (counter >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and not (buttonPressedUp == 1) and buttonPressedUp == 0 and (counter + 2) <= 100 and not ((counter + 1) <= 100))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and not (buttonPressedUp == 1) and buttonPressedUp == 0 and (counter + 2) <= 100 and (counter + 1) <= 100 and counter <= 100 and not ((counter - 2) >= 0) and not ((counter - 1) >= 0) and not (counter >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    if state == 0 and ((not (buttonPressedDown == 1) and buttonPressedDown == 0 and not (buttonPressedUp == 1) and buttonPressedUp == 0 and not ((counter + 2) <= 100) and not ((counter + 1) <= 100) and counter <= 100 and (counter - 2) >= 0 and not ((counter - 1) >= 0))):
      state_prime = 0
      buttonDown_prime = 1
      buttonUp_prime = 1
      counter_prime = (counter - 1)

    state = state_prime
    counter = counter_prime
    buttonUp = buttonUp_prime
    buttonDown = buttonDown_prime
    yield {'counter':counter, 'buttonUp':buttonUp, 'buttonDown':buttonDown}


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

