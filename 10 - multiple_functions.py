def ave(scores):
    total = 0
    for i in scores:
        total += i
        
    return total / len(scores)

def highest(scores):
    total = scores[0] # sets the value based on the first index
    for i in scores:
        if i > total:
            total = i
    return total

def lowest(scores):
    total = scores[0]
    for i in scores:
        if i < total:
            total = i
    return total

scores = []

amount = int(input("How many students?: "))
cnt = 1

while amount != 0:
    input_num = int(input(f"Score of student {cnt}: "))
    scores.append(input_num)
    cnt += 1
    amount -= 1

print("Average: ", ave(scores))
print("Highest: ", highest(scores))
print("Lowest: ", lowest(scores))

