import win32com.client
# names=["affan","ibrahim","ali","mustafa","faiz","abubakar"]
name="mubbu"
speaker=win32com.client.Dispatch("SAPI.SpVoice")
# for name in names:
speaker.speak(f"gali gali me shor hai {name}  haram khor hai")
