# -*- coding: utf-8 -*-
"""comp sci text adventure.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ImRgHPVYF7x1iObqbIMxOawD2hLJKnHa
"""

import sys
#import sys allows for me to stop the code from running when you die on one path while the other paths keep going
proper_base_skill_point = 1
print "--Your eyes flutter open and you wake up from your deep slumber. You sit up from where you were laying on the forest floor. In front of you is a dusty, blue blob.--"
player_name = raw_input("?: What is your name, young one? ")
print "\n"
print "?: It's an honor to meet you, " + str(player_name) + ", but let me tell you right here. You're a wizard."
print "?: Your parents were the greatest wizards to ever live, but they unfortunately met their end at the hands of a dark wizard named Azel."
response_onelife = 1
while response_onelife >= 1:
  response_one = raw_input("You: (How? / I understand) ")
  print "\n"
  if response_one == "How?" or response_one == "how?" or response_one == "how":
    response_onelife = response_onelife - 1
    print "?: You want to know how?"
    print "?: Well...it's rumored that they were targeted by Azel. Your parents fought valiently...but it wasn't enough for them to survive."
    print "You: I see..."
    print "Komi: Oh -- sorry. I'm Komi, a spirit without form, sadly. I'm here to guide you through your adventure, if you have the guts, anyway."
    print "You: It's nice to meet you."
    print "Komi: Yes, yes, but besides the greetings and introductions now, let's get to the real business."
  elif response_one == "I understand" or response_one == "i understand" or response_one == "understand" or response_one == "ok":
    response_onelife = response_onelife - 1
    print "Komi: Such a tragic end for them. Anyway, my name is Komi. I am a spirit existing as far back as the BCs."
print "Komi: As a wizard, you need your base skill set to develop and grow stronger as you improve yourself."
while proper_base_skill_point >=1:
  choose_base_skill = raw_input("Komi: What skill do you choose? (Healing, Strength, Defense, Charisma, CW) ")
  print "\n"
  if choose_base_skill == "healing" or choose_base_skill == "Healing":
    print "Komi: A healer? Interesting, I wish the best of luck to you and your medicine!"
    proper_base_skill_point = proper_base_skill_point - 1
  elif choose_base_skill == "strength" or choose_base_skill == "Strength":
    print "Komi: Strength? You must have guts, good luck on your adventure!"
    proper_base_skill_point = proper_base_skill_point - 1
  elif choose_base_skill == "defense" or choose_base_skill == "Defense":
    print "Komi: Defense? A wise choice, good luck on your adventure!"
    proper_base_skill_point = proper_base_skill_point - 1
  elif choose_base_skill == "charisma" or choose_base_skill == "Charisma":
    print "Komi: Charisma? Aren't you a social one. Okay, good luck to you!"
    proper_base_skill_point = proper_base_skill_point - 1
  elif choose_base_skill == "cw" or choose_base_skill == "CW":
    print "Komi: What?? You're kind of weird..."
    cat_whisperer_confirmation = raw_input("Komi: Are you sure you really want to choose this skill? You don't even know what it is... (yes/no) ")
    if cat_whisperer_confirmation == "yes" or cat_whisperer_confirmation == "Yes" or cat_whisperer_confirmation == "y" or cat_whisperer_confirmation == "Y":
      print "Komi: I'm questioning your choice but if that's what you say, then ok. Good luck, I guess?"
      proper_base_skill_point = proper_base_skill_point - 1
    elif cat_whisperer_confirmation == "no" or cat_whisperer_confirmation == "No" or cat_whisperer_confirmation == "n" or cat_whisperer_confirmation == "N":
      print "Komi: That's what I thought, pick again."
    else:
      print "Komi: What are you saying??? This time, choose properly."
  else:
    print "Komi: Did you type something wrong or are you incapable of choosing?"
