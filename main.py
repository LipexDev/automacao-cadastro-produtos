import pyautogui
import time


pyautogui.PAUSE = 0.5


#Passo 1 : Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
#abrir o chrome
pyautogui.press("win")
pyautogui.write("google")
pyautogui.press("enter")

#digitar o site
#esperar 3 segundos
time.sleep(3)
pyautogui.click(x=440, y=62)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#esperar 3 segundos
time.sleep(3)

#Passo 2: Fazer Login
pyautogui.click(x=867, y=405)
pyautogui.write("fih1992@gmail.com")

#preencher a senha
pyautogui.press("tab")
pyautogui.write("minhasenhasupersecreta")

#botao logar
pyautogui.press("tab")
pyautogui.press("enter")

#espera 3 segundos
time.sleep(3)



#Passo 3 : Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

#Passo 4 : Cadastrar um produto
for linha in tabela.index: # repetir a linha de codigo para cada linha da tabela
    pyautogui.click(x=954, y=297)

    codigo = tabela.loc[linha,"codigo" ]
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]




    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)


#Passo 5 : Repetir para todos os produtos
