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
define p = Character('Serena', color="#c13383")
define a = Character('Maeve', color="#e3a000")
define d = Character('Angela', color="#7b1ff6")
define i = Character("[povname]", color="#00ff00")



# The game starts here.
label start:

    # Programmer Introduction Starts
    scene bg office
    with fade


    "It’s 9:55 a.m. on the first day of my internship at Meteoric Games. They told me to be here at 10… The office is locked. No one is here yet."

    "Me" "Does everyone really arrive after 10…?"

    "I feel so silly. What if someone shows up and sees me standing here looking like a lost weirdo?"

    "Maybe I should go around the corner and get a coffee."

    "A third coffee."

    "Yeah, that’s what I’ll do."

    "When I turn around, I almost collide with a woman coming up the office stairs. I give a little yell, but the woman just laughs."

    show programmer happy
    with dissolve

    "???" "I guess you’re the fresh blood."

    show programmer normal

    "Me" "Is it really that obvious?"

    "???" "Well, you’re a little overdressed…"

    "I look down at the collared shirt and shiny gray pencil skirt I bought at Banana Republic last week. Then I look at the woman’s ensemble. It’s a little bit hip and a little bit goth. She looks like she just walked out of a 90s high school, but in a really good way."

    "Me" "I like your outfit!"

    show programmer happy

    "???" "Thanks. I got this shirt in Germany last time I visited my parents. I’m {color=#c13383}Serena{/color}, by the way. And as I recall, your name is…"

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

    hide programmer
    with dissolve

    "She unlocks the office door, and we head in."

    "The office's windows are huge, letting in lots of natural light. Its design is sleek and modern, in stark contrast to the messy desks lined up along the walls."

    i "What do you do here?"

    show programmer normal
    with dissolve

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

    p "So, {color=#e30000}programs{/color} are sequences of instructions that change the computer's data. That's all a program really is: data, and instructions that modify data."

    p "Let's talk about {color=#e30000}data{/color} first. Imagine you're looking at a spreadsheet. And this spreadsheet lists, hmm... inventory items. Yeah, items that are in your inventory."

    i "Okay. A spreadsheet listing items in my inventory."

    p "In one column, you have the {color=#e30000}item name.{/color} In the next column, you have the {color=#e30000}item's value{/color} in gil. I mean, gold. The item's value in gold."

    p "Then, the third column lists {color=#e30000}how many{/color} of that item you have."

    hide programmer

    "I imagine the spreadsheet in my head..."

    show programmer explain

    p "So the first column, the name, that's a piece of data. And the type of the data is text. In programming, though, we call that a {color=#e30000}string{/color}."

    p "The monetary value would be a {color=#e30000}floating-point number{/color}, meaning it's a number that can have precision after the decimal point. Like 10.25, or 1.50."

    p "So what type of data do you think the item count column would be?"

    $ prog_score = 0

label programmer_question_1_first:
    hide textframe

    show programmer normal at right
    with move

    menu:
        "Floating-point number.":
            jump programmer_wrong_1
        "Integer.":
            $ prog_score += 1
            jump programmer_right_1
        "String.":
            jump programmer_wrong_1
        "Number.":
            jump programmer_wrong_number

label programmer_question_1:
    hide textframe

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
    show programmer explain at center
    with move

    p "Not quite. Why don't you try again?"
    p "What type of data would an item count be?"
    jump programmer_question_1

label programmer_wrong_number:
    show programmer explain at center
    with move

    p "Almost, but that's not specific enough. Give it another shot."
    jump programmer_question_1

label programmer_right_1:
    show programmer happy at center
    with move

    p "That's right. Great job! The item count would be an {color=#e30000}integer.{/color}"

    show programmer explain

    p "If I wanted to declare an integer in code, I'd write this:"

    hide programmer

    "She types into the program: {color=#e30000}int count;{/color}"

    show programmer explain

    p "To declare a {color=#e30000}string{/color}, I'd write this."

    hide programmer

    "She types: {color=#e30000}String name;{/color}"

    show programmer explain

    p "And a {color=#e30000}floating-point{/color} number looks like this:"

    hide programmer

    "{color=#e30000}float value;{/color}"

    show programmer explain

    p "Okay, now I'm going to jump ahead a bit. Give me a minute..."

    hide programmer
    show sample_script_1

    p "So, what do you think is the value of the name variable at the end of this code segment?"

