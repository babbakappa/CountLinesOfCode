# Файл ui.py
# В этом файле написан класс для интерфейса,
# который взаимодействует с core.py, сам интерфейс
# работает на tkinter и customtkinter


import customtkinter as ctk
from tkinter import messagebox as msgbx

from pyparsing import replaceWith

import core


class AppUI:

    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("800x400")  # Немного увеличили окно для вместительности
        self.root.title("Подсчет строк кода")
        self.root.resizable(False, False)

        self.current_path = ""
        self.files = []
        self.how_much_lines = 0
        self.languages = []

    def make_ui(self):
        # Главный заголовок
        top_text = ctk.CTkLabel(master=self.root,
                                text="Подсчет строк кода",
                                font=("Segoe UI", 20, "bold"))
        top_text.pack(pady=(20, 10))

        # Контейнер для полей ввода (используем grid для выравнивания)
        self.input_container = ctk.CTkFrame(master=self.root, fg_color="transparent")
        self.input_container.pack(pady=10, padx=20, fill="x")

        # Строка 1: Путь к папке
        lbl_path = ctk.CTkLabel(master=self.input_container, text="Путь к папке:")
        lbl_path.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.input_field = ctk.CTkEntry(master=self.input_container, width=350)
        self.input_field.grid(row=0, column=1, padx=5, pady=5)

        select_dir_button = ctk.CTkButton(master=self.input_container,
                                          text="Выбрать",
                                          width=90,
                                          command=self.if_pressed_sdb)
        select_dir_button.grid(row=0, column=2, padx=5, pady=5)

        # Строка 2: Расширения
        lbl_ext = ctk.CTkLabel(master=self.input_container, text="Расширения (через запятую):")
        lbl_ext.grid(row=1, column=0, sticky="w", padx=5, pady=5)

        self.input_ext_field = ctk.CTkEntry(master=self.input_container, width=350, placeholder_text="py, js, cpp")
        self.input_ext_field.grid(row=1, column=1, padx=5, pady=5)

        # Кнопка анализа
        analyze_button = ctk.CTkButton(master=self.root,
                                       text="Анализировать",
                                       font=("Segoe UI", 14, "bold"),
                                       fg_color="#1f538d",
                                       command=self.if_pressed_analyze)
        analyze_button.pack(pady=15)

        # Фрейм результатов (используем pack для внутренних элементов)
        self.result_container = ctk.CTkFrame(master=self.root)
        # Он скрыт изначально, появится после клика

        self.top_result_text = ctk.CTkLabel(master=self.result_container,
                                            text="Результаты анализа:",
                                            font=("Segoe UI", 14, "bold"))
        self.top_result_text.pack(anchor="w", padx=15, pady=(10, 5))

        self.show_lines = ctk.CTkLabel(master=self.result_container,
                                       text="",
                                       font=("Segoe UI", 13))
        self.show_lines.pack(anchor="w", padx=15, pady=2)

        self.show_langs = ctk.CTkLabel(master=self.result_container,
                                       text="",
                                       font=("Segoe UI", 13))
        self.show_langs.pack(anchor="w", padx=15, pady=(2, 10))

    def make_results_appear(self):
        # Отображаем контейнер с результатами целиком
        self.result_container.pack(pady=10, padx=20, fill="x")

        # Динамически обновляем текст в виджетах
        self.show_lines.configure(text=f"Всего строк кода: {self.how_much_lines}")
        self.show_langs.configure(text=f"Обнаруженные языки: {self.form_langs}")

    def analyze_given(self):
        # Берем актуальный путь из поля ввода на случай, если его ввели вручную
        self.current_path = self.input_field.get()
        raw_ext = self.input_ext_field.get()

        if not raw_ext and not self.current_path:
            msgbx.showwarning("Предупреждение", "Вы не указали путь и тип файлов")
            return

        if not raw_ext:
            msgbx.showwarning("Предупреждение", "Вы не указали тип файлов")
            return

        if not self.current_path:
            msgbx.showwarning("Предупреждение", "Пожалуйста, выберите или введите путь к папке!")
            return False

        # Получаем чистый список расширений
        to_work_with_exts = core.prepare_exts(raw_ext)

        # Получаем файлы и считаем строки
        self.files = core.get_file_list(self.current_path, to_work_with_exts)
        self.how_much_lines = core.count_lines_of_code(self.files)

        # Если расширения не были введены, берем их автоматически из найденных файлов
        if not to_work_with_exts:
            detected_exts = core.search_for_extensions(self.files)
            self.languages = core.determine_languages(detected_exts)
        else:
            self.languages = core.determine_languages(to_work_with_exts)

        self.form_langs = core.make_lang_str(self.languages)
        return True

    # Если нажали на "Выбор"
    def if_pressed_sdb(self):
        self.current_path = core.get_dir_path()
        self.input_field.delete(0, "end")
        self.input_field.insert(0, self.current_path)

    # Если нажали "Анализировать"
    def if_pressed_analyze(self):
        if self.analyze_given():
            self.make_results_appear()

    def start(self):
        self.root.mainloop()