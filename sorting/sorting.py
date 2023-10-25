def bubble_sort(names):
    n = len(names)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if names[j] > names[j + 1]:
                names[j], names[j + 1] = names[j + 1], names[j]
names = input("Enter a list of names").split()

bubble_sort(names)
for name in names:
    print(name)
