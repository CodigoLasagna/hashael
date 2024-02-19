import time
tiempo_espera = 1

def nohashael(valor_encriptado, llave):
    texto_original = ""
    key_val = sum(ord(c) for c in llave)
    valores = [int(num) for num in valor_encriptado.split("-")]
    first_key = 0
    hash_value = ""
    for i in range(len(valores)):
        time.sleep(tiempo_espera)
        if i > 0:
            hash_value = chr(int(valores[i] / (key_val ** first_key)))
            texto_original += hash_value
            print("[" + str(valores[i]) + "]", "/", "([llave: " + str(key_val) + "]", "//", "[primer valor: " + str(first_key) + "]) =", hash_value)
        else:
            texto_original += chr(int(valores[i]))
            print(str(valores[i]), "=" ,chr(int(valores[i])))
            first_key = valores[i]

    return texto_original


def hashael(texto, llave):
    hash = ""
    key_val = sum(ord(c) for c in llave)
    print("llave: ", llave, "=", key_val)
    first_key = 0
    hash_value = ""
    for i in range(len(texto)):
        valor_ascii = ord(texto[i])
        time.sleep(tiempo_espera)
        if i > 0:
            hash_value = str(valor_ascii * (key_val ** first_key))
            hash += hash_value
            print("[" + texto[i] + ":", str(valor_ascii) + "]", "*", "([llave: " + str(key_val) + "]", "**", "[primer valor: " + str(first_key) + "]) =", hash_value)
        else:
            first_key = valor_ascii
            hash += str(valor_ascii)
            print("[" + texto[i] + ":", str(valor_ascii) + "]")
        if i < len(texto)-1:
            hash += '-'
    
    return hash

entrada = "hola"
#entrada = "hola como estas, yo muy bien gracias por tenerme aquí, este texto esta super largo porque no tenía de otra osi osi, pero bueno aquí ya termina"
llave = "a"
print("\033[91mEntrada:", entrada)
print("\033[92m")
hash_resultante = hashael(entrada, llave)
time.sleep(0.5)
print("\033[94m")

#print("\033[92mHash resultante:", hash_resultante)
print("")

cadena_original = nohashael(hash_resultante, llave)
print("\033[96mCadena original encontrada:", cadena_original)

