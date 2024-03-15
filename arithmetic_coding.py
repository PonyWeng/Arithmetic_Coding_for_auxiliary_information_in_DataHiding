from random import random
from arithmetic_compressor import AECompressor
from arithmetic_compressor.models import StaticModel


def generate_random_string(length, p_one):
  """
  Generate a random location map of a specified length.

  Args:
    length: the length of the location map
    p_one: the probability of the symbol "1" in the location map

  Returns:
    Random Location Map
  """
  random_bits = [int(random() < p_one) for _ in range(length)]
  return ''.join(map(str, random_bits))

# Generate a location with a length of 262144 and a symbol "1" ratio of only 0.005.
random_string = generate_random_string(262144, 0.005)


########### Read your Location map file 
# with open('LocationMap.txt', 'r') as file:
#     input_string = file.read()


input_string = random_string

N=len(input_string)

# Automatically calculate the probabilities of each symbol.
chars = list(set(input_string))
frequencies = [input_string.count(char) for char in chars]
probabilities = [frequency / len(input_string) for frequency in frequencies]

# Create AECompressor Model
model = StaticModel(dict(zip(chars, probabilities)))

# Create Compressor
coder = AECompressor(model)

# Encode
encoded_string = coder.compress(input_string)

# Output
print(f"Input String：{input_string[:10]}",".....skipped")
print(f"encoded string：{encoded_string[:10]}",".....skipped")
print(f"Length of original string：{N}")
print(f"Length of encoded string：{len(encoded_string)}")

# Decode
decoded_data = coder.decompress(encoded_string,N)

decoded_string=""
for i in decoded_data:
    decoded_string+=i

# Comparison
print(f"Decoded String：{decoded_string[:10]}",".....skipped")
print("Is decoded string same as original string?",decoded_string==input_string)
print("Compression Rate =", 1-(len(encoded_string)/N))
