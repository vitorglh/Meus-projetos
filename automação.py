# biblioteca = pacote de dados 
# pip install pyautogui
# passo a passo do seu programa

import pyautogui
import time

# pyautogui.click > clica 
# pyautogui.write > escreve texto
# pyautogui.press > pressiona tecla
# pyautogui.hotkey > comando
pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# passo 1 entrar sistema empresa
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")
# pausa maior pro site carregar
time.sleep(3)

# passo 2 fazer login 
# clicar campo de email
pyautogui.click(x=808, y=373)
pyautogui.write("vitormito173@gmail.com")
pyautogui.press("tab") #passar proximo campo
pyautogui.write("12345")
pyautogui.press("enter")
# pausa maior pro site carregar
time.sleep(4)

# passo 3 abrir base de dados (importar arquivo)
# pip install pandas openpyxl

import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)


for linha in tabela.index:
# passo 4 cadastrar 1 produto
    pyautogui.click(x=836, y=261)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo) 
    pyautogui.press("tab") #passar próx

    # marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    #tipo produto
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    #preço
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    #obs
    obs = str(tabela.loc[linha, "obs"])
    if obs !="nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

    #voltar inicio da tela
    pyautogui.scroll(20000) # Caso sua res vá descendo a tela com o tab, bota no talo por garantia

# passo 5 repetir o passo 4 até terminar