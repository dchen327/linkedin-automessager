import pyautogui
import platform
from time import sleep

cmd = 'cmd' if platform.system() == 'Darwin' else 'ctrl'
message = '''
hey!!
- testing linkedin messaging script
- bye :)
'''.strip()


def alt_tab():
    pyautogui.keyDown('alt')
    sleep(0.3)
    pyautogui.press('tab')
    sleep(0.3)
    pyautogui.keyUp('alt')


def hit_tab(num=1):
    for _ in range(num):
        pyautogui.hotkey('tab')
        sleep(0.2)


def load_links():
    with open('profile_links.txt') as f:
        return f.read().splitlines()


if __name__ == '__main__':
    links = load_links()
    alt_tab()
    for link in links:
        sleep(0.5)
        pyautogui.hotkey(cmd, 'l')  # go to address bar
        sleep(0.5)
        pyautogui.typewrite(link)
        sleep(0.3)
        pyautogui.hotkey('enter')  # load page
        sleep(4)  # wait for page load
        pyautogui.click(50, 300)
        hit_tab(2)
        pyautogui.hotkey('enter')  # hit connect button
        sleep(0.5)
        hit_tab(2)
        pyautogui.hotkey('enter')  # hit add note button
        sleep(0.5)
        pyautogui.typewrite(message)
        sleep(0.2)
        hit_tab(3)
        pyautogui.hotkey('enter')  # send message and connect
        sleep(1.5)
