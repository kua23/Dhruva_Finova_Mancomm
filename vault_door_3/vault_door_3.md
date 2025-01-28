# vault-door-3

## Challenge
This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java]

## Solution
Simple reverse engineering [script](solve.py) in Python:
```py
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
```
This returns the flag.

## Flag
`picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_c79a21}`