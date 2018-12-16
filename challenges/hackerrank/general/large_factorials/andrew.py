def main(n):
    if n == 1:
        return 1
    return main(n - 1) * n

print(main(950))