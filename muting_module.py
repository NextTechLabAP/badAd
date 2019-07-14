import pyautogui
function mute(int var_state):
	pyautogui.moveTo(1703,1046)
	pyautogui.click(1703,1046)
	pyautogui.moveTo(1510,987)
	pyautogui.click(1510,987)
	var_state = 1
function unmute(int var_state):
	pyautogui.moveTo(1703,1046)
	pyautogui.click(1703,1046)
	pyautogui.moveTo(1510,987)
	pyautogui.click(1510,987)
	var_state = 0			