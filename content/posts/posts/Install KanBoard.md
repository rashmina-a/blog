---
title: Installed KanBoard
date: 2026-10-11
draft: false
tags:
  - self_host
  - New
  - Brand_new
  - study
  - learn
---
Ok today I installed **KanBoard** which is a self hosted Project Management Software which I use for **Spaced Repetition** when studying , I use it with several columns where I have these things called recall columns where I put the names of lessons as tasks which I studied Then I have columns where there are recall in 1,3,7,21 days and also an initial stage. I first put them into Initial stage and after studying it I put into recall 1 and then I put it to a column in front or back based on my recallability for that specific lesson. This helps preserve my memory of that lesson for a long ... time.

!![Image Description](/images/Pasted%20image%2020261011131811.png)

This is just an illustration of how it works , I also use **Anki Flashcards** to retain my memory like this , I suggest You too check it out [Anki](https://apps.ankiweb.net/). Don't worry it's a free software which can be installed mostly on any device. I've been using it for about an year now and I can guarantee that It helps you retain memory.
## Installation - KanBoard

The easiest method to install is using docker which you need to install and you need to open your terminal and run this command 
```bash
   docker run -d --name kanboard --restart unless-stopped -p 8080:80 `
     -v kanboard_data:/var/www/app/data `
     -v kanboard_plugins:/var/www/app/plugins `
     kanboard/kanboard:latest
```
This will automatically download the image and make it so that it automatically starts up on log in, And then you can go to [This link](http://localhost:8080) or [http://localhost:<Specified_Port>] to access the web interface, the default username and password are **admin** , **admin** Change it immediately after logging in by going to **User icon -> My Profile -> Change Password** after that you can follow the next steps by using the [Documentation](https://docs.kanboard.org/) 

## Preview

!![Image Description](/images/Pasted%20image%2020261011133149.png)

!![Image Description](/images/Pasted%20image%2020261011133201.png)

!![Image Description](/images/Pasted%20image%2020261011133233.png)
## Helpful Links

[Docker Documentation](https://docs.docker.com/)
[KanBoard Documentation](https://docs.kanboard.org/)
