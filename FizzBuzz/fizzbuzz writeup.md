## FizzBuzz Write-Up
- I'm going to try a different approach today: coding in small chunks! I think that will help me complete this assignment without resorting to Googling stuff.
- So we're going to need some code that will print every integer from 1 to 100. So we'll need a counter that will stop once it gets to 100. That could look like this:

count = 0
while (count <= 99):
  count = count + 1
  print(count)

- Ok, just ran this in python and it WORKS! Awesome. Now, we need to tell the counter to print "Fizz" for 3 and "Buzz" for 5. I think we can do that with some if/else nesting commands:

if count == 3:
  print("Fizz")
else count == 5:
  print("Buzz")

- Ok, so that printed "Fizz" but NOT "Buzz". What? IDLE says that I have invalid syntax and highlighted the `c` in `count` that I have after `else` (line 14). I literally have no idea what that's about...
- Oh, wait! I think it needs to be an `if` command too, not an `else` command yet. Ok!
- Moving on, I'm just going to add the parts about being divisible by 3, 5, or both using a modulo operation:

if count == 3 or count % 3 == 0:
  print("Fizz")
  if count == 5 or count % 5 == 0:
    print("Buzz")
    if count % 3 == 0 and count % 5 == 0:
    print("FizzBuzz")

- Let's put it all together:

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

- Yay, it wor- ...WHAT?! Why is it not printing out "Buzz" when count == 5?!!!!!
- Just googled the difference between `if` and `elif` and read:
"so the difference is that the code always checks to see if an 'if' statement is true, checks 'elif' statements only if each 'if' and 'elif' statement above it is false, and 'else' runs only when the conditions for all attached 'if' and 'elif' statements are false." [first result returned on google](https://www.google.com/search?q=difference+between+if+and+elif+commands&rlz=1C5CHFA_enUS896US897&oq=difference+between+if+and+elif+commands&aqs=chrome..69i57j33i160l3.4651j0j7&sourceid=chrome&ie=UTF-8)
- Alright, let's try changing my `if` statements to `elif` ones instead:

count = 0
while (count <= 99):
  count = count + 1
  print(count)
  if count == 3 or count % 3 == 0:
    print("Fizz")
    elif count == 5 or count % 5 == 0:
      print("Buzz")
      elif count % 3 == 0 and count % 5 == 0:
          print("FizzBuzz")

- Woah, nope, now everything is text and there are no numbers. I'm reverting back to this code as my final answer:

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

- I know this isn't right, since it's printing the number AND the text, but I'm not sure how to change that and this is already late so this is my final answer for now!
