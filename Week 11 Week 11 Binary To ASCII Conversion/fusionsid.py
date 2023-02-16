def binary_conversion(binary: str) -> str:
    return "".join(
        [
            chr(int(char, 2))
            for char in [binary[i : i + 8] for i in range(0, len(binary), 8)]
        ]
    )


# tests (all working):
print(
    binary_conversion(
        "010010010010000001101100011011110111011001100101001000000101010001100101011100110110100000100001"
    )
)
print(binary_conversion("001100010011001000110001001100110011000100110111"))
print(
    binary_conversion(
        "010000010110110101100001011110100110100101101110011001110010000001000101011001000110000101100010011010010111010000100001"
    )
)
