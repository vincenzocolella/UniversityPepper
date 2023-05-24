import sys
from modim_interaction import *
from pddl2txt import *
from scripts_ import *


destinations = {"banca": "pos7_12","fisiologia umana" :"pos12_7","fisiologia generale" :"pos12_11","botanica":"pos9_18","genetica":"pos10_19","medicina legale":"pos5_22","obitorio":"pos5_22","scienze statistiche":"pos13_5","scienze solitiche":"pos15_9","ciao":"pos13_15","lettere e filosofia":"pos16_20","scienze umanistiche":"pos16_20","laboratori chimica":"pos13_24","fisica":"pos23_14",
                "chimica":"pos23_16","chimica farmaceutica":"pos21_22","geologia":"pos18_10","giurisprudenza":"pos17_12",
         "matematica":"pos19_22","igiene":"pos27_14","zoologia":"pos21_6","neurologia":"pos24_6","scienze dello spettacolo":"pos27_8","ortopedia":"pos27_15"}

vocab = ['banca', 'fisiologia', 'botanica', 'genetica', 'medicina', 'obitorio', 'scienze statistiche', 'scienze politiche', 'ciao',
         'lettere e filosofia', 'scienze umanistiche', 'laboratori chimica', 'fisica', 'chimica', 'chimica farmaceutica', 'geologia',
         'giurisprudenza', 'matematica', 'igiene', 'zoologia', 'neurologia', 'scienze dello spettacolo', 'ortopedia']

speech = Speech()
gesture = Gestures()
def main_run():
    
    interaction = start_interaction(speech)
    
    if (interaction):
        speech.say("Do you need indications or do you want to play?")
        rightanswer=False
        while(not rightanswer):
            answer = speech.listen()
            
            if answer == "Indications":
                rightanswer = True
                
                speech.say("Perfect! Where do you have to go?")
                goal = speech.listen(vocabulary=vocab)
                
                if (goal not in vocab):
                    find = False
                
                    while(not find):
                        speech.say("Sorry I didn't understand, can you repeat please?")
                        goal = speech.listen(vocabulary=vocab)
                
                        if (str(goal) in vocab):
                            find=True

                speech.say("Ok, now using the tablet press on the cells in which are obstacles, if None press the Ok button")
                
                #take the cell position
                
                for pos in destinations:
                    if (pos == goal):
                        goal = destinations[pos]
                        
                #modify the javascript of the grid
                with open("../grid.js","r") as f:
                    js_file = f.readlines()
                    f.close()
                    gg = goal.strip("pos\n").split("_")
                    
                    js_file[0] = "var goalx = "+gg[0]+";\n"
                    js_file[1] = "var goaly = "+gg[1]+";\n"
                with open("../grid.js","w") as f:
                    for js_line in js_file:
                        f.write(js_line)
                    f.close()
                    
                #APRI INTERAZIONE CON MAPPA SUL TABLET
                TabletInteraction("i1")
                
                speech.say("please wait, i'm computing the best path for you")
                
                with open("../utils/obs.out","r") as f:
                    obs = f.readline()
                    f.close()
                    obs = obs.strip("\n")

                img_p = create_problem(obs,goal)
                
                with open("../actions/quit","r") as f:
                    lines = f.readlines()
                    f.close()
                    lines[1] = "<*,*,*,*>: img/"+img_p+"\n"
                
                with open("../actions/quit","w") as f:
                    for line in lines:
                        f.write(line)
                    f.close()
                
                speech.say("I'm ready! Look at my tablet to see your path")
                
                TabletInteraction("i3")
                
                speech.say("I hope it helped, see you next time bye!")
                gesture.sayhi()
                
            elif answer=="Play":
                rightanswer = True
                speech.say("Perfect! Let's play a memory game on the tablet")
                #APRI INTERAZIONE CON GIOCO SU TABLET
                
                TabletInteraction("i2")
                
                speech.say("I hope you had fun, see you next time bye!")
                gesture.sayhi()
            else:
                speech.say("Sorry, I didn't understand")
    return
    
if __name__ == "__main__":

    while True:
        try:
            sonar = Sonar()
            check = sonar.listen(detected=False)
            if check == 'front':
                main_run()
        except KeyboardInterrupt:
            print("Interrupted")
            Reset()
            sys.exit(0)
