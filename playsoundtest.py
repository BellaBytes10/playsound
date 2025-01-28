from playsound import playsound
def autoclose(secs, delay, delay2):
    import time
    time.sleep(delay2)
    while secs>0:
        print("Automatically closing in",secs)
        time.sleep(1)
        secs-=1
    exit()
def help():
    import os
    os.getcwd()
def play():
    print("Provide file path...")
    song=input("")
    playsound(song)
play()
autoclose(10, 2, 0)
