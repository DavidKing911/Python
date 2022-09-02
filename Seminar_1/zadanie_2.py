# 2-Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
# Предикату можно заменить на понятие "бит".

def check():
    print("-"*15)
    print("X", "Y", "Z", "result", sep="  ")
    print("-"*15)
    for X in range(2):
        for Y in range(2):
            for Z in range(2):
                if not(X or Y or Z) == (not(X) and not(Y) and not(Z)):
                    print(f"{X}  {Y}  {Z} - True")
                else:
                    print(f"{X}  {Y}  {Z} - False")

check()