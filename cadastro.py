from usuarios import listaUsuarios
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import speech_recognition as sr
import pyttsx3
import os
engine = pyttsx3.init()
engine = pyttsx3.init()
engine.setProperty("voice", "brazil")
engine.setProperty("rate", 200)
engine.setProperty("volume", 1.)



def inicio():
    engine.say("Olá, sou sua assistente virtual. Você já possui cadastro?")
    engine.runAndWait()
    if 'não' in entrar_audio():
        personalizar()

    else:
        engine.say('Me informe seu nome')
        engine.runAndWait()
        nome = entrar_audio().lower()
        engine.say('Autenticando')
        engine.runAndWait

        if login(nome):
            engine.say('Autenticado')
            engine.runAndWait()
            print(nome)
 
        else:
            while True:
                engine.say('Erro de usuário, fale seu nome novamente')
                engine.runAndWait()
                #Caso o nome informado pela pessoa nao esteja na lista de users, ele vai entrar nesse 
                # else e automaticamente no while, e enquanto o nome informado nao estiver na lista, ele vai informar queo usario eta incorreto e perguntar novamente
                nome = entrar_audio()
                
                if login(nome):
                    break
                else: 
                    pass
          
            print(nome) 


def login(nome):
    for j in listaUsuarios:
        if j['nome'] == nome: 
            return True

        else:
            return False


def personalizar():
    # colocar aqui para personalizar voz, lingua e nome só
    print("Olá, para a minha personalização, por favor, responda algumas perguntas abaixo:")

    engine.say('Como voce quer que eu me chame')
    engine.runAndWait()
    nomeAssistente = entrar_audio()

    engine.say('Qual seu nome?')
    engine.runAndWait()
    nome = entrar_audio().lower()

    engine.say("vôce deseja acionar o desligamento do computador automático?")
    engine.runAndWait()
    desligar = entrar_audio()

    print("tudo pronto!")
    engine.say(f'Olá {nome} sou {nomeAssistente} , sua Assistente virtual')
    engine.runAndWait()

    info = {'nome': nome, 'nomeAssistente': nomeAssistente, 'desligar': desligar}
    listaUsuarios.append(info)
    with open("usuarios.py", 'w') as arc:
        arc.write(f'listaUsuarios = {listaUsuarios}')


def entrar_audio():
    frase = ''
    while frase == '':
        microfone = sr.Recognizer()
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)
            audio = microfone.listen(source)
        try:
            frase = microfone.recognize_google(audio, language='pt-BR')

        except sr.UnknownValueError:
            engine.say('')
            engine.runAndWait()
        return frase


def pesquisar():
    engine.say("o que voê deseja que eu pesquise?")
    engine.runAndWait()


inicio()
