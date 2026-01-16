# Passo a passo do programa

from turtle import pd
import pyautogui
import time
# pyautogui.click -> clica
# pyautogui.write -> escreve um texto
# pyautogui.press -> aperta uma tecla
# pyautogui.hotkey -> aperta um atalho (hotkey)

pyautogui.PAUSE = 0.5
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
# Passo 1: entrar no sistema da empresa
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

pyautogui.write(link)
pyautogui.press('enter')

#fazer uma pausa pro site carregar
time.sleep(3)

# Passo 2: fazer login
pyautogui.click(x=668, y=455)
pyautogui.write('otavioaugustomarques14@gmail.com')
pyautogui.press('tab') #passar para o proximo campo
pyautogui.write('123456')
pyautogui.press('tab')
pyautogui.press('enter')
#fazer uma pausa pro site carregar
time.sleep(3)

# Passo 3: Abrir base de dados
import pandas
tabela = pandas.read_csv('produtos.csv')

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=653, y=294)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    
# Passo 5: Repetir passo 4 ate acabar a lista de produtos
