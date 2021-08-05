import pyautogui, time
word = "your text to spam"
for i in range(9999):
	pyautogui.typewrite(word)
	time.sleep(1)
	pyautogui.press("enter")

	
