# test_add_new_book_add_two_books. Проверил, что метод корректно добавляет книги и их количество.
# test_add_new_book_sets_empty_genre. Проверил, что у только что добавленной книги жанр по умолчанию пустой ('').
# test_set_book_genre_successfully_updates_genre. Проверил, что метод корректно меняет жанр у существующей книги. 
# test_get_book_genre_scenarios (параметризованный). Проверил, что книга есть, жанр установлен, книга есть, но жанр пустой, книги не существует.
# test_add_to_favorites_success. Проверил, что книга успешно добавляется в список избранного. 
# test_add_to_favorites_ignores_duplicate. Проверил, что повторное добавление книги не увеличивает длину списка.
# test_remove_from_favorites. Проверил, что книга корректно удаляется из списка избранного. 
# test_children_books_includes_allowed_genre. Проверил, что книги с детскими жанрами попадают в список. 
# test_children_books_excludes_restricted_genre. Проверил, что книги с возрастными ограничениями не попадают в список детских книг. 
# test_get_books_with_specific_genre_returns_correct_count. Проверил, что количество найденных книг соответствует ожидаемому. 
# test_get_books_with_specific_genre_includes_target_books. Проверил, что в списке есть именно те книги, которые искал. 
# test_get_books_with_specific_genre_excludes_other_genres. Проверил, что в списке нет книг, не относящихся к целевому жанру. 
# test_get_books_genre_returns_correct_keys. Проверил, что в словаре присутствуют правильные названия книг. 
# test_get_books_genre_returns_correct_values. Проверил, что у книг стоят правильные жанры. 
# test_get_books_genre_returns_correct_length. Проверил, что общее количество книг в словаре соответствует ожидаемому. 