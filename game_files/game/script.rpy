# Background Images
image bg office = "bgOffice.jpg"

# Sprites
image programmer happy = "programmer_happy.png"
image programmer normal = "programmer_normal.png"
image programmer explain = "programmer_explain.png"
image artist happy = "artist_happy.png"
image artist normal = "artist_normal.png"
image artist explain = "artist_explain.png"
image designer happy = "artist_happy.png"
image designer normal = "designer_normal.png"
image designer explain = "designer_explain.png"

# Non-Sprite Images
image sample_script_1 = Image("sample_script_1.png", yalign=0.35)
image sample_script_2 = Image("sample_script_2.png", yalign=0.25)
image textframe = "textframe.jpg"
#image art_image_maya = Image("art_image_maya.png")
#image art_image_texture = Image("art_image_texture.png")
#image art_image_rig = Image("art_image_rig.png")
#image art_image_grapheditor = Image("art_image_grapheditor.png")

# Characters
define p = Character('Serena', color="#00ff00")
define a = Character('Artist', color="#00ff00")
define d = Character('Designer', color="#00ff00")
define i = Character("[povname]", color="#00ff00")



# The game starts here.
label start:

    # Programmer Introduction Starts
    scene bg office
    with dissolve

    "It’s 9:55 a.m. on the first day of my internship at GameCompany. They told me to be here at 10… The office is locked. No one is here yet."

    "Me" "Does everyone really arrive after 10…?"

    "I feel so silly. What if someone shows up and sees me standing here looking like a lost weirdo?"

    "Maybe I should go around the corner and get a coffee."

    "A third coffee."

    "Yeah, that’s what I’ll do."

    "When I turn around, I almost collide with a woman coming up the office stairs. I give a little yell, but the woman just laughs."

    show programmer happy
    with dissolve
    
    show textframe

    "???" "I guess you’re the fresh blood."

    show programmer normal

    "Me" "Is it really that obvious?"

    "???" "Well, you’re a little overdressed…"

    "I look down at the collared shirt and shiny gray pencil skirt I bought at Banana Republic last week. Then I look at the woman’s ensemble. It’s a little bit hip and a little bit goth. She looks like she just walked out of a 90s high school, but in a really good way."

    "Me" "I like your outfit!"

    show programmer happy

    "???" "Thanks. I got this shirt in Germany last time I visited my parents. I’m Serena, by the way. And as I recall, your name is…"

    #start input script
    python:
        povname = renpy.input("What is your name?")
        povname = povname.strip()

        if not povname:
            povname  = "Lucy"

    p "[povname], right?"

    i "Wow. Good memory!"

    show programmer normal

    p "Yeah. It helps with the job."

    "She unlocks the office door, and we head in."

    "The office's windows are huge, letting in lots of natural light. Its design is sleek and modern, in stark contrast to the messy desks lined up along the walls."

    i "What do you do here?"

    p "I'm the engineering lead for Astral War."

    "Whoa..."

    "I'm trying not to look too star-struck."

    i "That's amazing."

    p "So what are you here for, [povname]?"

    i "Um..."

    i "The truth is, I'm not really sure. I got this internship because I made a short documentary about competitive gaming for school, and the hiring manager, Ayla, loved it."

    i "I know I want to work in games, but I don't have any experience yet. The whole point of this internship is to try and figure out exactly what I want to do."

    i "I think I'm going to be reporting to one of the producers, but Ayla said I'll have room to explore a lot of different options while I'm here."

    p "Cool. You ever done any coding before?"

    i "No..."

    p "Want to learn?"

    i "Right now...?"

    p "Sure. You'd be surprised how much you can learn in a short time."

    p "A lot of people think you need to be some kind of reclusive genius to code. But look at me. I'm not reclusive."

    i "Um..."

    hide programmer

    "She sits down at a desk that's nearly empty except for a mug that says \"Animal Haven\" on it. Then she pulls up an extra chair."

    show programmer normal

    p "Have a seat and we'll get started."

    hide programmer

    "I sit down next to her, feeling a little nervous. She opens up a program that looks kind of like Notepad, but more intense."

    show programmer explain

    p "So, programs are sequences of instructions that change the computer's data. That's all a program really is: data, and instructions that modify data."

    p "Let's talk about data first. Imagine you're looking at a spreadsheet. And this spreadsheet lists, hmm... inventory items. Yeah, items that are in your inventory."

    i "Okay. A spreadsheet listing items in my inventory."

    p "In one column, you have the item name. In the next column, you have the item's value in gil. I mean, gold. The item's value in gold."

    p "Then, the third column lists how many of that item you have."

    hide programmer

    "I imagine the spreadsheet in my head..."

    show programmer explain

    p "So the first column, the name, that's a piece of data. And the type of the data is text. In programming, though, we call that a string."

    p "The monetary value would be a floating-point number, meaning it's a number that can have precision after the decimal point. Like 10.25, or 1.50."

    p "So what type of data do you think the item count column would be?"


