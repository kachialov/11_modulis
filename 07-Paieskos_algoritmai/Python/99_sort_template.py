def search(arr, search_value):
    # ToDo: parašyti paieškos algoritmą
    return -1

arr = [64, 34, 25, 12, 22, 11, 90, 15, 5, 6]
search_value = 15
found_index = search(arr, search_value)

if found_index == -1:
    print(f"Ieskomas elementas \"{search_value}\" nerastas.")

print(f"Ieskomo elemento \"{search_value}\" indeksas yra {found_index} ir reiksme lygi \"{arr[found_index]}\".")
