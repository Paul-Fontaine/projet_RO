def number_to_bits(n):
    # Get the binary representation of the number
    binary_representation = bin(n)[2:]  # Remove the '0b' prefix
    # Convert the binary string to a list of bits (integers)
    bits = [int(bit) for bit in binary_representation]
    bits.reverse()
    return bits


N = 4
objets = list(range(N))
combinaisons = []

for i in range(2**N):
    bits = number_to_bits(i)
    combi = [j for j, add in enumerate(bits) if add]
    print(f"i = {i}   ", "bin : ", bits)
    print(combi)
    print()
    combinaisons.append(combi)

print(combinaisons)