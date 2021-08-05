import pyautogui, time
kata = "bot spam by roby"
for i in range(9999):
	pyautogui.typewrite(kata)
	time.sleep(1)
	pyautogui.press("enter")

	