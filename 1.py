countries_capitals = {
    "Россия": "Москва",
    "Белорусь": "Минск",
    "Германия": "Берлин",
    "Италия": "Рим",
    "Испания": "Мадрид"
}
country_name = input("Введите название страны, чтобы узнать ее столицу: ").strip()
capital = countries_capitals.get(country_name)
if capital:
    print(f"Столица {country_name} - {capital}")
else:
    print("Ошибка: такая страна не найдена в списке.")

print("\nСтраны и их столицы в алфавитном порядке:")
for country in sorted(countries_capitals.keys()):
    print(f"{country}: {countries_capitals[country]}")