label programmer_question_2_first:
    hide textframe

    hide sample_script_1

    show programmer normal at right

    menu:
        "Plain Crossbow":
            jump programmer_wrong_2
        "Golden Crossbow":
            $ prog_score += 1
            jump programmer_right_2
        "nothing":
            jump programmer_wrong_2
        "1001.75":
            jump programmer_wrong_2

label programmer_question_2:
    hide sample_script_1
    show programmer normal at right
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
    show programmer happy at center
    with move

    p "Great job. Now let's try something else..."
    hide programmer
    show sample_script_2
    p "So, how many crossbows do I have at the end of this code segment?"

label programmer_question_3_first:
    hide sample_script_2

    show programmer normal at right


    menu:
        "3":
            jump programmer_wrong_3
        "2":
            jump programmer_wrong_3
        "1":
            $ prog_score += 1
            jump programmer_right_3
        "0":
            jump programmer_wrong_3

label programmer_question_3:
    hide sample_script_2

    show programmer normal at right

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
    show programmer happy at center
    with move

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
        $ prog_feelings = 2
        jump proceed_from_programmer_feelings
    "It was just okay.":
        $ prog_feelings = 1
        jump proceed_from_programmer_feelings
    "I don't think it's my thing.":
        $ prog_feelings = 0
        jump proceed_from_programmer_feelings

label proceed_from_programmer_feelings:
    "Hmmm..."

#Begin Animator Section
label artist_part_1:
    "???" "Lalala! LaLa~!"

    "There's a woman washing mugs out in the sink, humming exuberantly and shuffling her feet in time to the song."

    i "Hi!"

    show artist normal
    with dissolve

    "???" "La--Oh, gosh! Sorry, I was just thinking about my new routine and got carried away"

    i "Are you a dancer? Neat!"

    show artist happy

    "???" "Yeah, ballroom and Latin! Kinda my main hobby, working on movement when I'm not working on movement..."

    show artist normal

    "???" "But, wait, wait, back up. Are you the intern they told us about?"

    i "Yup, that's me."

    a "Nice to meetcha! I'm {color=#e3a000}Maeve{/color}--I'm the art lead on Astral War. You studying animation?"

    i "I'm kind of trying a little bit of everything right now. I guess I'm not really sure yet what I want to specialize in."

    a "I getcha--the generalist path! You interested in helping out on the art side of things?"

    i "I mean, I don't really know where to start."

    hide artist
    with dissolve

    "I follow her over to a computer, where she sits down and opens up a complicated looking program. The interface has approximately a bajillion menu options."

    #show art_image_maya

    "My face must reflect something of the consternation I feel, because {color=#e3a000}Maeve{/color} glances over at me and laughs."

    #hide art_image_maya

    show artist happy

    a "Don't worry. I know Maya looks intense, but trust me, spend a little time in any 3D package and it becomes second nature."

    show artist explain

    a "I'll just take you through the basics. Astal War is a 3D game, which means that we build and animate the art assets in a program like Maya before we bring them into the game engine."

    show artist normal

    a "What makes creating 3D for games different than making art for animated films is the computer has to render--or create--the images in real time as you are playing, instead of doing it all ahead of time."

    i "Yeah, I was reading this thing about Pixar, about the massive banks of computers they have to render their movie frame-by-frame."

    a "Totally! It takes days and days for that kind of detail. We don't get that luxury here, right? We have to carefully watch how many polygons are in a scene."

    i "Polygons? Like shapes?"

    show artist explain

    a "Every 3D model in a game is composed of a mesh of little many shapes called {color=#e3a000}POLYGONS{/color} which the engine calculates and draws. If you look at a game model's polygons, it looks like it is covered with a net of little squares, a \"wireframe.\""

    i "So when people talk about \"polycount,\" they are talking about how many of those square shapes there are?"

    show artist normal

    a "Exactly! So {color=#e3a000}MODELING{/color} is the job of building game assets using polygons."

    i "Sweet. So what are some of the other jobs on the art team?"

    show artist happy

    a "Well, there's drawing {color=#e3a000}CONCEPT ART{/color} \(That's a fun one\), there's {color=#e3a000}TEXTURING{/color} the model after it's created, there's {color=#e3a000}RIGGING{/color}--setting up the model so it can be animated, and {color=#e3a000}ANIMATION{/color}--adding movement to the model."

    "She waves her hands excitedly as she talks, and I wonder if all 3D artists get this animated when talking about animation. It's obviously something she's passionate about, and I'd like to find out more..."

    i "So... texturing?"

    show artist normal

    a "It's like painting on top of the model--a flat image that is wrapped around the shape to give it color and texture."

    #show art_image_texture

    a "There are different types of texture maps that do different things for the way a model is displayed."

    a "A {color=#e3a000}DIFFUSE MAP{/color} provides the diffuse color of the model, a {color=#e3a000}NORMAL MAP{/color} makes it bumpy, a {color=#e3a000}SPECULAR MAP{/color} controls how shiny it is, and an {color=#e3a000}ALPHA MAP{/color} lets the engine know which parts of the model should be rendered as transparent."

    #hide art_image_texture

    show artist explain

    a "So like, to double check, creating a {color=#e3a000}specular map{/color} would be part of which job?"

    hide artist explain
    $ art_score = 0

