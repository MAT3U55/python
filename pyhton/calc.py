def multiplique(num1, num2):
    return round(num1 * num2, 4)

def main():
    num1 = float(input("digite um número "))
    num2 = float(input("digite mais um numero "))

    print(multiplique(num1, num2))

main()