# Допишите в вашу задачу Archive обработку исключений.
# Добавьте исключение в ваш код InvalidTextError, которые будет вызываться,
# когда текст не является строкой или является пустой строкой.
# И InvalidNumberError, которое будет вызываться, если число не
# является положительным целым числом или числом с плавающей запятой.


class InvalidTextError(Exception):
    pass


class InvalidNumberError(Exception):
    pass


class Archive:
    def __init__(self, text, number):
        if not isinstance(text, str) or not text:
            raise InvalidTextError(f"Invalid text: {text}. Text should be a non-empty string.")

        if not (isinstance(number, int) and number > 0) and not (isinstance(number, float) and number > 0):
            raise InvalidNumberError(f"Invalid number: {number}. Number should be a positive integer or float.")

        self.text = text
        self.number = number

    def __str__(self):
        return f"Text is {self.text} and number is {self.number}. Also [] and []"