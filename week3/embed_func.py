nums = [5, 12, 7, 18, 24, 3, 16]

evens = list(filter(lambda x: x % 2 == 0, nums))
print("Çift sayılar:", evens)

square = list(map(lambda x: x**2, evens))
print("Kareleri:", square)

sort = sorted(square, reverse=True)
print("Azalan sırada:", sort)
