## Chessboard Write-Up
Since I wasn't in class this past week, I read through the README on GitHub. That helped me get a basic idea of what the simple operators and syntax are for JS.
For this to work, I'm going to need 8 rows to print out a hashtag in a staggered pattern. I can use a counter that will go up to 8 for the rows and just a `result = "#"` to print out the correct character. I'm not sure how to make it a staggered pattern though! Google time.
I found [this article](https://stackoverflow.com/questions/26838639/javascript-chessboard-print) which had a really useful explanation of how to print the chessboard pattern. I liked this article because the original poster had a question about how to make their code more efficient, and the answers broke it down in a way that helped me understand what was going on (instead of just copying code without knowing why I'm doing what I'm doing).
Here is the code I used from the website that printed out the correct chessboard:

`let result = " ";
 for (let x = 0; x < 8; x++){
    for (let z = 0; z < 8; z++){
      if (0 == (z + x) % 2){
        result += " ";
      } else if (0 != (z + x) % 2){
        result += "#";
      }   
    }    
    result += "\n";
}  
console.log(result);`

This worked, just as expected!
I wasn't exactly sure how I was supposed to turn in a record of the console on Chrome, so I read [this article](https://stackoverflow.com/questions/7627113/save-the-console-log-in-chrome-to-a-file) on how to save your console as a .log file (thank you, Stack Overflow!!!) Hopefully that's the right way to turn this in, but I'll find out in class tomorrow!