print "You: Thank you. Will you help me in finding Azel? I need to avenge my parents..."
print "Komi: That was my intention the entire time. Why else do you think I even approached you in the first place?"
print "You: Okay, sorry, jeez."
print "Komi: That's right."
response_twolife = 1
response_threelife = 1
response_fourlife = 1
while response_twolife >= 1:
  response_two = raw_input("You: (Where is he? / How was your day?) ")
  print "\n"
  if response_two == "Where is he?" or response_two == "where is he?" or response_two == "where is he":
    response_twolife = response_twolife - 1
    print "Komi: A good question. For once you speak something valuable."
    print "Komi: The most recent activity I received from the dark wizard Azel was from the town of Frostford."
  elif response_two == "How was your day?" or response_two == "how was your day?" or response_two == "how was your day" or response_two == "day":
    print "Komi: We don't have time to mess around."
    print "Komi: Do you want to find out what I know of Azel's location or not?"
    while response_threelife >= 1:
      response_three = raw_input("You: (yes/no) ")
      print "\n"
      if response_three == "yes":
        response_threelife = response_threelife - 1
        response_twolife = response_twolife - 1
        print "Komi: Recent activity from him has been reported from the small town of Frostford."
      elif response_three == "no":
        response_threelife = response_threelife - 1
        response_twolife = response_twolife - 1
        print "Komi: Really then? There is no point to me accompanying you on this journey. Good luck on your own. I doubt you can do anything without me."
        if choose_base_skill == "charisma" or choose_base_skill == "Charisma":
          print "--Because your base skill is charisma, you have the option to get back on Komi's good side.--"
          while response_fourlife >= 1:
            response_four = raw_input("You: (apologize/do nothing) ")
            print "\n"
            if response_four == "apologize" or response_four == "Apologize":
              response_fourlife = response_fourlife - 1
              response_twolife = response_twolife - 1
              response_threelife = response_threelife - 1
              print "You: I'm sorry. I didn't mean it. I need your help, please."
              print "Komi: That's what I thought. Now about Frostford..."
            elif response_four == "do nothing" or response_four == "Do nothing" or response_four == "nothing":
              response_fourlife = response_fourlife - 1
              response_twolife = response_twolife - 1
              response_threelife = response_threelife - 1
              print "--Komi disappears from your sight. You can no longer hear her voice. She is gone and without her, your journey has hit a dead end.--"
              print "--Nice work, " + str(player_name) + ". Game over for you.--"
              sys.exit()
        else:
          response_fourlife = response_fourlife - 1
          response_twolife = response_twolife - 1
          response_threelife = response_threelife - 1
          print "--Komi disappears from your sight. You can no longer hear her voice. She is gone and without her, your journey has hit a dead end.--"
          print "--Nice work, " + str(player_name) + ". Game over for you.--"
          sys.exit()
      else:
        print "Komi: Can you hurry up and write an actual response? Jeez, I'm surrounded by airheads..."
  else:
    print "Komi: What? Hurry up and answer me. We don't have the time for your silly mistakes."
print "You: We should go there, then."
print "Komi: Do you even have anything to defend yourself with?"
print "You: In terms of weaponry, not really."
print "Komi: As I expected. You're hopeless."
print "You: Hey, hey, that's not really nice. Where can I get weapons?"
print "Komi: We can get you a wand in one of the shops in the village nearby. Come, now."
print "--You travel to the nearby village. It is bustling with life. Two weapon shops are on either side of the road you walked down.--"
print "--The shop on the right is dark and had a beat up sign on its door. The one on the left seemed as if it was painted and polished recently.--"
response_fivelife = 1
while response_fivelife >= 1:
  response_five = raw_input("--Which shop will you go to?-- (right/left) ")
  print "\n"
  if response_five == "right" or response_five == "Right" or response_five == "r":
    response_fivelife = response_fivelife - 1
    print "--The shop had been open for hundreds of years. The shelves were loaded. You have acquired a WAND, SATCHEL and POISONED DAGGER.--"
  elif response_five == "left" or response_five == "Left" or response_five == "l":
    response_fivelife = response_fivelife - 1
    print "--The shop opened just a day ago. The shelves were almost bare. The workers told you they were still stocking up. You have a acquired a WAND, PLASTIC BAG and CANDY.--"
  else:
    print "--What?--"