label programmer_question_1:
    hide programmer
    with dissolve
    
    scene bg office
    
    show programmer normal at right
    with move
    
    
    menu:
        "Floating-point number.":
            jump programmer_wrong_1
        "Integer.":
            jump programmer_right_1
        "String.":
            jump programmer_wrong_1
        "Number.":
            jump programmer_wrong_number

label programmer_wrong_1:
    show programmer explain at right
    
    p "Not quite. Why don't you try again?"
    jump programmer_question_1

label programmer_wrong_number:
    p "Almost, but that's not specific enough. Give it another shot."
    jump programmer_question_1

label programmer_right_1:
    scene bg office
    with dissolve
    
    show programmer happy

    p "That's right. Great job! The item count would be an integer."

    show programmer explain

    p "If I wanted to declare an integer in code, I'd write this:"

    hide programmer

    "She types into the program: int count;"
    
    show programmer explain

    p "To declare a String, I'd write this."

    hide programmer

    "She types: String name;"
    
    show programmer explain

    p "And a floating-point number looks like this:"
    
    hide programmer

    "float value;"
    
    show programmer explain

    p "Okay, now I'm going to jump ahead a bit. Give me a minute..."

    hide programmer
    show sample_script_1

    p "So, what do you think is the value of the name variable at the end of this code segment?"

label programmer_question_2:
    hide sample_script_1
    show programmer normal at right
    with move
    
    menu:
        "Plain Crossbow":
            jump programmer_wrong_2
        "Golden Crossbow":
            jump programmer_right_2
        "nothing":
            jump programmer_wrong_2
        "1001.75":
            jump programmer_wrong_2

label programmer_wrong_2:
    show sample_script_1
    hide programmer
    
    p "Not quite. Why don't you try again?"
    jump programmer_question_2

label programmer_right_2:
    hide programmer
    with dissolve
    
    show programmer happy
    p "Great job. Now let's try something else..."
    hide programmer
    show sample_script_2
    p "So, how many crossbows do I have at the end of this code segment?"

label programmer_question_3:
    hide sample_script_2
    
    show programmer normal at right
    with move
    
    menu:
        "3":
            jump programmer_wrong_3
        "2":
            jump programmer_wrong_3
        "1":
            jump programmer_right_3
        "0":
            jump programmer_wrong_3

label programmer_wrong_3:
    show sample_script_2
    hide programmer
    
    p "Not quite. Why don't you try again?"
    jump programmer_question_3

label programmer_right_3:
    scene bg office
    with dissolve
    
    show programmer happy

    p "Awesome! See, that's all there is to it."

    i "Really?"

    show programmer normal

    p "Well, no. It gets a lot more complicated than that. But these are the building blocks for everything that comes after."

    p "We got through all the basics, and I haven't even had my morning coffee yet. Why don't I show you around the kitchen?"
    
    hide programmer

    "She picks up the mug from her desk."
    
    show programmer normal

    i "What's Animal Haven?"

    p "Oh, that's the animal shelter where I volunteer on the weekends. If you like animals, you should join me some time. We could use the help."
    
    hide programmer
    with dissolve

    "She shows me around the kitchen: snacks, coffee machine, water cooler. I'm starting to really like this place."
    

    "Looking back on what I learned about programming, I think to myself..."