label art_question_1_first:
    show artist normal at right
    with move

    menu:
        "Modeling":
            jump art_wrong_1
        "Texturing":
            $ art_score += 1
            jump art_right_1
        "Rigging":
            jump art_wrong_1
        "Animation":
            jump art_wrong_1

label art_question_1:
    show artist normal at right
    with move

    menu:
        "Modeling":
            jump art_wrong_1
        "Texturing":
            jump art_right_1
        "Rigging":
            jump art_wrong_1
        "Animation":
            jump art_wrong_1

label art_right_1:
    show artist happy at center
    with move

    a "Bingo! Sorry for the info overload, just wanted to make sure I wasn't rambling too fast for ya."
    jump art_part_2

label art_wrong_1:
    show artist explain at center
    with move

    a "Mmm, not quite, try again."
    jump art_question_1

label art_part_2:
    show artist normal
    i "And you said {color=#e3a000}rigging{/color} was like setting up the character?"

    #show art_image_rig
    a "Yeah, it's getting it ready for animation, by putting joints inside it. Giving a character a \"skeleton\" and controls for the animator to move. It's like adding strings to a puppet!"

    i "A skeleton? Heehee... spooky!"

    #hide art_image_rig

    show artist explain

    a "Think of it this way. If a model is like a body, and a texture is the body's skin, then rigging is like the bones and muscles inside the body that allow it to move."
    a "Like, if you wanted to make a character's leg bend, what would you need to create?"

    hide artist explain

label art_question_2_first:
    show artist normal at right
    with move

    menu:
        "joints":
            $art_score += 1
            jump art_right_2
        "locators":
            jump art_wrong_2
        "materials":
            jump art_wrong_2
        "wireframes":
            jump art_wrong_2

label art_question_2:
    show artist normal at right
    with move

    menu:
        "Joints":
            jump art_right_2
        "Locators":
            jump art_wrong_2
        "Materials":
            jump art_wrong_2
        "Wireframes":
            jump art_wrong_2

label art_right_2:
    show artist happy at center
    with move

    a "Right on the money. Joints make everything all bendy and bouncy and great!"
    jump art_part_3

label art_wrong_2:
    show artist explain at center
    with move

    a "Not quite. I'll give you another guess."
    jump art_question_2

