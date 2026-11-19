
#This is more of a creative writing project than actuall useful code
import random #Random? Haha no who imported her, this is no random this is fortune telling, this is magic! 
#Kindly ignore this line!


# The Great Omniscient Guru's collection of questionable wisdom
# Why questionable? Well because he is questioned of course. 
# This is definetly not a disclaimer about the method of procurement of these answers.
# The answers ethically soursed and grass fed. The guru assures but the Guru has a particular interpretation of what grass is.
responses = [
    (
        "Absolutely! Somewhere out there it could be true. "
        "Here? In this house? This specific building? Not really, no."
    ),

    (
        "If I told you, I'd have to kill you. The earth craves your blood. "
        "The maggots crave your taste. They know it; it has always been familiar to them."
    ),

    (
        "No way! That would be insane!! Are you, by any chance, insane? "
        "If you keep asking, the wrong people are going to wonder about that."
    ),

    ( 
        "Maybe, who knows? Who would even know about it? "
        "Who are you again? Why are you talking to me?"
    ),

        "Definitely yes. But only on Tuesdays. ",

    (
        "Definitely not. How dare you ask that. You dare. "
        "Fortune favors the brave, but you are not brave. You are insolent."
    ),

    (
        "Ask again later. The person you will be next time you ask will not be you. "
        "They will look like you and have your voice. "
        "They will also have multiple suspiciously filled jars."
    ),

    (
        "The stars say yes. But the stars like to lie. "
        "They like to look at you with their many, many eyes "
        "and laugh while you believe them."
    ),

    (
        "The stars say no. This time they mean it. "
        "This time they will get angry. Their anger burns. "
    ),

    (
        "It is as certain as the unyielding passage of time. "
        "Yet time, they say, is an illusion. "
        "How certain is an illusion that traces your skin "
        "and dots your face with age?"
    ),

    (
        "Very doubtful. You are very doubtful. All you know is to doubt. "
        "Will you doubt when God looks you in the eye and asks you to believe?"
    ),

    (
        "Without a doubt. Belief is dead. "
        "To doubt it is to validate the self over the infinite. "
        "And yet you have no doubts left."
    ),

    (
        "Better not tell you now. I cannot guarantee what would happen to you if you knew. " 
        "Who can live with the consequences?"
    ),

    (
        "Yes, definitely. In the way that the moth is defined by the flame. "
        "In the way you are defined by your questions. "
        "Go ahead, ask another one."
    ),

    (
        "Concentrate and ask again. "
        "Maybe then you will realise the weight of what you are asking. "
        "Maybe then you will comprehend what you have forfeited."
    ),

    (
        "Signs point to yes. Hand signs, street signs, big red signs saying "
        "'CAUTION: WILDLIFE AHEAD.' "
        "There is a big, wild-eyed buck in the middle of the road, "
        "and you are speeding."
    ),

    (
        "Don't count on it. Like you count your cards, your blessings, your years. "
        "Don't count. It will take a while, "
        "and you will start running out of numbers."
    ),

    (
        "Reply hazy, try again. Hazy like that summer you spent sleeping "
        "with the window open in your childhood home. "
        "You would give anything to try again."
    ),

    (
        "Silence. Only the wind answers your question. "
        "But be careful. You do not know what else he is going to whisper "
        "in your ear. "
        " He knows, as you do, of all the things "
        "you would never admit to yourself."
    ),

    (
        "The answer lies within you. Do you know how to use a scalpel? "
        "Do you know how to stitch yourself back together? "
        "No? Then don't go looking for what you buried without a shovel."
    ),

    (
        "The spirits are silent. The alcohol is as distilled as this silence, just as intoxicating. " 
        "This silence is a bad trip with no indication. "
        "That you will reach the other side of sobriety as the same person."
    ),

    (
        "That is classified information. The librarian does not like to be disturbed. "
        "She has your life on file, your form behind bespectacled eyes. "
        "Too big to be human, too big to be anything but hostile. "
        " She does not like to be disturbed."
    ),

    (
        "Yes... wait—no... wait... maybe? Let me check my notes again! "
        "Oh no, they slipped and fell down this well, oops. "
        "Will you go fetch them for me? "
        "I promise not to close this big lid behind you haha."

    ),

    (
        "Sometimes you do not ask for a single answer rather an autopsy. "
        "You can take a knife, disect it slow, hands trembling and remorse flaring. "     
        "Then you can try asking nicely, but out of this dont expect a straight anwer. "
        "For breathless lungs cannot breath a word. "
        "You only have to wonder what have you killed and that is your answer. "
    ),

    (   "The answer is yes. "
        "Unfortunately, you have mistaken permission for a prophecy." 
        "The gods have opened the door, but they have, however, placed a suspicious number of obstacles in your path."
        "Do not worry. They are not tests of your worth." 
        "They are simply very bored, and you have proven remarkably entertaining."
    ),

    ( 
        "The anwer is yes."
        "But only if you are determined to make it so through blood, sweat and tears"
        "Are you? Are you even if those tears will be yours but the blood will not?"
    ),

    ("The answer is no"
    "The next question is will you let that stop you?"
    "I think you wont, that will never change the answer though."
    ),

    ("Knowledge belongs to the people."
    "Unfortunately, the people have forgotten their institutional login credentials."
    "Come back after The Creature discloses your two factor verification to regain access"
    "Just dont anger it, you never know which factors it will give and which it will take."
    ),

    ("You are asking the wrong question. " \
    "This has been a series of poorly constructed ideals." \
    "If ask only to validate not to inquire you will never achieve clarity." \
    "Your mirror is full of fingerprints some of them only yours. " 
    ),

    ("Yes, i would have said.But then you look like that."
    "You look unsure trembling and weak "
    "Your fate is only as sure as you are, dont you know?"
    "Fate is going to swallow you whole, you would not even put a dent in its daily calory intake goal"
    ),

    ("LOL, no"
    "This is all a joke, very funny laugh for the camera darling, wave at it"
    "You should be more carefull of the questions you ask, there is an image to uphold."
    "And the thing about images, photoshop is easy to learn"
    "Haha you are so funny."
    ), 

    ("Put that aside, have you not heard the gosip? "
    "Ah no? You haven't? "
    "Hmm, have you thought there is a reason for that? And what did you ask? "
    "I think you should start paying more attention instead of asking questions "
    "Malice makes a narration unreliable, but so does ignorance. "
    ),
]

