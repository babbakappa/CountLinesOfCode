# Файл core.py
# В этом модуле написаны функции поиска файлов,
# подсчета количества строк и другое


from pathlib import Path
import os
from tkinter import filedialog

from lang import detect_language


# В эту функцию подаются готовый список расширений
def get_file_list(dir_path, file_extensions_list):
    res = []
    for e in file_extensions_list:
        res += list(Path(dir_path).rglob(f"*.{e}"))
    return res


# В эту функцию подается список ссылок на файлы
def count_lines_of_code(file_list):
    result = 0
    for p in file_list:
        try:
            with open(p, "r", encoding="utf-8") as f:
                # Добавляем число строк в одном файле
                result = result + len(f.readlines())
        except:
            continue
    # Возвращаем число строк
    return result

# Возвращает путь к папке
def get_dir_path():
    return filedialog.askdirectory(title="Выберите папку")

# Функция возвращающая список расширений,
# подается список ссылок на файлы
def search_for_extensions(file_list):
    result = []
    for p in file_list:
        p = p.split(".", 1)[1]
        result.append(p)
    return result

# Функция возвращающая список языков к файлам,
# подается список расширений
def determine_languages(exts):
    result = []
    for e in exts:
        r = detect_language(e)
        if r not in result:
            result.append(r)
    return result

# Красиво формируется строка из языков,
# подается список языков
def make_lang_str(langs):
    res = ""
    if len(langs) == 0:
        return "Нет языков"

    if len(langs) == 1:
        return langs[0]

    if (len(langs) > 1):
        for l in langs:
            res = res + l + ", "
        res = res[:-2]
        return res

def prepare_exts(strexts):
    if not strexts.strip():
        return []
    return [ext.strip().lower().lstrip('.') for ext in strexts.split(',')]