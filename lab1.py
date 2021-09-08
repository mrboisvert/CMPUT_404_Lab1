import requests as r
raw_script = r.get("https://raw.githubusercontent.com/mrboisvert/CMPUT_404_Lab1/main/lab1.py")
print(raw_script.content)