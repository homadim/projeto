
import itertools

# Função para calcular o hash
def calcula_hash(palavra):
    valor = 0
    for letra in palavra:
        valor += ord(letra)
    return valor


# Senha fictícia para demonstração
senha_nova = "mar"
hash_novo = calcula_hash(senha_nova)

# Pequeno conjunto de caracteres
caracteres = "amr"

print("Hash da senha:", hash_novo)
print("Testando combinações...")

# Demonstração de combinações possíveis
for combinacao in itertools.product(caracteres, repeat=len(senha_nova)):
    tentativa = "".join(combinacao)

    if calcula_hash(tentativa) == hash_novo:
        print("Combinação encontrada:", tentativa)

        if tentativa == senha_nova:
            print("Senha original encontrada!")
            break