print "Komi: Excellent."
print "You: Let's go."
print "Komi: Look, there's a soldier over there. You can ask him if he knows anything about Azel."
print "--You walk up to the soldier and tap his arm."
print "--The soldier points his wand at you.--"
print "Soldier: Who are you? State your purpose before I freeze you."
response_sixlife = 1
while response_sixlife >= 1:
  response_six = raw_input("You: (attack/talk) ")
  print "\n"
  if response_six == "attack" or response_six == "Attack":
    response_sixlife = response_sixlife - 1
    print "--You raise your wand in defense and send electric sparks towards him.--"
    print "Soldier: Why you-"
    if choose_base_skill == "defense" or choose_base_skill == "Defense":
      print "--Because of your defense skill, you are able to dodge the soldier's attacks.--"
      print "Soldier: What are you doing here?"
      print "You: I just need to ask you a question. Where is Azel?"
      print "Soldier: Like I'd tell a child like you."
      print "You: I need to defeat him."
      print "Soldier: You? As if you can. Dark wizard Azel has been spotted in the rundown warehouse at the outskirts of Frostford. Let's see what you got, kid."
      print "Komi: This guy has logic. Unlike you."
      print "You: Thank you sir."
    else:
      print "--The soldier has taken advantage of your inexperience in the wizarding world.--"
      print "--You have been thrown in prison. Komi clicks her tongue in disdain.--"
      print "Komi: To think that head of yours would be more rational. I'm disappointed in you, " + str(player_name) + ". I expected you to take this seriously."
      print "--Komi disappears from your sight and you are left alone on the cold prison ground.--"
      print "--Game over, " + str(player_name) + "."
      sys.exit()
  elif response_six == "talk" or reponse_six == "Talk":
    response_sixlife = response_sixlife - 1
    print "You: Wait! I only have a question to ask. I mean no harm. My name is " + str(player_name) + "."
    print "Soldier: What's your question, kid?"
    print "You: What do you know of Azel?"
    print "Soldier: You speak his name so casually like that? Whispers have been going around town that he resides in a warehouse on the outskirts of Frostford."
    print "You: Thank you, that's all I needed."
print "Soldier: Yeah, yeah, now get lost."
print "\n"
print "--You walk through the village with Komi and reach a fork in the road.--"
print "--The road on the left is dark and bumpy. Trees cover the road and you can't see farther than the entrance.--"
print "--The road in the middle is an abandoned railroad track that goes on for a few more meters.--"
print "--The road on the right is bright and has a bit of pavement. It seems people take this path the most.--"
response_sevenlife = 1
while response_sevenlife >= 1:
  response_seven = raw_input("--Which road do you choose?-- (left, middle, right) ")
  print "\n"
  if response_seven == "left" or response_seven == "Left" or response_seven == "l":
    print "--You encounter a swarm of spiders in the forest. This isn't the right path. You are now traumatized.--"
  elif response_seven == "middle" or response_seven == "Middle" or response_seven =="m":
    response_sevenlife = response_sevenlife - 1
    print "--The farther you follow the rails, the more civilized the landscape looks. This is the right path. You have entered the outskirts of Frostford.--"
  elif response_seven == "right" or response_seven == "Right" or response_seven == "r":
    print "--You walk through the sun. The path leads to a bustling city. This is not Frostford. You are on the wrong path.--"
  else:
    print "--Did you type something wrong?--"
