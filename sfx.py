import simpleaudio as sa
print("freakysfx")
def app():
    print("""options
          --------------
          - freakybob is calling
          - knock
          - party""")
    sfx = input("sfx? ")
    if (sfx == "freakybob is calling" or sfx == "Freakybob is calling"):
        print("sound from https://tuna.voicemod.net/sound/5149f3d4-c176-489d-a747-67f8fabfd21d")
        wave_obj = sa.WaveObject.from_wave_file("calling.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()
        print("done playing")
        app()
    if (sfx == "knock" or sfx == "Knock"):
        print("sound from https://www.101soundboards.com/sounds/31065914-knock-knock")
        wave_obj = sa.WaveObject.from_wave_file("knock.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()
        print("done playing")
        app()
    if (sfx == "party" or sfx == "Party"):
        print("sound from https://www.101soundboards.com/sounds/30318385-hey-man-its-me-are-you-still-coming-to-my-party")
        wave_obj = sa.WaveObject.from_wave_file("party.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()
        print("done playing")
        app()
app()