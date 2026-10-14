turns=int(input())
health=100+(4*turns)-(6*turns)
if health < 0:
    health=0
print(health)