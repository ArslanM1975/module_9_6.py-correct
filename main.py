def all_variants(text):
    length = len(text)
    # Генерируем все возможные подпоследовательности
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield text[start:end]

# Использование функции-генератора
a = all_variants("abc")

# Сохраним все сгенерированные подпоследовательности в списке
subsequences = list(a)

# Сортируем сначала по длине, затем по алфавиту
subsequences = sorted(set(subsequences), key=lambda x: (len(x), x))

# Выводим подпоследовательности по заданному формату
for subseq in subsequences:
    print(subseq)