import cadastro
import os
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime


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


def principal():
  if 'desligar' in cadastro.entrar_audio():
    desligar()


def spotify():
  pass


def pesquisa():
  cadastro.engine.say("o que voce quer que eu pesquise?")
  cadastro.engine.runAndWait()
  pesquisa = cadastro.entrar_audio()


def main():
  cadastro.engine.say("o que você deseja?")
  cadastro.engine.runAndWait()

  if "horas" or "horário" in cadastro.entrar_audio():
    horas()
  #if cadastro.entrar_audio() == horas

  elif "dia" or "data" or "mes" or "ano" in cadastro.entrar_audio():
    data()

  elif "desligar" or "desliga" or "desligue" in cadastro.entrar_audio():
    desligar()
  

main()