import unittest
#  Подключаем библиотеку для автоматических тестов.

from chatbot import normalize_text, tokenize_text, lemmatize_text, get_response
# Импортируем функции из файла chatbot.py, которые будем проверять.

class ChatBotTests(unittest.TestCase):
# Создаём класс с тестами для чат-бота.
      
    def test_greeting_response(self):
        # Проверяем ответ на приветствие.
        response, is_exit = get_response("Привет!")

        self.assertIn("учебный бот", response)
        self.assertFalse(is_exit)

    def test_ticket_response(self):
        # Проверяем ответ на вопрос про билеты.
        response, is_exit = get_response("Хочу купить билет")

        self.assertIn("город вылета", response)
        self.assertFalse(is_exit)

    def test_baggage_response(self):
        # Проверяем ответ на вопрос про багаж.
        response, is_exit = get_response("Какая норма багажа?")

        self.assertIn("зависит от тарифа", response)
        self.assertFalse(is_exit)

    def test_flight_status_response(self):
        # Проверяем ответ на вопрос про статус рейса.
        response, is_exit = get_response("Статус рейса 100")

        self.assertIn("Статус рейса", response)
        self.assertFalse(is_exit)

    def test_help_response(self):
        # Проверяем ответ на слово "помощь".
        response, is_exit = get_response("помощь")

        self.assertIn("билеты", response)
        self.assertFalse(is_exit)

    def test_unknown_question_returns_fallback(self):
        # Проверяем ответ на неизвестный вопрос.
        response, is_exit = get_response("Расскажи рецепт пирога")

        self.assertIn("не знаю ответа", response)
        self.assertFalse(is_exit)

    def test_empty_message_response(self):
        # Проверяем ответ на пустое сообщение.
        response, is_exit = get_response("   ")

        self.assertIn("Напишите вопрос", response)
        self.assertFalse(is_exit)

    def test_exit_response(self):
        # Проверяем завершение диалога.
        response, is_exit = get_response("До свидания")

        self.assertIn("До свидания", response)
        self.assertTrue(is_exit)

    def test_normalize_replaces_letter(self):
        # Проверяем нормализацию текста.
        self.assertEqual(normalize_text("  Самолёт123   летит  "), "самолет летит")

    def test_tokenize_returns_words(self):
        # Проверяем разбиение текста на слова.
        self.assertIn("багаж", tokenize_text("Багаж?"))

    def test_lemmatize_text_returns_normal_forms(self):
        # Проверяем лемматизацию слов.
        result = lemmatize_text("Билеты рейсы багажа")

        self.assertIn("билет", result)
        self.assertIn("рейс", result)
        self.assertIn("багаж", result)


if __name__ == "__main__":
    # Если файл запущен напрямую, запускаем тесты.
    unittest.main()