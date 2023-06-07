#pip install pyautogui
#pip install time
#não é necessario instalar a biblioteca pyperclip, pois ela se instala junto com a pyautogui

import pyautogui
import time
import pyperclip

#esse processo segue o passo a passo para entrar no whatsapp e enviar meensagem automaticamente
#para qualquer usuario.

pyautogui.hotkey("ctrl","t")
time.sleep(3)
pyautogui.click(x=561, y=427)
pyautogui.write("whatsapp")
pyautogui.press("enter")
time.sleep(3)
pyautogui.doubleClick(x=283, y=399)
pyautogui.press("enter")
time.sleep(7)
pyautogui.click(x=244, y=155)
pyautogui.write(" Destinatario")
time.sleep(5)
pyautogui.click(x=124, y=261)
time.sleep(3)

#pega a mensagem previamente escolhida
texto= """Mensagem que deseja enviar"""

#envia a mensagem
pyperclip.copy(texto)
pyautogui.hotkey("ctrl","v")
time.sleep(2)
pyautogui.press("enter")



#comando para pegar a posição do mouse no monitor
#time.sleep(5)
#print(pyautogui.position()) 