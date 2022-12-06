import win32clipboard
import os,platform

def pause():
    os.system('pause')

if platform.system().lower() != 'windows':
    print("This program doesn't work in linux")

win32clipboard.OpenClipboard()

while True:
    os.system('cls')
    choice = input('''
1) Get text from clipboard
2) Exit
Select: ''')

    if choice == '1':
        clipboard = win32clipboard.GetClipboardData()
        print('\n'+clipboard)
        pause()

    else:
        break

win32clipboard.CloseClipboard()
