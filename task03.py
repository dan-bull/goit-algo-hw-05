from compare_search_algo import *
import timeit
import pandas as pd

def read_txt_file(file_path, encoding='utf-8'):
    try:
        with open(file_path, 'r', encoding = encoding) as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None

# Шлях до першого файлу
path_text1 = "/Users/asd/Documents/University_Code/Algorithms/стаття 1.txt"
file_1 = read_txt_file(path_text1)
# Шлях до другого файлу
path_text2 = "/Users/asd/Documents/University_Code/Algorithms/стаття 2.txt"
file_2 = read_txt_file(path_text2)

# Вихідні дані
functions = [kmp_search, boyer_moore_search, rabin_karp_search]
correct_pattern_1 = "Цільовий елемент порівнюється із середнім."
correct_pattern_2 = "Отже, вибір методів реалізації СУБД для зберігання даних рекомендаційної системи є важливою науково-практичною задачею."
incorrect_pattern = "Цього тексту тут не існує"

# Створюємо cловник куди будемо записувати результати
data = {"Алгоритм Пошуку": [], 
        "Час для пошуку існуючого тексту 1":[], 
        "Час для пошуку неіснуючого тексту 1":[], 
        "Час для пошуку існуючого тексту 2":[], 
        "Час для пошуку неіснуючого тексту 2":[]}

# Цикл пропрацьовує кожну функцію та записує результат у таблиці
for func in functions:
    run_search_correct_1 = timeit.timeit("func(file_1, correct_pattern_1)", number=10, globals=locals())

    run_search_incorrect_1 = timeit.timeit("func(file_1, incorrect_pattern)", number=10, globals=locals())

    run_search_correct_2 = timeit.timeit("func(file_2, correct_pattern_2)", number=10, globals=locals())

    run_search_incorrect_2 = timeit.timeit("func(file_2, incorrect_pattern)", number=10, globals=locals())

    
    data["Алгоритм Пошуку"].append(func.__name__)
    data["Час для пошуку існуючого тексту 1"].append(float(run_search_correct_1))
    data["Час для пошуку неіснуючого тексту 1"].append(float(run_search_incorrect_1))
    data["Час для пошуку існуючого тексту 2"].append(float(run_search_correct_2))
    data["Час для пошуку неіснуючого тексту 2"].append(float(run_search_incorrect_2))
    

df = pd.DataFrame(data)
print(df)
df.to_csv(r"Results.csv", index=False)

