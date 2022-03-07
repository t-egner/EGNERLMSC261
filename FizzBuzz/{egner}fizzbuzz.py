count = 0
while (count <= 99):
  count = count + 1
  print(count)
  if count == 3 or count % 3 == 0:
    print("Fizz")
  if count == 5 or count % 5 == 0:
    print("Buzz")
  if count % 3 == 0 and count % 5 == 0:
      print("FizzBuzz")
