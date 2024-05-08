def binary_search_float(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    count = 0
 
    while low <= high:
 
        mid = (high + low) // 2
        count += 1

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
 
        # інакше x присутній на позиції і повертаємо його
        else:
            return count, mid
    
    # Верхня межа
    upper_bound = arr[low] if low < len(arr) else None
    return count, upper_bound
 
array = [1.2, 3.4, 5.6, 7.8, 9.1]
target = 9.1

count, upper_bound = binary_search_float(array, target)

print(f"Кількість ітерацій: {count}")
print(f"Верхня межа: {upper_bound}")