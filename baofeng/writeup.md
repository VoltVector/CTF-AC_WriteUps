## Baofeng
> forensics

`Our radio monitoring agency captured a recording of someone disturbing the radio waves. Due to buget cuts there's nobody to decode the message and who he is. Please help us!`

A very helpful tool for solving this challenge was Audacity. I loaded the MP3 file into Audacity and started analyzing it. Since the call was rather short and quick, I decided that a good approach would be slowing down the call by at least 50%. After that, I amplified the call by -12db, normalized it, and reduced the background noise.

![[Pasted image 20250916202608.png]]

The middle part of the call states that the location is "KN15KS", which is a reference to the Hunedoara city. Although the first part of the call sign was unintelligible, after some research, I've found that the prefix YO2 is assigned to aircrafts from the given area (Hunedoara). After that, I've listened for the rest of the callsign and completed the challenge.

Flag: ctf{yo2tss_hunedoara}
