# Файл cloc.py
# В этом файле находится главный сценарий программы



from ui import AppUI

# Главный сценарий
def main():

    MainObject = AppUI()
    MainObject.make_ui()
    MainObject.start()



if __name__ == "__main__":
    main()