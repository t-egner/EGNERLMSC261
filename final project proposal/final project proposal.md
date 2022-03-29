# Final Project Proposal

## Description
For my final project, I am going to make a website that hosts a program that can turn any audio file into a hilarious, TikTok-ready meme.
As someone who has been chronically online since the early days of Youtube, I have watched a myriad of trends come and go. Today, TikTok seems to be the master of these trends. Whatever becomes a meme on TikTok is almost immediately reposted to every other platform: Reddit, Instagram, Youtube, Twitter, even Facebook. The one thing these memes all have in common? The processing on their accompanying audio. Without fail, the song that the video plays along to is "bass boosted" and bit crushed, distorting it to the brink of being unrecognizable.
On my website, the client will be able to choose an audio file from their hard drive to upload, then sit back as my program goes to work.

First, an EQ will add a brick wall low pass filter to cut everything above 3 kHz. The EQ will also add a +6 dB bandshelf filter with a Q of 0.5 at 100 Hz to boost all bass frequencies.
Then, the program will use a bitcrusher to downsample the file four times at a 10 bit resolution. To hear a sample of the sound I'm going for, please listen to the .mp3 file I've added in this folder on GitHub. I used Izotope's Ozone Pro EQ and Logic's stock Bitcrusher plug-in to turn a small excerpt from "Levels" by Avicii into the perfect meme song.
Finally, the website will give the client a .mp3 file to download to their hard drive.

## Problem Solved and Use Cases
My website will solve the problem that any aspiring meme poster has: "how do I make content? And how do I make it standout?" Currently, the meme posting world is pretty limited to those who have knowledge of audio processing, and those who have access to a DAW or other program that allows them to manipulate audio. This seems unfair to me. There are plenty of producers out there, but still, they make up a small percent of the total population of people on the internet. With my website, everyone would have the ability to try their hand at making hilarious memes for the world. I have personally found a lot of joy in the funny things that people post, so if more people can bring their funny ideas to fruition, the better.
I'm aiming this website at the casual computer user who may not know much about how it actually works. I want my website to be very user friendly so that anyone from ages 2 to 102 can feel comfortable using it. Of course, this website will only really appeal to other chronically online people like me whose sense of humor is so broken that distorted audio evokes laughter. This is a niche subgroup, but it is ever-growing.

## Resources
For this idea to work, I'm going to need to know how to make a website. Luckily, we talked about that a lot in class today! I plan to use the [CSS templates](https://www.w3schools.com/css/) and [HTML5 Cheat Sheet](https://websitesetup.org/wp-content/uploads/2019/08/HTML-CHEAT-SHEET.png) you gave us in class today to make the website. I want the website to have a very Web1.0 aesthetic, since it's creating audio that sounds like it came straight out of 1996. Check out "interface inspo.jpeg" in this folder to get an idea of what I mean.

Next, I'm going to need to make it possible for a client to upload an audio file to my website. [This](https://stackoverflow.com/questions/43710173/upload-and-play-audio-file-js) article on stackoverflow shows how to do this in HTML.

Now, the hardest part: creating a program that can apply EQ and downsample an audio file. I'm hoping though that this won't become too difficult, since I'm not creating entire plug-ins, just make a computer apply processing to a file. The website won't allow the client to adjust any parameters either, so it should be pretty straight forward. For starters, [this article](https://www.mathworks.com/help/audio/ref/graphiceq-system-object.html) from mathworks gives the code for a simple EQ you can make using MATLAB. Then, I found another [stackoverflow article](https://stackoverflow.com/questions/30619740/downsampling-wav-audio-file) that outlines a program that can downsample a .wav file. I'm hoping it would work on other types of audio files, too (namely compressed ones), but I'm not sure. I'll need to do some more research and developnent there.

## Timeline
Week 10 (03/28 - 04/01): Design webpages using HTML5
Week 11 (04/04 - 04/08): Write code that will EQ an audio file  
Week 12 (04/11 - 04/15): Write code that will downsample an audio file and add that to Week 11's code
Week 13 (04/18 - 04/22): Link audio processing program to website
Week 14 (04/25 - 04/29): Debug any outstanding issues and finalize details
Week 15 (05/02 - 05/06): **Final Project DUE on Monday, May 2nd.**

## My Assessment
First, I think I should be graded on turning the project in on time. I should also be graded on the look of the website. Is it creative? Does it draw you in? Does it match the Web1.0 aesthetic I was aiming at? Further, I should be graded on how easy it is to use. Is it self-explanatory? Is there a clear order of clicks the user can follow? How long does it take to get your result? Finally, I should be graded on how well my audio processing program works. Can it operate on common lossy audio file types (.mp3, .m4a)? Does it produce the desired result? How long does it take to process and render a new file? These are just some ideas. There are probably lots of ways I can be graded on this assignment, but these are the first ideas that come to mind. 
