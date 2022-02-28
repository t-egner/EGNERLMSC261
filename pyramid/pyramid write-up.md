## Pyramid Write-Up
-- I remembered that we did something similar in class, so I went to take a look at my notes and our README.md file for the week.
-- In IDLE, I input the code from the (notes)[https://github.com/rdwrome/lmsc261sp22/blob/main/100ControlFlow/README.md] that listed out 0 - 9 in a pyramid
-- When I ran this code, it made a huge list only one character wide...it looked like I had input the code correctly, but maybe I have a formatting preference in IDLE that's incorrect?
-- Well, I guess I'll just try anyway and maybe we can talk about an incorrect preference I might have in class!
-- After reviewing my notes, I googled "how to print pyramids idle" and read (this)[https://medium.com/edureka/python-pattern-programs-75e1e764a42f]. It had the exact "backwards" facing pyramid we needed for the homework!
-- In the homework, we had to define "stack" as a variable...hmm. Not really sure how that plays a part, so I just tried this (which also incorporated the code I found in the article):

n = int(input("Enter an integer between 1 and 8 to choose a height for the pyramid"))
# this is where I had the user input their number of choice
n = "stack"
# trying to define the variable...lol
def pattern (stack):
        k = 2 * n - 2
        for i in range(0, n):
            for j in range(0, k):
                print(end='')
# most of this i remembered from class!
            k = k - 2
            for j in range(0, i + 1):
                print("#", end='')
            print()

-- Well that didn't work! Excited to see the answer in class!!!
