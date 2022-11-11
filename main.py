import cadastro
import os
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time


def desligar():
  cadastro.engine.say(" Voce tem certeza de que deseja desligar o computador?")
  cadastro.engine.runAndWait()
  desligar = cadastro.entrar_audio()
  if desligar == "sim":
    os.system("shutdown /s /t 1")
  else:
    main()


def horas():
  cadastro.engine.say("Agora sao")
  cadastro.engine.runAndWait()
  cadastro.engine.say(datetime.now().strftime('%H:%M:%S'))
  cadastro.engine.runAndWait()


def data():
  cadastro.engine.say("Hoje é")
  cadastro.engine.runAndWait()
  cadastro.engine.say(datetime.now().strftime('%d-%m-%Y'))
  cadastro.engine.runAndWait()

  
def spotify():
  nav = webdriver.Chrome()
  pyautogui.hotkey('win')
  time.sleep(2)
  pyautogui.write('Spotify')
  time.sleep(1)
  pyautogui.hotkey('enter')
  time.sleep(10)


def pesquisa():
  cadastro.engine.say("o que voce quer que eu pesquise?")
  cadastro.engine.runAndWait()
  pesquisa = cadastro.entrar_audio()

 
def mensagemWpp():
  wichPerson = input('qual pessoa voce deseja mandar mensagem?')
  txt = input('qual mensagem voce quer enviar?')
  if wichPerson == '':
      pass
  else:
      nav = webdriver.Chrome()
      pyautogui.hotkey('win')
      time.sleep(2)
      pyautogui.write('google')
      time.sleep(1)
      pyautogui.hotkey('enter')
      time.sleep(3)
      pyautogui.hotkey('tab')
      pyautogui.hotkey('tab')
      pyautogui.hotkey('tab')
      pyautogui.hotkey('tab')
      pyautogui.hotkey('enter')
      pyautogui.hotkey('ctrl', 't')
      pyautogui.write('https://web.whatsapp.com/')
      time.sleep(2)
      pyautogui.hotkey('enter')
      time.sleep(11)
      pyautogui.hotkey('tab')
      pyautogui.hotkey('tab')
      pyautogui.hotkey('tab')
      pyautogui.hotkey('tab')
      pyautogui.write(f'{wichPerson}')
      time.sleep(2)
      pyautogui.hotkey('enter')
      pyautogui.hotkey('enter')
      pyautogui.write(f'{txt}')
      pyautogui.hotkey('enter')


      
def main():
  cadastro.engine.say("o que você deseja?")
  cadastro.engine.runAndWait()

  if "horas" or "horário" in cadastro.entrar_audio():
    horas()
  #if cadastro.entrar_audio() == horas

  if "dia" or "data" in cadastro.data():
    data()

  if "desligar" or "fechar" in cadastro.data():
    desligar()

  if "enviar mensagnes" or "whatsapp" or "envio" in cadastro.mesagemWpp():
    mensagemWpp()

  
main()
