triplet_to_dig = {
    "ZER" : 0,
    "ONE" : 1,
    "TWO" : 2, 
    "THR" : 3, 
    "FOU" : 4, 
    "FIV" : 5, 
    "SIX" : 6, 
    "SEV" : 7,
    "EIG" : 8, 
    "NIN" : 9
}
dig_to_triplet = {}
for k, v in triplet_to_dig.items():
    dig_to_triplet[v] = k
def triplets_to_number (s):
    n = ""
    for k in range(0, len(s), 3):
        n += str(triplet_to_dig[s[k:k+3]])
    return int(n)
def number_to_triplet (num) :
    num_str = str(num)
    result = ""
    for i in num_str:
        dig = int(i)
        triplet = dig_to_triplet[dig]
        result += triplet
    return result
def ww(expr) :
    for ope in "+-*/":
        if ope in expr:
            a, b = expr.split(ope)
            return a, b, ope
expr = input()
num1_str, num2_str, operator = ww(expr)

num1 = triplets_to_number(num1_str)
num2 = triplets_to_number(num2_str)

if operator == "+":
    rr = num1 + num2
elif operator == "-":
    rr = num1 - num2 
elif operator == "*":
    rr = num1 * num2

result = number_to_triplet(rr)

print(result)

    






    
