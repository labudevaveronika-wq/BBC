import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel
)

class Analizator(QWidget): # создаем класс Analizator, который наследуется от QWidget
    def __init__(self):
        super().__init__() # вызываем конструктор родительского класса


        self.setWindowTitle("Анализ Вашего текста") # заголовок
        self.setFixedSize(600, 500)
        layout = QVBoxLayout() # все элементы будут располагаться друг под другом

        self.text_edit = QTextEdit() # текстовое поле для ввода текста
        layout.addWidget(self.text_edit) # добавляет виджет в layout

        self.btn_Analizator = QPushButton("Анализ Вашего текста:") # кнопка
        self.btn_Analizator.clicked.connect(self.analyze_text) # привязывает функцию analyze_text к событию нажатия на кнопку
        layout.addWidget(self.btn_Analizator)


        self.result_label = QLabel("Тут будет анализ Вашего текста")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def analyze_text(self):
        your_text = self.text_edit.toPlainText()

        chars = len(your_text) # подсчитывает общее количество символов в тексте
        plase = your_text.count(" ") # подсчитывает количество пробелов
        chars_no_plase = len(your_text.replace(" ", "")) # подсчитывает количество символов без пробелов

        result = (
            f"Всего символов: {chars}\n"
            f"Пробелов: {plase}\n"
            f"Символов без пробелов: {chars_no_plase}"
        )

        self.result_label.setText(result)

if __name__ == "__main__": # запуск
    app = QApplication(sys.argv)
    window = Analizator()
    window.show()
    sys.exit(app.exec())
