def inverte(s):
    string = ""
    for i in range(len(s)-1, -1, -1):
        string += s[i]
    return string

original = input("Digite uma string: ")
invertida = inverte(original)

print(f"A string original é: {original}")
print(f"A string invertida é: {invertida}")