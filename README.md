# carsavingscountdown

While I may have a strategy for saving for my future and retirement, I haven't got a decent strategy for saving up for a car upgrade. As of 2024-05-15, I am learning Python again. I thought that I would try to hit two birds with one stone with this project.

## Overview

This repo will consist of a very simple Python script that will be stored locally on my Windows machine which will run on startup which will remind me of my savings target and how far I am off the target. I will employ the use of a seperate .bat file that will run on startup with the use of Windows Task Scheduler.

This script works by creating seperate functions for each component of this script's utility. These components include:

1. Loading the savings figures from savings.json.
2. Saving the updated values to savings.json.
3. Displaying the savings progress and current values. 
4. Main menu.

Each of these functions are called before the main menu is presented. There is a function for the main menu which presents the user with some options to either edit the savings/goal values, give them a motivational speech or exit the script. 

### Figure 1: savings.json output with simple records of goal and saved amounts

![image](https://github.com/v-azza/carsavingscountdown/assets/6570303/2dbd1dfd-7be7-4981-b1af-520c3b54236a)

For the image below, I have added example values. 

### Figure 2: What I see when my PC is booted

![image](https://github.com/v-azza/carsavingscountdown/assets/6570303/475c23d4-05f2-40c1-8fa6-29201714cb06)


## Setup

Save this script in a safe place. Then you must do the following: 

1. Create a .bat file to point towards both your Python3.exe, and this script file. [This](https://datatofish.com/batch-python-script/ "Link to help you write the .bat file which will point to your python script to be used in Task Scheduler") link was very helpful for me in writing this .bat file.
2. Move this .bat file to your Start up programs folder. You can find out where this Start up programs folder is by pressing `Win + R` then type `shell:startup`.
3. Create a task in Task Scheduler, to run the .bat file with elevated permissions. Otherwise, given the need to write a .json file to the root folder, the script will not work as intended. [This](https://datatofish.com/batch-python-script/(https://superuser.com/a/797635) "Superuser answer that helped me set up the task in Task Scheduler") Superuser answer was very helpful for me in partuclar in getting this to run correctly.

### Figures 3 - 7: Task Scheduler options used. 

Note I have anonymised the path for the Author and .bat location paths, that would usually be displayed here.
![1](https://github.com/v-azza/carsavingscountdown/assets/6570303/bd67a936-b208-47fe-8fba-e753e2d06b20)
![2](https://github.com/v-azza/carsavingscountdown/assets/6570303/9d3e0e0b-067e-4b7f-a194-19333a1c4838)
![3](https://github.com/v-azza/carsavingscountdown/assets/6570303/915c2e16-5126-4753-a072-1ab1289ea61d)
![4](https://github.com/v-azza/carsavingscountdown/assets/6570303/a846359d-2cc5-4d4e-bc33-db733361c19b)


## Known issues

There are a few bits that I need to figure out on my own to make this a bit nicer, and I will get round to these. They are:

1. Input validation: When unexpected inputs are provided, the script exits with no feedback to the user. 
2. Progress bar: There is no visual aid to illustrate how far along the saving process I am. This will be added
3. JSON usage: Since this is a not a critical or data-sensitive script, the current savings/goal value storage method is appropriate. However, I can store these values in another method to improve usability. Like a madlad, it currently throws a .json file into my system32 folder to help store my savings values. 
4. Readability: I can employ the use of colours to help highlight certain features.