label art_part_3:
    a "And anyway, rigging gets the stuff ready for animation, which is my original background!"

    show artist explain

    a "Look up the 12 principles of animation. That'll get you started--same ideas hold true whether you are making animation in 2D or 3D, for games or for film."

    #show art_image_grapheditor
    a "I set keyframes on the character to define some important poses and then I open this menu, the trusty graph editor, to control the motion between those two poses."
    a "Timing, spacing--these curves represent the movement and rotation of all the character controls."

    #hide art_image_grapheditor
    #show
    a "So basically the graph editor a tool mostly for..."


label art_question_3_first:
    show artist normal at right
    with move

    menu:
        "Optimizing the topology of the model":
            jump art_wrong_3
        "Creating shaders":
            jump art_wrong_3
        "Giving fine control over the animation":
            $ art_score += 1
            jump art_right_3
        "Organizing the nodes of the scene":
            jump art_wrong_3

label art_question_3:
    show artist normal at right
    with move

    menu:
        "Optimizing the topology of the model":
            jump art_wrong_3
        "Creating shaders":
            jump art_wrong_3
        "Giving fine control over the animation":
            jump art_right_3
        "Organizing the nodes of the scene":
            jump art_wrong_3

label art_right_3:
    show artist happy at center
    with move

    a "You got it."
    jump art_part_4

label art_wrong_3:
    show artist explain at center
    with move

    a "Yeah, well, not really. There are other tools to do that."
    jump art_question_3

label art_part_4:

    show artist normal

    a "In games we often make short loops of movement that can be played seamlessly over and over as the player controls the characters. Cycles: walking, running, that sort of thing."

    a "There's not a lot different in principle from animating on paper, just like in the old days. We still focus on creating the illusion of movement on frame at a time."

    i "The Illusion of Life. I've got that textbook."

    show artist happy

    a "OMG, have you read it? It's like my favorite reference book ever. Those old men really knew their stuff."

    show artist normal

    a "So okay, I've probably just about talked your ear off. I'll let you get back to your studio tour, but if you wanna come back and learn more, I'll be right here."

    hide artist normal
    with dissolve

    "As I walk away, {color=#e3a000}Maeve{/color} gets absorbed in her work. I see her doing a weird motion with her arm, like she is testing the way her elbow bends, and then goes to make adjustments to the character on the screen."

    "Animators are kinda... different."

    "I think about if I want to do more of this stuff going forward."

menu:
    "It seemed really cool.":
        $ art_feelings = 2
        jump proceed_from_artist_feelings
    "It was just okay.":
        $ art_feelings = 1
        jump proceed_from_artist_feelings
    "I don't think it's my thing.":
        $ art_feelings = 0
        jump proceed_from_artist_feelings