print "\n"
print "You: Komi, look. That's Frostford, right?"
print "Komi: Yes, you airhead. Can you not see the sign?"
print "You: I, in fact, did not see that. Anyway, the soldier said Azel was in a warehouse..."
print "Komi: Look, there's a little girl working over there."
print "--You walk over to the girl. She stops gardening and looks up at you curiously.--"
print "You: Excuse me, I'm looking for a warehouse near here. Do you happen to know where that is?"
print "Girl: Warehouse? You mean the abandoned tool company? It's right over there, past those trees."
print "You: Thank you very much."
print "\n"
print "--You travel to the abandoned warehouse and stop outside the door. You hesitate.--"
print "You: Komi, I have a wand, but I don't know any spells or hexes and such. What do I do?"
print "Komi: Here are three you should know:"
print "Komi: There is the levitation spell, which immediately lifts you up in the air."
print "Komi: Then there is the attack spell, which shoots firey sparks out of your wand."
print "Komi: Lastly, there is the ice spell. You can interpret it in any way you want."
print "You: That's useful. Thanks. I'm ready to face him now."
print "\n"
print "--You slowly open the creaky doors of the warehouse. On the other side of the building, you see the shadow of a figure.--"
print "You: Azel! Is that you?"
print "?: Stupid child."
print "You: Ok. That's just an insult, man."
print "?: You know nothing of this world. You're just an insolent child."
print "Komi: This is Azel. Quick, take cover!"
print "\n"
print "--You quickly duck behind a few crates. Azel fired a spell where you previously stood.--"
print "You: Azel, I'm going to avenge my parents for what you've done to them!"
print "--The figure chuckles, stepping out of the shadows.--"
print "\n"
print "Azel: So foolish. You don't know half of the truth. It wasn't some wizard targeting you, it was your father. Or rather...me."
print "You: What..."
print "Azel: I eliminated your mother immediately. It was your turn, but they took you away before I could get rid of you permanently. Be grateful, child."
print "You: How could you..."
response_eightlife = 1
while response_eightlife >= 1:
  response_eight = raw_input("--Attack Azel with a spell!-- (levitation/fire/ice) ")
  print "\n"
  if response_eight == "levitation" or response_eight == "Levitation":
    response_eightlife = response_eightlife - 1
    print "--You start levitating a few feet above the ground. You did no damage to Azel.--"
    print "Azel: This is a joke, right? For a child of mine, you are clueless. No worries, this makes killing you easier."
    print "--Azel shoots an offensive spell at you while you are vulnerable in the air.--"
    if choose_base_skill == "defense" or choose_base_skill == "Defense":
      print "--Because of your defense skill, you have the ability to defend yourself.--"
      response_ninelife = 1
      while response_ninelife >= 1:
        response_nine = raw_input("--Defend?-- (yes/no) ")
        if response_nine == "yes" or response_nine == "Yes":
          response_ninelife = response_ninelife - 1
          print "\n"
          print "--You use your ice spell to create a wall, defending yourself from Azel's attack. You slowly lower yourself to the ground.--"
          print "Azel: Tch. Lucked out."
        elif response_nine == "no" or response_nine == "No":
          response_ninelife = response_ninelife - 1
          print "--This is the end for you. The attack hits you straight through the heart.--"
          print "--Your life was not in vain, " + str(player_name) + ". Game over for you."
          sys.exit()
        else:
          print "--Did you make a mistake, " + str(player_name) + "?"
    else:
      print "--This is the end for you. The attack hits you straight through the heart.--"
      print "--Your life was not in vain, " + str(player_name) + ". Game over for you."
      sys.exit()
  elif response_eight == "fire" or response_eight == "Fire":
    response_eightlife = response_eightlife - 1
    print "--You fire your spell at him, hitting him in the arm.--"
    #strength ending
    if choose_base_skill == "strength" or choose_base_skill == "Strength":
      print "--Your strength is impeccable. Azel's arm is now incapable. He can no longer use it. He screams in pain.--"
      print "Azel: You'll regret ever coming here!"
      print "--Azel tries running away, but you attack him with the fire spell again.--"
      print "--In a fit of agony, Azel withers to the ground and collapses.--"
      print "\n"
      print "You: I did it...I did it, Komi!"
      print "Komi: It was a pleasure working with you, " + str(player_name) + ". Or at least it was a pleasure half of the time."
      print "You: I'll ignore the last part."
      print "\n"
      print "--Congratulations, " + str(player_name) + ". You have beat the game through the 'Strength' skill.--"
      print "--Thank you for playing!--"
      sys.exit()
    else:
      print "Azel: Agh!"
      print "Azel: You'll pay for that."
  elif response_eight == "ice" or response_eight == "Ice":
    response_eightlife = response_eightlife - 1
    print "--You shoot shards of ice at him, freezing his body.--"
    if choose_base_skill == "strength" or choose_base_skill == "Strength":
      print "--Your strength is impeccable. Azel is incapable of moving.--"
      print "Azel: You will pay for this one day. You are no child of mine!"
      print "--You attack him with the ice spell again, hitting him directly in the heart.--"
      print "--Azel collapses on the ground.--"
      print "\n"
      print "You: I did it...I did it, Komi!"
      print "Komi: It was a pleasure working with you, " + str(player_name) + ". Or at least it was a pleasure half of the time."
      print "You: I'll ignore the last part."
      print "\n"
      print "--Congratulations, " + str(player_name) + ". You have beat the game through the 'Strength' skill.--"
      print "--Thank you for playing!--"
      sys.exit()
    else:
      print "Azel: You'll pay for that!"
      print "--He uses a fire spell to melt the ice surrounding him.--"
  else:
    print "Komi: Take this seriously, kid!"
