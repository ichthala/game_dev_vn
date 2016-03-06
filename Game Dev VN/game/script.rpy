# Background Images
image bg office = "bgOffice.jpg"

# Sprites
image programmer happy = "programmer_happy.png"
image programmer  normal = "programmer_normal.png"
image programmer  explain = "programmer_explain.png"
image artist happy = "artist_happy.png"
image artist normal = "artist_normal.png"
image artist  explain = "artist_explain.png"
image designer happy = "artist_happy.png"
image designer normal = "designer_normal.png"
image designer explain = "designer_explain.png"

# Characters.
define p = Character('Programmer', color="#c8c8ff")
define a = Character('Artist', color="#c8c8ff")
define d = Character('Designer', color="#c8c8ff")
define i  = Character("[povname]", color="#c8c8ff")

# The game starts here.
label start:
    
    # Programmer Introduction Starts 
    scene bg office
    "???" "Hello World"

    #start input script
    python:
        povname = renpy.input("What is your name?")
        povname = povname.strip()

        if not povname:
            povname  = "..."

    i "Hi, I'm [povname]"
    
    show  programmer normal
    p  "Intro Dialogue"
 
    show  artist happy
    a "More Intro Dialogue"    

    return
