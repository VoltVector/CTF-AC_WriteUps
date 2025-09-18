# Solution 

In this chall, we are tasked to find the owner of the server from this image

At first, we tried to see if there's anything that the image hides,and so we used tools like binwalk, but to no avail.
Then we decided to see if there's a way to see if we can pinpoint what server do the players from the image frequent. At the same time, we saw that one of the players has his name cut of half way, and so we also set out to find who this person was.

We eventually found the accounts of the other players, but still, we found no lead. Judging by the 6th's player skin and name, we eventually bruteforced our way into finding his account: **Leaky_Tandos**. With a simple google search, we were able to find a minecraft server with
Leaky_Tandos in it, called: `The Pen`. 

The comment section if full of him just typing "bump".

After joining the server, I tried to find the room from the image, and low and behold, I found who the owner is.

## Flag

ctf{play.thepen-mc.net:Leaky_Tandos}