print "\n"
print "--Azel catches you off guard and shoots you with an electricity spell, shocking you. You are now injured.--"
#healing ending
if choose_base_skill == "healing" or choose_base_skill == "Healing":
  print "--You heal yourself back to full health.--"
  response_tenlife = 1
  while response_tenlife >= 1:
    response_ten = raw_input("(attack/flee) ")
    if response_ten == "flee" or response_ten == "Flee":
      response_tenlife = response_tenlife - 1
      print "You: Komi...I need to run. I can't do this."
      print "Komi: As you wish."
      print "Azel: Coward! You are no child of mine!"
      print "--Game over for you, " + str(player_name) + ". You went so far to drop out like this?"
    elif response_ten == "attack" or response_ten == "Attack":
      response_tenlife = response_tenlife - 1
      print "\n"
      print "--You fire another ice spell at him, shooting an icicle straight at his heart. Azel shrivels up and collapses on the ground.--"
      print "\n"
      print "Komi: He died with a cold heart. How ironic."
      print "You: I did it...I did it, Komi!"
      print "Komi: It was a pleasure working with you, " + str(player_name) + ". Or at least it was a pleasure half of the time."
      print "You: I'll ignore the last part."
      print "\n"
      print "--Congratulations, " + str(player_name) + ". You have beat the game through the 'Healing' skill.--"
      print "--Thank you for playing!--"
    else:
      print "Komi: Take this seriously, kid!"
#defense ending
elif choose_base_skill == "defense" or choose_base_skill == "Defense":
  print "--You use the ice spell to create a wall, shielding yourself.--"
  response_tenlife = 1
  while response_tenlife >= 1:
    response_ten = raw_input("(attack/flee) ")
    if response_ten == "flee" or response_ten == "Flee":
      response_tenlife = response_tenlife - 1
      print "You: Komi...I need to run. I can't do this."
      print "Komi: As you wish."
      print "Azel: Coward! You are no child of mine!"
      print "--Game over for you, " + str(player_name) + ". You went so far to drop out like this?"
    elif response_ten == "attack" or response_ten == "Attack":
      response_tenlife = response_tenlife - 1
      print "\n"
      print "--You fire another ice spell at him, shooting an icicle straight at his heart. Azel shrivels up and collapses on the ground.--"
      print "\n"
      print "Komi: He died with a cold heart. How ironic."
      print "You: I did it...I did it, Komi!"
      print "Komi: It was a pleasure working with you, " + str(player_name) + ". Or at least it was a pleasure half of the time."
      print "You: I'll ignore the last part."
      print "\n"
      print "--Congratulations, " + str(player_name) + ". You have beat the game through the 'Defense' skill.--"
      print "--Thank you for playing!--"
    else:
      print "Komi: Take this seriously, kid!"