label proceed_from_artist_feelings:
    "Yeah..."

    "There are people gradually filling up the office now. I should probably find Melinda, the producer I'm reporting to..."

    "Just as I start to try asking around, another woman comes up to me."

    show designer normal
    with dissolve

    "???" "Hey there. I understand you're the new apprentice?"

    "Compared to {color=#e30000}Serena{/color} and {color=#e3a000}Maeve{/color}, this woman seems a lot more... formal. I can somehow tell from her manner that she's an overachiever."

    i "That's me. Are you Melinda?"

    "???" "No, but Melinda should be in soon. I'm {color=#7b1ff6}Angela.{/color} Lead designer for Astral War."

    d "Since Melinda isn't here yet, I thought I'd check in and see if you had any questions."

    i "I do have a question, actually."

    d "What is it?"

    i "Well, er, what exactly... do you..."

    i "...do?"

    show designer happy
    "{color=#7b1ff6}Angela{/color} laughs."

    d "That's actually a very good question. {color=#7b1ff6}Game designers{/color} do a lot of things. One of my favorite things about this job is that I don't have a typical working day."

    show designer normal
    "She glances down at her smart watch."

    d "It looks like I have a few minutes before my 12 o'clock meeting. Why don't we sit at the lunch table and I'll try to give you a real answer?"

    i "I'd love that!"

    hide designer
    with dissolve

    "We sit down at the table together. It's kind of refreshing having face-to-face conversation for a bit, rather than looking at a screen."

    show designer explain
    with dissolve

    d "So the first thing to understand about game design is that it goes way beyond video games."

    show designer normal

    d "In fact, I got my start designing board games up in Montreal."

    i "Wow. I never thought about it that way, but it makes perfect sense."

    d "I'm glad you say that. Most people think that game design is programming and art. But in fact, the programmers and artists are just the minions who carry out my demands."

    show programmer normal at left
    with moveinleft

    p "I heard that!"

    hide programmer at left
    with moveoutleft

    show designer happy

    d "Much to {color=#e30000}Serena's{/color} chagrin."

    show designer normal

    d "So first let's talk about the game design process."
    d "It all starts with {color=#7b1ff6}research.{/color} My undergrad degree is in History and I have a Master's in Musicology, so I know quite a lot about research."

    i "That's a pretty interesting background for a game designer."

    d "It's more common than you might think. The best training for a game designer is a broad base of knowledge, plus a little bit of coding, writing, and art."
    d "I've worked really hard to be proficient in all of those skills. I'm not expert—that's what people like {color=#e30000}Serena{/color} and {color=#e3a000}Maeve{/color} are for—but I'm good enough to communicate my intentions through prototypes or sketches."

    show designer explain
    d "After we've gathered a lot of research, the next stage is {color=#7b1ff6}brainstorming{/color} and coming up with the {color=#7b1ff6}initial concept.{/color}"
    d "Part of that step is adding {color=#7b1ff6}constraints{/color}: we have deadlines, a budget, limits to our technical abilities. But often, constraints can actually make the creative process easier."
    d "We take an iterative approach here, which means we do a lot of {color=#7b1ff6}rapid protoyping{/color} to get feedback on our changes as quickly as possible."
    d "We iterate on the prototype many, many times before we move on to the {color=#7b1ff6}implementation stage{/color}—that is, building the actual game. Then we iterate on the implementation, too."

    show designer normal
    d "That way, we don't invest a lot of time in implementing a rule that people won't like."

    i "A rule?"

    show designer explain
    d "Yes. I'm using the term broadly. That brings us to some of the core principles of game design: What are the most basic elements of a game?"
    d "What do you think?"

    $ design_score = 0

label designer_question_1_first:
    show designer normal at right
    with move

    menu:
        "Graphics, sound, textures.":
            jump designer_wrong_1_graphics
        "Narrative, characters, endings.":
            jump designer_wrong_1_narrative
        "Players, objectives, rules.":
            $ design_score += 1
            jump designer_right_1
        "Levels, puzzles, combat.":
            jump designer_wrong_1_levels

label designer_question_1:
    show designer normal at right
    with move

    menu:
        "Graphics, sound, textures.":
            jump designer_wrong_1_graphics
        "Narrative, characters, endings.":
            jump designer_wrong_1_narrative
        "Players, objectives, rules.":
            jump designer_right_1
        "Levels, puzzles, combat.":
            jump designer_wrong_1_levels

label designer_wrong_1_graphics:
    show designer explain at center
    with move

    d "Not exactly. Those are all bells and whistles on top of the gameplay. Try again."
    jump designer_question_1

label designer_wrong_1_narrative:
    show designer explain at center
    with move

    d "Well, no. Those things help you form an emotional connection to the game."
    d "They can influence the gameplay, but they aren't the gameplay itself. Try again."
    jump designer_question_1

label designer_wrong_1_levels:
    show designer explain at center
    with move

    d "You're not wrong, exactly. Those are all things game designers work on."
    d "But they aren't the core elements of a game. Think more basic."
    jump designer_question_1

label designer_right_1:
    show designer happy at center
    with move

    d "Great answer! Players, objectives, and rules are three of the formal elements of gameplay."
    show designer normal
    d "There are several possible types of {color=#7b1ff6}player structures.{/color} Here at Meteoric, all our games are {color=#7b1ff6}single-player{/color}, which means they have a player structure called {color=#7b1ff6}solitaire.{/color}"

    i "Like the card game?"

    show designer explain
    d "Exactly. Just like a single-player video game, solitaire involves a single actor interacting with the game system."
    d "Another player structure is {color=#7b1ff6}PvE, player vs. environment,{/color} where multiple players are pitted against the game system cooperatively. Some MMOs fit that category."
    d "And other MMOs fit a different category: {color=#7b1ff6}PvP,{/color} also called a {color=#7b1ff6}free-for-all{/color}, which is player vs. player vs. player and so on."
    show designer normal
    d "Can you give me an example of a game and tell me what its player structure is?"


