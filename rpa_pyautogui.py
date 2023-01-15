import pyautogui
import time

def main():
    # avisar usuário que o pyautogui vai rodar
    pyautogui.alert('Pyautogui será executado. Não use teclado ou mouse enquanto o programa estiver executando')

    # acrescenta intervalo de 0.5s antes de cada comando a ser executado
    pyautogui.PAUSE = 0.5

    # apertar botão windows
    pyautogui.press('win')

    # escrever textMaker
    pyautogui.write('textMaker')

    # pressionar enter
    pyautogui.press('enter')

    # escrever um texto
    pyautogui.write('Hello World!')
    time.sleep(0.5)

    # ctrl+S
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)

    # levar o mouse até o googledrive
    pyautogui.moveTo(86, 406)

    # clicar googledrive
    pyautogui.click()
    time.sleep(1)

    # Levar mouse até meu drive
    pyautogui.moveTo(388, 208)

    # clique duplo
    pyautogui.doubleClick()
    time.sleep(1)

    # levar mouse até nome
    pyautogui.moveTo(267, 458)

    # clicar em nome
    pyautogui.click()

    # escrever nome do arquivo
    pyautogui.write('pyautogui_test')

    # pressionar enter
    pyautogui.press('enter')

    # avisar usuário que o programa já rodou
    pyautogui.alert('O programa já foi executado. Pode voltar a usar o computador')


if __name__ == "__main__":
    main()