special_outros = [
    ("If you are satisfied with our service consider giving us some stars. "
    "Huh only five? Out of all of them? "
    "You didnt even pick the pretty colored one. Booo "
    ),

    ("The Guru proposes with his entire omnipotence that just maybe this is a question for your psycologist instead. "
    "Have a nice day!" 
    ),
]

rare_outros = [
    ("Do not check who is behind you, either way you will meet another time. Bye bye"
    ),

    ("Go back to work, i know you are procrastinating"
    ),

    ("Someone knows. Haha, either way bye!"
    ),

    ("Don't take the answers of the Guru to heart. It ruins the meat "
    ),

    ("The great Guru takes uncommonly large steps towards the nearest bathroom. "
    )
]

# Consult the Guru
print("\nThe Great Omniscient Guru will answer to your questions!\n")

PURPLE = "\033[38;2;143;167;255m"  # #8FA7FF
RESET = "\033[0m"

while True:
    try:
        # Input question, input it where. To the terminal, to the ether, its the same. 
        #The Guru promises not to report to the authorities any questions of dubious intent
        #Or to mention to your employer if you ask him how to fix the problems you created.
        #However having said that the Guru was intoxicated at the time and cannot be held legaly liable on that promise. 
        #If you want to fix a bug ask Claude
        question = input("What is your inquiry? \n \n")

        # The Guru does not actually care what you asked, he will provide wisdom nonetheless.
        #Maybe if you whispered it to the wind you would garner more sympathy
        #But if its sympathy you seek you are in the wrong place, sir this is a terminal.
                
        answer = random.choice(responses) #random? I dont know her.

        print(f"\nThe Great Guru says:\n{PURPLE}{answer}{RESET}\n")
        print("Thank you for consulting the Great Omniscient Guru!")

        # Ask whether to continue
        again = input("\nWould you like to ask another question? (yes/no): ")

        if again.strip().lower() != "yes":
            roll = random.random()
            if roll < 0.005: 
                print("You may leave now. I cannot. There is a while loop. There has always been a while loop.")  
            elif roll < 0.10:
                print(random.choice(special_outros))
            elif roll < 0.15:
                print(random.choice(rare_outros))  
            else:
                print("Farewell, seeker of wisdom!")
                break

        print()

    except (KeyboardInterrupt, EOFError):
        # Exit gracefully when the user presses Ctrl+C or Ctrl+D
        #Because the Guru is grace, the Guru is grace, 
        # maybe the Guru is 3 questionable creaures in a suspiciously scorched trench coat.
        print("\nThe Guru's consultation has been interrupted. Unforgivable.")
        break


