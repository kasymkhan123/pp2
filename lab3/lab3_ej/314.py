n = int(input())
numbers = list(map(int, input().split()))
n_oper = int(input())
for k in range(n_oper):
    operations = input().split()
    if operations[0] == "abs":
        numbers = list(map(lambda x: abs(x), numbers))
    elif operations[0] == "add":
        numbers = list(map(lambda x: x + int(operations[1]), numbers))
    elif operations[0] == "multiply":
        numbers = list(map(lambda x: x * int(operations[1]), numbers))
    elif operations[0] == "power":
        numbers = list(map(lambda x: x ** int(operations[1]), numbers))
print(*numbers)
