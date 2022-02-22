# Mice doc
First, I read through our README.md for this week again to see if I could find any clues in there.
The command line about bags and bananas under the header "f-String math" seemed interesting, but I knew that wasn't quite what I was looking for. I needed to figure out how to indent text.
So, I googled "how to print text in cascade in python."
I clicked on (this article)[https://stackoverflow.com/questions/67373424/cascade-printing-in-python]
The correct answer in the article said to use these command lines to cascade text:
a="******"
  for i in range(0,3):
  print("\t"*(i+1),a)
Here, a is the text they wanted to print.
I'm guessing the range(0,3) indicates how many lines it prints...but I'm not sure.
Then, I think \t means tab!
The a at the end will tell python to print the text associated with variable a.
So, I put this into python. I assigned a = "3BlindMice." Oops, not quite right.
Then, I tried this:
a = 3
b = "Blind" (When I first tried this, I just said b = Blind. Oops, error, need the quotes!)
c = "Mice"
for i in range(0,3):
	print("\t"*(i + 1),a)
	print("\t"*(i + 1),b)
	print("\t"*(i + 1),c)
...Which was also not right. It printed this:
3
Blind
Mice
  3
  Blind
  Mice
    3
    Blind
    Mice

Nooo! Ugh. Not quite sure what I'm doing wrong here. I'm close! But I don't know how to isolate each line of text.
My last try: instead of having (i + 1) for each print line, I did (i + 1), (i + 2), then (i + 3).
Maybe this will isolate each variable!
NO! This is what I got:
3
		 Blind
			 Mice
		 3
			 Blind
				 Mice
			 3
				 Blind
					 Mice
Not sure what to do next, but I'm excited to go over this in class and find the right answer!
