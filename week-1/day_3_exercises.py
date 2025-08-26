### DAY 3: EXERCISES FOR PYTHON PROGRAMMING
### EXERCISE 1: INPUTS
a = int(input("Primo Numero: "))
b = int(input("Secondo Numero: "))

somma = a + b
differenza = a - b
prodotto = a * b
divisione = round(a / b, 2)

risultati = {"somma": somma,
      "differenza": differenza,
      "prodotto": prodotto,
      "divisione": divisione}

print(risultati)

### EXERCISE 2: CONDITIONS
voto = int(input("Voto da 0 a 100: "))

if voto < 0 or voto > 100:
  print('Non Valido')
elif voto >= 90:
  print('A')
elif voto >= 80:
  print('B')
elif voto >= 70:
  print('C')
elif voto >= 60:
  print('D')
else:
  print('F')

### EXERCISE 3: FOR CYCLE
positivo = int(input("Numero Positivo: "))

for i in range(1, positivo + 1):
  print(i)

### EXERCISE 4: WHILE CYCLE
numero = int(input("Numero positivo: "))
contatore = 1
somma = 0

while contatore <= numero:
  somma += contatore
  contatore += 1

print(f"La somma da 1 a {numero} è: {somma}")

### EXERCISE 5: STRINGS
frase = str(input("Inserisci una frase: "))

frase = frase.strip().lower().replace("a", "*").replace("e", "*").replace("i", "*")

print(frase)

### EXERCISE 6: SUMMARY OF THE CHAPTERS
parola = str(input("Inserisci una parola: "))
parola_lower = parola.lower()

if len(parola) < 3:
  print("Troppo corta")
else:
  if parola_lower == parola_lower[::-1]:
    print("Palindromo")
  else:
    print("Non Palindromo")
