students = {
    'Морковкин': {'английский', 'китайский', 'французский'},
    'Огурчиков': {'английский', 'немецкий'},
    'Помидоров': {'китайский', 'японский'},
    'Картошечкин': {'русский', 'китайский', 'испанский'},
    'Капустин': {'английский'}
}

all_languages = set()
for langs in students.values():
    all_languages.update(langs)
print("Все языки:", sorted(all_languages))

chinese_speakers = [name for name, langs in students.items() if 'китайский' in langs]
print("Студенты, знающие китайский:", chinese_speakers)