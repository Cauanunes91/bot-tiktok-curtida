# passos manuais em sequencias, dps tornar cada passo  em um código python
# quais são os passos manuais
# navegar até o site do tiktok https://www.tiktok.com/pt-BR
# LEMBRANDO QUE PARA FUNCIONAR É NECESSÁRIO ALINHAR IGUALMENTE AS DUAS PÁGINAS
# NA TELA UMA DO LADO DA OUTRA
import webbrowser,pyautogui
from time import sleep
webbrowser.open('https://www.tiktok.com/pt-BR')
sleep(10)
# Clicar em login 
pyautogui.click(1781,103,duration=2)
sleep(2)
#  Clicar em logar com email
pyautogui.click(1350,425,duration=2)
sleep(2)
#clicar em logar com email e senha
pyautogui.click(1522,356,duration=2)
sleep(1)
#digitar email/username e senha
pyautogui.click(1346,390,duration=2)
pyautogui.write('INSIRA SEU E-MAIL')
sleep(1)
pyautogui.click(1388,436,duration=2)
pyautogui.write('INSIRA SUA SENHA')
sleep(1)
# clicar em login
pyautogui.click(1415,538,duration=2)
sleep(3)
#navegar até a pagina https://www.tiktok.com/@ronaldinho
webbrowser.open('https://www.tiktok.com/@ronaldinho')
sleep(3)
# clicar na postagem mais recente
pyautogui.click(1157,584,duration=2)
sleep(2)
# verificar se o video ja foi curtido
for video in range (15):
    imagem = pyautogui.locateOnScreen('curtida.png')
    if imagem:
        pyautogui.press('down')
        sleep(2)
        #pule para o proximo o video
    else:
        sleep(2)
        pyautogui.click(1618,396,duration=2)
        sleep(2)
        pyautogui.press('down')
        #codigo para curtir o video 

#se foi curtido passar para o próximo video
# se n foi curtido, curtir este video e passar para o próximo video
#repetir por quantas vezes quiser