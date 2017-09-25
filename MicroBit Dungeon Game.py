
#                MICROBIT DUNGEON GAME 1.0 ~ By Jeremiah Boby

#                        ------------------------
#                         Version 1.0 changelog:
#                        ------------------------
#       The character can now move across a 2-dimensional array map.
#           The game quits on reaching a; specified coordinate.

from microbit import *
# Import all the microbit functions
import random
# We need this to randomise map areas etc.

pixelMap = (
    # The map for the Microbit game
    (9),(9),(9),(9),(9),(9),(9),(9),(9),(9),(9),(0),(0),(0),(9),
            
    (9),(0),(0),(0),(0),(0),(0),(0),(0),(9),(9),(0),(0),(0),(9),
            
    (9),(0),(0),(0),(0),(0),(0),(0),(0),(9),(9),(0),(0),(0),(9),
            
    (9),(0),(0),(0),(0),(0),(0),(0),(0),(9),(9),(0),(0),(0),(9),
            
    (9),(0),(0),(0),(9),(9),(0),(0),(0),(9),(9),(0),(0),(0),(9),
            
    (9),(0),(0),(0),(9),(9),(0),(0),(0),(9),(9),(0),(0),(0),(9),
            
    (9),(0),(0),(0),(9),(9),(0),(0),(0),(9),(9),(0),(0),(0),(9),
            
    (9),(0),(0),(0),(9),(9),(0),(0),(0),(9),(9),(0),(0),(0),(9),
            
    (9),(0),(0),(0),(9),(9),(0),(0),(0),(9),(9),(0),(0),(0),(9),
            
    (9),(0),(0),(0),(9),(9),(0),(0),(0),(9),(9),(0),(0),(0),(9),
        
    (9),(0),(0),(0),(9),(9),(0),(0),(0),(9),(9),(0),(0),(0),(9),
            
    (9),(0),(0),(0),(9),(9),(0),(0),(0),(0),(0),(0),(0),(0),(9),
            
    (9),(0),(0),(0),(9),(9),(0),(0),(0),(0),(0),(0),(0),(0),(9),
            
    (9),(0),(0),(0),(9),(9),(0),(0),(0),(0),(0),(0),(0),(0),(9),
            
    (9),(9),(9),(9),(9),(9),(9),(9),(9),(9),(9),(9),(9),(9),(9),
    )

Cords = []
# The map of coordinates of the 15x15 grid
for a in range(14,-1,-1):
    # Go through the y axis
	for b in range(0,15):
            # Go through the x axis
		Cords.append([b,a])
		# Add the coordinate

Cords = [tuple(item) for item in Cords]
# Convert coordinates to tuples, allows me to hash Cords[] to a dictionary

refer = dict(zip(Cords,pixelMap))
# Creates a dictionary for pixel referencing

currentLoc = [2,2]
# Set the beginning location for the character
# 2 <= x <= 12
# 2 <= y <= 12

def moveChar(x,y):
    # Function to move character across the map by a set amount
    global currentLoc
    prevLoc = currentLoc
    # In case changes cannot be made
    try:
        # Error trapping the frame/map arrays
        currentLoc[0]+=x
        currentLoc[1]+=y
        areaSet()
    except:
        # Revert to previous location
        currentLoc = prevLoc
        areaSet()
    if refer[currentLoc[0]+x,currentLoc[1]+y] > 0:
        # If user is in a wall
        currentLoc = prevLoc
        areaSet()
        
def syntaxify(array):
    # Turns a 2d array into a Microbit-frame
    tempFrame = ""
    # Sets the microfied frame to ""    
    for row in array:
        # Goes through every row in the frame
        for pixel in row:
            # Goes through every pixel in the row
            tempFrame += str(pixel)
            # Adds that pixel to the Microfied frame
        tempFrame += ":"
        # Adds a colon (Microbit syntax for next row)        
    tempFrame = tempFrame[0:len(tempFrame)-1]
    # Takes away the last colon (No new line needed)
    return tempFrame
    # This is the final Microfied frame

def refresh(array):
    # Display a Micro-bit frame, followed by a 100 millisecond frame delay
    frame=Image(syntaxify(array))
    # Turn the Microbit-frame into a frame object
    display.show(frame)
    # Display the frame  object
    sleep(0.1)
    # Delay until the next frame
    
def areaSet():
    # Function to refresh the user's position in the map tuple
    global currentLoc
    x = currentLoc[0]
    # Set x to the player's x value
    y = currentLoc[1]
    # Set y to the player's y value
    area = (
        (x-2,y+2), (x-1,y+2), (x,y+2), (x+1,y+2), (x+2,y+2),
        (x-2,y+1), (x-1,y+1), (x,y+1), (x+1,y+1), (x+2,y+1),
        ( x-2, y), ( x-1, y), ( x, y), ( x+1, y), ( x+2, y),
        (x-2,y-1), (x-1,y-1), (x,y-1), (x+1,y-1), (x+2,y-1),
        (x-2,y-2), (x-1,y-2), (x,y-2), (x+1,y-2), (x+2,y-2)
        )
    # Creates the coordinate frame to refer[] to later on
    pArea = []
    # Creates the pixel brightness frame
    for coord in area:
        # Goes through every coordinate in the area[] tuple
        try:
            pArea.append(refer[coord])
        except:
            pArea.append(9)
        # Appends the corresponding pixel value using refer[], or sets it to a wall value
    empty = [[],[],[],[],[]]
    # Set an empty array so that we can put it into syntaxify()
    for row in range(0,5):
        # Go through every first index
        for item in range(0,5):
            # Go through every second index
            index = ((row*5)+(item+1))-1
            # The number from 0-24 to index from pArea[]
            empty[row].append(pArea[index])
            # Add the number to the correct row in empty[]
    refresh(empty)
    # Display this frame
    if currentLoc == [22,24]:
        endGame()

def endGame():
    # Code to run when the game is over
    display.scroll("Game over!")
    sleep(100)
    exit()
                    
while True:
    # The main bit of code that references the previous functions:
    x = accelerometer.get_x()
    # Get the accelerometer x value
    y = accelerometer.get_y()
    # Get the accelerometer y value
    if x > 200:
        # Right facing
        moveChar(1,0)
    elif x < -200:
        # Left facing
        moveChar(-1,0)       
    if y > 200:
        # Down facing
        moveChar(0,-1)        
    elif y < -200:
        # Up facing
        moveChar(0,1)
    















