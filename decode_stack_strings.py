def decode_little_endian():
    print("[*] Début du décodage des Stack Strings (UnCrackable 2)...")
    
    # Les variables hexadécimales trouvées dans Ghidra (uStack_30 à uStack_1a)
    hex_variables = [
        "6e616854", # uStack_30
        "6620736b", # uStack_2c
        "6120726f", # uStack_28
        "74206c6c", # uStack_24
        "6568",     # uStack_20
        "73696620", # uStack_1e
        "68"        # uStack_1a
    ]
    
    secret_password = ""
    
    for hex_val in hex_variables:
        # 1. Convertir la chaîne hexadécimale en octets (bytes)
        byte_data = bytes.fromhex(hex_val)
        
        # 2. Inverser l'ordre des octets (règle du Little Endian)
        little_endian_data = byte_data[::-1]
        
        # 3. Convertir les octets en texte ASCII
        secret_password += little_endian_data.decode('utf-8')
        
    print(f"[+] Décodage réussi ! Le mot de passe est : '{secret_password}'")

if __name__ == "__main__":
    decode_little_endian()