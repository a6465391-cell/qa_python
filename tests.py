import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_genre(self):
        collector = BooksCollector()
        book_name = "Гарри Поттер"
        valid_genre = "Фантастика"  
        collector.add_new_book(book_name)
        
        assert collector.get_book_genre(book_name) == ""

        collector.set_book_genre(book_name, valid_genre)
        result = collector.get_book_genre(book_name)
        assert result == valid_genre, f"Ожидание '{valid_genre}', результат '{result}'"

    @pytest.mark.parametrize(
        "book_name, genre_to_set, expected_result",
        [
            # Сценарий 1: Книга есть, жанр установлен -> получаем жанр
            ("Гарри Поттер", "Фантастика", "Фантастика"),
            
            # Сценарий 2: Книга есть, но жанр пустой -> получаем ''
            ("1984", "", ""), 
            
            # Сценарий 3: Книги нет вообще -> получаем None
            ("Неизвестная книга", None, None), 
        ],
        ids=[
            "existing_with_genre", 
            "existing_no_genre", 
            "missing_book"
        ]
    )
    def test_get_book_genre_scenarios(self, book_name, genre_to_set, expected_result):
       
        collector = BooksCollector()
       
        if expected_result is not None:
            collector.add_new_book(book_name)
            if genre_to_set is not None:
                collector.set_book_genre(book_name, genre_to_set)
        
        result = collector.get_book_genre(book_name)       
        assert result == expected_result, (
            f"Книга '{book_name}' с жанром '{genre_to_set}' "
            f"ожидание {expected_result}, результат {result}"
        )  

    def test_favorites_operations(self):
        collector = BooksCollector()
        book_name = "Гарри Поттер"
       
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)       
        assert book_name in collector.get_list_of_favorites_books()

        collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 1

        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 0  

    def test_get_books_for_children_filtering(self):
        collector = BooksCollector()       
        collector.add_new_book("Добрая сказка")
        collector.set_book_genre("Добрая сказка", "Мультфильмы")
        collector.add_new_book("Страшный триллер")
        collector.set_book_genre("Страшный триллер", "Ужасы")
        children_books = collector.get_books_for_children()
        assert "Добрая сказка" in children_books, "Детская книга"
        assert "Страшный триллер" not in children_books, "Книга для взрослых" 

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Фэнтези 1")
        collector.set_book_genre("Фэнтези 1", "Фантастика")
        collector.add_new_book("Фэнтези 2")
        collector.set_book_genre("Фэнтези 2", "Фантастика")
        collector.add_new_book("Другая книга")
        collector.set_book_genre("Другая книга", "Детективы")

        result = collector.get_books_with_specific_genre("Фантастика")
        assert len(result) == 2
        assert "Фэнтези 1" in result
        assert "Фэнтези 2" in result
        assert "Другая книга" not in result

    def test_get_books_genre_returns_full_dict(self):
        collector = BooksCollector()
        collector.add_new_book("Книга А")
        collector.set_book_genre("Книга А", "Комедии")        
        collector.add_new_book("Книга Б")
        collector.set_book_genre("Книга Б", "Мультфильмы")

        result = collector.get_books_genre()
        assert result.get("Книга А") == "Комедии"
        assert result.get("Книга Б") == "Мультфильмы"
        assert len(result) == 2

    