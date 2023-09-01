import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

ram = "Jai Shree Ram............. Jai Jai Shree Ram............. Jai Jai Jai Shree Ram..."

speak.Speak(ram)
