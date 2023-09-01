import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")
text = "Hellow, Sharad How are you?"
gd = "Have a good day Sharad"

ram = "Jai Shree Ram............. Jai Jai Shree Ram............. Jai Jai Jai Shree Ram..."

# play = '''Shri ram janki baithe hai mere seene mein,
#
# dekh lo mere dil ke nagine mein,
#
# shri ram janki baithe hai mere seene mein …..'''

# speak.Speak(text)
# speak.Speak(gd)
speak.Speak(ram)
# speak.Speak(play)