menu:
    
    "It seemed really cool.":
        jump proceed_from_programmer_feelings
    "It was just okay.":
        jump proceed_from_programmer_feelings
    "I don't think it's my thing.":
        jump proceed_from_programmer_feelings

label proceed_from_programmer_feelings:
    "Hmmm..."

#Begin Animator Section
label artist_part_1:
    "???" "Lalala! LaLa~!"

    "There's a woman washing mugs out in the sink, humming exuberantly and shuffling her feet in time to the song."

    i "Hi!"

    show artist normal

    "???" "La--Oh, gosh! Sorry, I was just thinking about my new routine and got carried away"

    i "Are you a dancer? Neat!"

    show artist happy
    
    "???" "Yeah, ballroom and Latin! Kinda my main hobby, working on movement when I'm not working on movement..."
    
    show artist normal
    
    "???" "But, wait, wait, back up. Are you the intern they told us about?"

    i "Yup, that's me."

    a "Nice to meetcha! I'm Maeve--I'm the art lead on Astral War. You studying animation?"

    i "I'm kind of trying a little bit of everything right now. I guess I I'm not really sure yet what I want to specialize in."

    a "I getcha--the generalist path! You interested in helping out on the art side of things?"

    i "I mean, I don't really know where to start."

    "I follow her over to a computer, where she sits down and opens up a complicated looking program. The interface has approximately a bajillion menu options."

    #show art_image_maya

    "My face must reflect something of the consternation I feel, because Maeve glances over at me and laughs."

    #hide art_image_maya
    
    show artist explain

    a "Don't worry. I know Maya looks intense, but trust me, spend a little time in any 3D package and it becomes second nature."

    a "I'll just take you through the basics. Astal War is a 3D game, which means that we build and animate the art assets in a program like Maya before we bring them into the game engine."

    show artist normal

    a "What makes creating 3D for games different than making art for animated films is the computer has to render--or create--the images in real time as you are playing, instead of doing it all ahead of time."

    i "Yeah, I was reading this thing about Pixar, about the massive banks of computers they have to render their movie frame-by-frame."

    a "Totally! It takes days and days for that kind of detail. We don't get that luxury here, right? We have to carefully watch how many polygons are in a scene."

    i "Polygons? Like shapes?"

    show artist explain
    
    a "Every 3D model in a game is composed of a mesh of little many shapes called POLYGONS which the engine calculates and draws. If you look at a game model's polygons, it looks like it is covered with a net of little squares, a \"wireframe.\""

    i "So when people talk about \"polycount,\" they are talking about how many of those square shapes there are?"

    show artist normal

    a "Exactly! So MODELING is the job of building game assets using polygons."

    i "Sweet. So what are some of the other jobs on the art team?"

    show artist happy

    a " Well, there's drawing CONCEPT ART \(That's a fun one\), there's TEXTURING the model after it's created, there's RIGGING--setting up the model so it can be animated, and ANIMATION--adding movement to the model."

    "She waves her hands excitedly as she talks, and I wonder if all 3D artists get this animated when talking about animation. It's obviously something she's passionate about, and I'd like to find out more..."

    i "So...Texturing?"
    
    show artist normal
    
    a "It's like painting on top of the model--a flat image that is wrapped around the shape to give it color and texture."

    #show art_image_texture

    a "There are different types of texture maps that do different things for the way a model is displayed."

    a "A DIFFUSE MAP provides the diffuse color of the model, a NORMAL MAP makes it bumpy, a SPECULAR MAP controls how shiny it is, and an ALPHA MAP lets the engine know which parts of the model should be rendered as transparent."

    #hide art_image_texture

    show artist explain

    a "So like, to double check, creating a specular map would be part of which job?"

    hide artist explain

