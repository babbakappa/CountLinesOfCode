# Файл cloc.py
# В этом файле находится главный сценарий программы


# TODO: Добавить возможность выбирать конкретные
#  файлы или возможность исключать папки (в случае с Python например .venv)


from ui import AppUI

# Главный сценарий
def main():

    MainObject = AppUI()
    MainObject.make_ui()
    MainObject.start()



if __name__ == "__main__":
    main()