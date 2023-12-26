def test_et(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))


print(test_et(1000))
print(test_et(900))
print(test_et(800))
print(test_et(2200))
