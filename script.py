import pyautogui
import time

def abrir_bloc_notas():
    """Abre el Bloc de notas y escribe un mensaje."""
    pyautogui.hotkey('win', 'r')  # Abre ejecutar
    time.sleep(1)
    pyautogui.write('notepad')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write('Hola, este es un mensaje automatizado.', interval=0.1)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'g')  # Guardar archivo
    time.sleep(1)
    pyautogui.write('notaAutomatica.txt')
    pyautogui.press('enter')

if __name__ == "__main__":
    abrir_bloc_notas()
