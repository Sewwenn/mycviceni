#1.
#mm = float(input("Delka [mm]: "))
#cm = mm / 10
#m = mm / 1000
#palec = mm / 25.4
#print(f"Delka v cm: {cm:.3f}")
#print(f"Delka v m: {m:.3f}")
#print(f"Delka v palcich: {palec:.3f}")

#2.
total_secunts = int(input("Zadejte pocet sekund: "))
hours = total_secunts // 3600
minutes = (total_secunts % 3600) // 60
seconds = total_secunts % 60
print(f"{hours}:{minutes:02d}:{seconds:02d}")

#3.
#word = input("Zadejte slovo: ")
#print(f"Pocet znaku: {len(word)}")
#print(f"Prvni znak: {word[0]}")
#print(f"Posledni znak: {word[-1]}")
#print(f"Velke pismena: {word.upper()}")
#print(f"Slovo naopak: {word[::-1]}")
#wordlower = word.lower()
#print(f"Polindrom: {True if wordlower == wordlower[::-1] else False}")


#4. 
#for bits in [8, 16, 32, 64]:
# Беззнаковое число (unsigned)
#    min_unsigned = 0
#    max_unsigned = 2**bits - 1
        
#    # Знаковое число (signed)
#    min_signed = -2**(bits - 1)
#    max_signed = 2**(bits - 1) - 1
    
#print(f"{bits:2d} bitů: {min_unsigned} až {max_unsigned}, {min_signed} až {max_signed}")

#5. 