label designer_question_2_first:
    show designer at right
    with move

    menu:
        "Hide and seek is PvE.":
            jump designer_wrong_2_hideseek
        "Monopoly is a free-for-all":
            $ design_score += 1
            jump designer_right_2
        "Blackjack is head-to-head, one player vs. another.":
            jump designer_wrong_2_blackjack

label designer_question_2:
    show designer at right
    with move

    menu:
        "Hide and seek is PvE.":
            jump designer_wrong_2_hideseek
        "Monopoly is a free-for-all":
            jump designer_right_2
        "Blackjack is head-to-head, one player vs. another.":
            jump designer_wrong_2_blackjack

label designer_wrong_2_hideseek:
    show designer explain at center
    with move

    d "Hide and seek is kind of a complicated example, but it isn't PvE because players aren't all on the same side."
    d "Since one person is \"it\" and everyone else is trying to hide from them, it's more like a one-against-many structure."
    d "Try again with another game."
    jump designer_question_2

label designer_wrong_2_blackjack:
    show designer explain at center
    with move

    d "Close! But actually, in blackjack, all of the dealer's moves are deterministic. So it's more like player vs. game system."
    d "Try again with a different example."
    jump designer_question_2

label designer_right_2:
    show designer happy at center
    with move
    d "Exactly. Monopoly is an example of a free-for-all game."

    show designer explain
    d "So, you have the player structure, then you have the {color=#7b1ff6}objectives,{/color} or the {color=#7b1ff6}conditions for winning and losing.{/color}"
    d "There are many different types of {color=#7b1ff6}winning conditions,{/color} as you probably know. In narrative video games like the ones we do at Meteroic, this tends to be simple: make it to the end of the game."
    d "But there are also games where the winning condition is controlling a certain amount of territory or collecting a certain amount of currency."
    d "Players achieve objectives by making decisions within the constraints of the game rules, or {color=#7b1ff6}mechanics.{/color}"

    show designer normal
    d "Game mechanics are the biggest part of my job. Once we have our first prototype, the rest of the process is spent tweaking, refining, and balancing the mechanics."
    d "I need to consider things like modulating difficulty as the game progresses, providing appropriate rewards for player skill, whether the game mechanics support the narrative or feel out of place, and of course, whether or not the game is fun."
    d "Then again, fun isn't a requirement for all game design."
    d "Have you ever heard of Pathologic? It's not a fun game at all, but it's genius. And it's a great example of mechanics that blend seamlessly with the narrative."

    i "I haven't heard of it. I'll check it out."

    d "I highly recommend you do. There's also an episode of Extra Credits called \"Narrative Mechanics\" that dives a little deeper into the relationship between, well, narrative and mechanics."
    d "So, that was a pretty long answer to your question, but did I answer it adequately? Do you know what a game designer does now?"


label designer_question_3_first:
    show designer at right
    with move

    menu:
        "Yeah. They design and iterate on gameplay mechanics.":
            $ design_score += 1
            jump designer_right_3
        "Yeah. They come up with ideas for games.":
            jump designer_wrong_3
        "Yeah. They create the characters and game world.":
            jump designer_wrong_3
        "Yeah. They tell programmers and artists what to do.":
            jump designer_wrong_3

label designer_question_3:
    show designer at right
    with move

    menu:
        "Yeah. They design and iterate on gameplay mechanics.":
            jump designer_right_3
        "Yeah. They come up with ideas for games.":
            jump designer_wrong_3
        "Yeah. They create the characters and game world.":
            jump designer_wrong_3
        "Yeah. They tell programmers and artists what to do.":
            jump designer_wrong_3

label designer_wrong_3:
    show designer explain at center
    with move

    d "That's not really the heart of a game designer's job. Do you remember the other stuff we talked about?"
    show designer normal
    jump designer_question_3

