print ("ESCAPE THE PRISON")
print ("A 80's styled text game")
print ("If the game stops printing. You probably created a syntax error. Other possibilities is just us being dumb.")
score = 0
print ("type start to begin!")
sta_rt = input()
answer = (sta_rt)
if answer == ("start") :
  print ("You start your journey as a man. That's all. Now escape this prison to get to your wife; Mrs McGuffin.")
  print ("But first. What is your name?")
  name = input()
  print ("Disclaimer this is not how prisons work".upper())
  print ("Warden: Hello",name,"Welcome to Badnews Prison")
  print ("Warden: I have left you mash potatoes in your lunch tray")
  print ("Voice in the sky: You have three choices")
  print ("'search the tray', 'eat the potatoes' or 'snort the potatoes'")
  print ("fact: CAPS ARE DEADLY!!!")
  answer_1 = input()
  answer = (answer_1)
  if answer == ("search the tray") :
    score = score + 1
    print ("The warden walks away and your eyes follow him. You quickly dig through the potatoes but find nothing. Except potatoes of course.")
    print ("Voice in the sky: Another 3 options... 'continue searching' through the potatoes. 'give up'. Or 'search the wall'")
    answer_1_1 = input()
    answer = (answer_1_1)
    if answer == ("continue searching") :
      print ("you dug through the potatoes so hard that the potatoes melted through the tray and slumped onto the ground. It began melting through the ground creating a tunnel as it had a mind of its own.")
      print ("Voice in the sky: \"jump into the tunnel\", \"continue watching it\" or type \"climb into it.\"")
      answer_1_1_1 = input()
      answer = (answer_1_1_1)
      if answer == ("jump into the tunnel") :        
        score = score + 1   
        print ("You decided to leap straight into the tunnel like a maniac. It was deeper than you thought and you broke both your legs")
      if answer == ("continue watching it") : 
        score = score + 0
        print ("you just watched the potatoes sink into the ground like a numpty.")
        print ("somehow watching the potatoes burn your retina's and you die. Tip: Don't trust food")
        print ("your final score is",score)

      if answer == ("climb into it"):
        score = score + 2   
        print ("You realised there was a super long ladder right next to you, you grabbed it and put it down the tunnel and climbed down safely.")
        print ("W.I.P")
  if answer == ("eat the potatoes") :
    print ("The warden walks away and your eyes follow him. You eat the potatoes and you fall dangerously ill and died. Tip: don't trust food.")
    print ("your final score is",score)
  if answer == ("snort the potatoes"):
    score = score + 2
    print ("The warden walks away and your eyes follow him. You decide to snort the potatoes and after that you feel high. Magically a key drops from the sky and you unlock the bars. Turns out you were high and you unlocked the door with your finger")
    print ("You leave your cell and you start seeing magical creatures. After a while they dissapear and you realize that your hands are bleeding profusely because you managed to unlock your cell with your fingers. ")
    print ("you have three choices. 'Try and stop the bleeding', 'Deal with it' or 'Pressurize the wound'")
    answer_1_2 = input ()
    answer = (answer_1_2)
    if answer == ("try and stop the bleeding"):
      print ("You stop the bleeding using your shirt which infected your wound")
      score = score + 1

    if answer == ("deal with it") :
      print ("You keep on running, spilling blood everywhere. Ten seconds later you faint and bleed to death. Tip:It's okay to be a wuss.")
      print ("your final score is",score)
      print ("Press run to restart")
    if answer == ("pressurize the wound"):
      print ("You keep your hand on the wound and run towards the door at the end of the cell block.")
      score = score + 2
      print ("Three choices now present themselves. A gaurd comes strolling down the cellblock and you can either. \"take him out\",\"hide\" or simply just \"run at him\"")
      answer_1_2_1 = input()
      answer = (answer_1_2_1)
      if answer == ("take him out") :
        print ("you decide to do a SUPA JUDO KICK. Which turns out badly for you because you kicked with immense speeds that your leg decides to snap off. Tip:Never SUPA JUDO kick anything")
        print ("your final score is",score)
      if answer == ("hide"):
        score = score + 2
        print ("You find an upcoming box to hide in but it seems that a creepy old man with a head band is already inside the box")
        print ("You can either. \"go on an adventure to stop super weapon metal gear\", \"kill the man\" or find another box")
      if answer == ("run at him") :
        score = score + 1
        print ("You run at the man with such speeds that he cowars and you run straight through the door")
  if answer == ("die") :
    print ("You drop dead right in front of the warden.")
    print ("your final score is",score)
  if answer == ("upupdowndownleftrightleftrightabstart"):
    score = score + 99999999999999999999999999999
    print ("You run past the warden and stab him in the chest")
    print ("You break through the prison walls and escape")
    print ("YOU WIN!!!!")
    print ("Your score is",score)

else:
  print ("Welp. Guess your not playing")
  print ("your final score is",score)
  
