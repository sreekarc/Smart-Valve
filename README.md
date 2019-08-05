# Smart-Valve

This is the code to a project that will turn off water if it has been flowing for longer than a set amount of time. It was made to turn off a shower if the hot water has been running for longer than an amount of time set in the corresponding app. 

Materials used for this Project:

motorized valve

sharkbites

raspberry pi

5v relay

wires

power source

flow sensor

The circuit for this project should look like this:
![alt text](https://cdn.instructables.com/FEL/FXOD/J7MFSVLB/FELFXODJ7MFSVLB.LARGE.jpg)

After completing the circuit on a breadboard I soldered it together and shrink-wrapped so it would look nice.

After the circuit is completed I started to set up the physical parts.

Here is a picture of it put together:
# PICTURE

This was meant to attach right onto the hot water pipe so pipes would need to be cut for this project.

First after installing noobs on the raspberry pi I wrote programs onto the pi that would create a website that would be used to control the a/c. To do this I first created a simple node js website. After that I installed socket.io using npm install. This website helped me create a simple webserver and install socket.io: https://www.w3schools.com/nodejs/nodejs_raspberrypi.asp. My main html webpage is above. The code in routes.js and index.js was written into the corresponding files so an outside device can talk to the pi. The python files were also made in the same folder.

The main communication method is a raspberry pi hosting a web server that any device on the internet can go on. I made an android app that can connect to the raspberry pi server for easier temperature control. The code to the phone app is here: # https://github.com/sreekarc/something. In the phone app code I had to set the raspberry pi ip address as the ip address to connect too in the phone's socket.io

After all the code was done there was one last thing I had to do, which was make it so that the code would all start running as the pi booted up. This way it could be headless. To do this I first went to the terminal and wrote `sudo nano /etc/rc.local`. Then I added these three lines of code to the end of the file right before "exit 0":

`sudo pigpiod`

`/usr/bin/python3 /home/pi/AC_Project/MindLabs/temperature.py >> /tmp/junk.txt &`

`node /home/pi/AC_Project/MindLabs/index.js >> /tmp/junk1.txt &`

After that I was done and was able to plug it in, position it just right, and control the temperature anywhere through my phone.