label designer_right_3:
    show designer happy at center
    with move

    d "That's right! You learned well."
    show designer normal
    d "Alright, looks like it's time for my 12 o'clock. I'll bring you over to Melinda first so you can get your formal orientation."

    hide designer
    with dissolve

    "I spend the rest of the day with Melinda, the producer, learning more about Meteoric's current projects."

    "At the end of the day, looking back on what I learned about game design, I think to myself..."

menu:
    "It seemed really cool.":
        $ design_feelings = 2
        jump endings
    "It was just okay.":
        $ design_feelings = 1
        jump endings
    "I don't think it's my thing.":
        $ design_feelings = 0
        jump endings

label endings:
    scene bg office
    with fade

    "The next day, when I sit down at lunch table with my food, I'm joined by an unexpected visitor."

    $ prog = prog_score * prog_feelings
    $ art = art_score * art_feelings
    $ design = design_score * design_feelings

    if prog >= art and prog >= design:
        jump programmer_ending

    if art >= prog and art >= design:
        jump artist_ending

    if design >= art and design >= prog:
        jump designer_ending

label programmer_ending:
    show programmer normal
    p "Hey girl. Hope you don't mind me invading your space, because I'm about to."

    "{color=#e30000}Serena{/color} sits down next to me."

    i "Of course not. How are you, {color=#e30000}Serena?{/color}"

    p "Peachy. I was just thinking, you seemed pretty interested in codeworld yesterday, and you took to it pretty fast."

    show programmer explain
    p "We have a little bandwidth right now for training. If you want, I could talk to Melinda about working some engineering into your internship."
    p "I can't guarantee you'll be a pro by the time you leave, but we'll def teach you enough that you can push a bugfix or two into the Astral War repo."
    p "What do you say?"

    i "I'd love that! Thank you so much, Serena!"

    show programmer happy
    p "Awesome, I'll run it by her this afternoon. In the meantime, let's talk cats."

    hide programmer
    with dissolve

    "I spent the rest of the summer helping Melinda get Astral War out the door. But as the months wore on and May turned to August, I found myself spending more and more time with {color=#e30000}Serena's{/color} team."
    "{color=#e30000}Serena{/color} took me under her wing and taught me so much more about programming than I ever thought possible in just one summer."
    "This fall, I'm planning on adding some Computer Science classes to my schedule. {color=#e30000}Serena{/color} says I might even be able to place out of CS101, the introductory course for the major."
    "Who knows? Maybe code will turn out to be my lifelong passion."

    return

label artist_ending:
    show artist happy

    a "OMG HIIII [povname]!"

    show artist normal

    "She looks down at my lunch."

    a "Ooh that looks tasty! I'm jealous."

    i "Thanks."

    show artist happy

    a "Yeah!"

    i "..."
    i "So..."
    i "What's up?"

    show artist normal

    a "Oh, right! I was wondering if you wanted to be under my wings?"

    i "What?"

    show artist happy
    a "You know what I mean. I could teach you some stuff. About art. While you're here."
    a "I'll ask Melinda if I can borrow you sometimes, and you can help on the art side."
    a "It seemed like you were interested, so I thought I'd at least ask. What do you think?"

    i "I'd be honored. Thank you so much, {color=#e3a000}Maeve.{/color}"

    a "No prob. I'll talk to Melinda about it later today."
    show artist happy
    a "In the meantime, let's eat!"
    hide artist
    with dissolve

    "I spent the rest of the summer helping Melinda get Astral War out the door. But as the months wore on and May turned to August, I found myself spending more and more time \"under {color=#e3a000}Maeve's{/color} wings,\" as she would say."
    "{color=#e3a000}Maeve{/color} and her team taught me so much more about art and animation than I ever thought possible in just one summer."
    "This fall, I'm planning on adding some Visual Arts classes to my schedule. I might even take night classes in 3D Animation at the art school downtown."
    "Who knows? Maybe animation will turn out to be my lifelong passion."

    return

label designer_ending:
    d "Placeholder ending with designer."

    return