#charisma ending
elif choose_base_skill == "charisma" or choose_base_skill == "Charisma":
  print "--Father...--"
  response_tenlife = 1
  while response_tenlife >= 1:
    response_ten = raw_input("(attack/flee) ")
    if response_ten == "flee" or response_ten == "Flee":
      response_tenlife = response_tenlife - 1
      print "You: Komi...I need to run. I can't do this."
      print "Komi: As you wish."
      print "Azel: Coward! You are no child of mine!"
      print "--Game over for you, " + str(player_name) + ". You went so far to drop out like this?"
    elif response_ten == "talk" or response_ten == "Talk":
      response_tenlife = response_tenlife - 1
      print "\n"
      print "You: It didn't have to end like this. Why? Why did you kill mom?"
      print "Azel: That's for me to know, child. Stick your nose in someone else's business."
      print "You: This IS my business! We could have been a happy family, you, mom, and I. We still can be, just turn around. You always have a chance."
      print "You: What are you even doing this for? Let's live a happy life together, dad."
      print "--Azel stares at you for a moment.--"
      print "\n"
      print "Azel: I think...I think you're right. Why am I doing this? I'm not even happy with the way I am. Let's go home, " + str(player_name) + "."
      print "--Azel heals you.--"
      print "You: I did it...I did it, Komi!"
      print "Komi: It was a pleasure working with you, " + str(player_name) + ". Or at least it was a pleasure half of the time."
      print "You: I'll ignore the last part."
      print "\n"
      print "--Congratulations, " + str(player_name) + ". You have beat the game through the 'Charisma' skill.--"
      print "--Thank you for playing!--"
    else:
      print "Komi: Take this seriously, kid!"
#CW ending
elif choose_base_skill == "cw" or choose_base_skill == "CW":
  print "You: Ouch...my wand is gone, Komi..."
  response_tenlife = 1
  while response_tenlife >= 1:
    response_ten = raw_input("(attack/flee) ")
    if response_ten == "flee" or response_ten == "Flee":
      response_tenlife = response_tenlife - 1
      print "You: Komi...I need to run. I can't do this."
      print "Komi: As you wish."
      print "Azel: Coward! You are no child of mine!"
      print "--Game over for you, " + str(player_name) + ". You went so far to drop out like this?"
    elif response_ten == "attack" or response_ten == "Attack":
      response_tenlife = response_tenlife - 1
      print "\n"
      print "Komi: Quick, over there on the floor! There's your wand!"
      print "--You struggle to crawl over to your wand. Before you reach it, Azel steps in front of you and breaks the wand in half.--"
      print "Azel: Not today."
      print "You: There's nothing I can do...this is the end, Komi."
      print "Komi: Your skill...earlier you chose your skill as CW, whatever that means. Try channeling it now! Anything helps at this point."
      print "--You hesitantly build up power in your core. A few seconds later, nothing happens.--"
      print "You: It's useless-"
      print "\n"
      print "--A cat's meow stops you mid-sentence. You look back towards the entrance of the warehouse to see an army of felines.--"
      print "--The cat in the front aggressively meows at Azel and bows their head towards you. Before you know it, the swarm of cats attacked Azel, leaving him unconscious on the ground.--"
      print "You: What.."
      print "Komi: CW...you're a cat whisperer!"
      print "--You quickly thanked the cats. As they exit the building, you turned to Komi.--"
      print "You: I did it...I did it, Komi!"
      print "Komi: It was a pleasure working with you, " + str(player_name) + ". Or at least it was a pleasure half of the time."
      print "You: I'll ignore the last part."
      print "\n"
      print "--Congratulations, " + str(player_name) + ". You have beat the game through the 'Cat Whisperer' skill.--"
      print "--Thank you for playing!--"
    else:
      print "Komi: Take this seriously, kid!"