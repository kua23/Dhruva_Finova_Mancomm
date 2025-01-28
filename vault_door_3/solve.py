def reverse_engineer_flag():
    transformed = "jU5t_a_sna_3lpm12g94c_u_4_m7ra41"
    password = [''] * 32
    for i in range(8):
        password[i] = transformed[i]
    for i in range(8, 16):
        password[i] = transformed[23 - i]
    for i in range(16, 32, 2):
        password[i] = transformed[46 - i]
    for i in range(31, 16, -2):
        password[i] = transformed[i]
    original_password = ''.join(password)
    flag = f"picoCTF{{{original_password}}}"
    return flag
flag = reverse_engineer_flag()
print("The flag is:", flag)