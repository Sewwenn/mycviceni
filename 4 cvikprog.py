# kolvo = 0
# number = 0
# large = None
# while True:
#     cislo = input("Číslo (Enter = konec): ")
#     if cislo == "":
#         break
#     number = int(cislo)
#     kolvo += 1
#     if large is None or large < number:
#         large = number
# if large is None:
#     print("Nebylo zadáno žádné číslo.")
# else:
#     print(f"Počet: {kolvo}")
#     print(f"Maximum: {large}")

#1
# diameters = [25.01, 24.97, 25.06, 25.00, 24.94, 25.03, 25.05, 24.95, 25.10, 24.99]
# diametr_cil = 25
# for diametr in diameters:
#     oshybka = diametr - diametr_cil
#     if oshybka >= -0.05 and oshybka <= 0.05:
#         print(f"{diametr}: OK")
#     if oshybka > 0.05:
#         print(f"{diametr}: VELKÝ")
#     if oshybka < -0.05:
#         print(f"{diametr}: MALÝ")


#2
# kolvo = 0
# for rok in range(1890, 2031):
#     if (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0): 
#         kolvo += 1
#         print(rok, end=" ")
#         if kolvo % 10 == 0:
#                 print()


#3
# n = int(input())
# num = n ** 0.5
# for cislo in range(2, int(num) + 1):
#     if n % cislo == 0:
#         print("Není prvočíslo")
#         break
# else:
#     print("Je prvočíslo")
   
#4

# h = int(input("Zadejte výšku: "))
# if h % 2 == 0 or h < 0:
#     print("Zadaná výška musí být lichá a kladná.")
#     exit()
# else:
#     print("Zadaná výška je lichá a kladná.")
#     print((h-1) // 2 * " " + (h // h) * "*" + (h-1) // 2 * " ")
#     for shyryna in range(1, ((h - 1) // 2)):
#         print(((h - 1) // 2 - shyryna) * " " + "*" + (2 * shyryna - 1) * " " + "*")

#     print("*" + (h - 2) * " " + "*")

#     for shyryna2 in range((h - 1) // 2 - 1, 0, -1):
#         print(((h - 1) // 2 - shyryna2) * " " + "*" + (2 * shyryna2 - 1) * " " + "*")
#     print((h-1) // 2 * " " + (h // h) * "*" + (h-1) // 2 * " ")
        

# oshybka: print(shyryna * " " + "*" + (h - 2) * " " + "*", end="\n")
# pravilno: print(((h - 1) // 2 - shyryna) * " " + "*" + (2 * shyryna - 1) * " " + "*")

# oshybka:print(shyryna2 * " " + "*" + (h - 2) * " " + "*", end="\n")
# pravilno: print(((h - 1) // 2 - shyryna2) * " " + "*" + (2 * shyryna2 - 1) * " " + "*")


#5.