label art_question_1:
    menu:
        "Modeling":
            jump art_wrong_1
        "Texturing":
            jump art_right_1
        "Riggin":
            jump art_wrong_1
        "Animation":
            jump art_wrong_1


label art_right_1:
    show artist happy
    a "Bingo! Sorry for the info overload, just wanted to make sure I wasn't rambling too fast for ya."
    jump art_part_2

label art_wrong_1:
    show artist explain
    a "Mmm, not quite, try again."
    jump art_question_1

label art_part_2:
    
    show artist normal
    
    i "And you said rigging was like setting up the character?"

    #show art_image_rig

    a "Yeah, it's getting it ready for animation, by putting joints inside it. Giving a character a \"skeleton\" and controls for the animator to move. It's like adding strings to a puppet!"

    i "A skeleton? Heehee...spooky!"

    #hide art_image_rig
    
    show artist explain
    
    a "Think of it this way. If a model is like a body, and a texture is the body's skin, then rigging is like the bones and muscles inside the body that allow it to move."

    a "like, if you wanted to make a character's leg bend, what would you need to create?"

    hide artist explain

label art_question_2:
    menu:
        "joints":
            jump art_right_2
        "locators":
            jump art_wrong_2
        "materials":
            jump art_wrong_2
        "wireframes":
            jump art_wrong_2
        
label art_right_2:
    show artist happy
    a "Right on the money. Joints make everything all bendy and bouncy and great!"
    jump art_part_3
label art_wrong_2:
    show artist explain
    a "Not quite. I'll give you another guess."
    jump art_question_2

label art_part_3:
    a "And anyway, rigging gets the stuff ready for animation, which is my original background!"

    a "Look up the 12 principles of animation. That'll get you started--same ideas hold true whether you are making animation in 2D or 3D, for games or for film."

    #show art_image_grapheditor
    a "I set keyframes on the character to define some important poses and then I open this menu, the trusty graph editor, to control the motion between those two poses."

    a "Timing, spacing--these curves represent the movement and rotation of all the character controls."
    
    #hide art_image_grapheditor
    #show 
    a "So basically the graph editor a tool mostly tor?"

label art_question_3:
    menu:
        "Optimizing the topology of the model":
            jump art_wrong_3
        "Creating shaders":
            jump art_wrong_3
        "Giving fine control over the animation":
            jump art_right_3
        "Organizing the nodes of the scene":
            jump art_wrong_3
        
label art_right_2:
    show artist happy
    a "You got it."
    jump art_part_4
label art_wrong_2:
    show artist explain
    a "Yeah, well, not really. There are other tools to do that."
    jump art_question_3

label art_part_4:
    
    show artist normal
    
    a "In games we often make short loops of movement that can be played seamlessly over and over as the player controls the characters. Cycles--Walking, running, that sort of thing."

    a "There's not a lot different in principle from animating on paper, just like in the old days. We still focus on creating the illusion of movement on frame at a time." 

    i "The Illusion of Life. I've got that textbook."

    show artist happy
    
    a "OMG, have you read it? It's like my favorite reference book ever. Those old men really knew their stuff."

    show artist normal

    a "So okay, I've probably just about talked your ear off. I'll let you get back to your studio tour, but if you wanna come back and learn more, I'll be right here."

    hide artist normal

    "As I walk away, Maeve gets absorbed in her work. I see her doing a weird motion with her arm, like she is testing the way her elbow bends, and then goes to make adjustments to the character on the screen." 

    "Animators are kinda...different."

    "I think about if I want to do more of this stuff going forward."

menu:
    "It seemed really cool.":
        jump proceed_from_artist_feelings
    "It was just okay.":
        jump proceed_from_artist_feelings
    "I don't think it's my thing.":
        jump proceed_from_artist_feelings

label proceed_from_artist_feelings:
    "Yeah..."

return
