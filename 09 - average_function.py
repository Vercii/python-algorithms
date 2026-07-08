def ave(scores):
    total = 0
    for i in scores:
        total += i
        
    return total / len(scores)

scores = []

amount = int(input("How many inputs?: "))

while amount != 0:
    input_num = int(input("Enter number: "))
    scores.append(input_num)
    amount -= 1

print(ave(scores))
