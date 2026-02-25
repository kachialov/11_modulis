# Nuosekli paieška
def sequential_search(data, target):
    for index in range(len(data)):
        if data[index] == target:
            return index
    return -1

# Dvejetainė paieška (duomenys turi būti surūšiuoti).
def binary_search(data, target):
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Pagrindinė programa
data1 = [64, 34, 25, 12, 22, 11, 90, 15, 5, 6]
data2 = [64, 34, 25, 12, 22, 11, 90, 15, 5, 6]

target = int(input("Įveskite paieškos reikšmė: "))

sequential_result = sequential_search(data1, target)
data2.sort()  # Dvejetainė paieška veikia tik su surūšiuotais duomenimis
binary_result = binary_search(data2, target)
    
print(f"Paieška: {target}")
if sequential_result == -1:
    print(f"Nuosekli paieška: NERASTA")
else:
    print(f"Nuosekli paieška: indeksas {sequential_result}, {target}=={data1[sequential_result]}")

if binary_result == -1:
    print(f"Dvejetainė paieška: NERASTA")
else:
    print(f"Dvejetainė paieška: indeksas {binary_result}, {target}=={data2[binary_result]}")
 
