import random

zero_digit = [1, 1, 1, 1, 1,
              1, 0, 0, 0, 1,
              1, 0, 0, 0, 1,
              1, 0, 0, 0, 1,
              1, 1, 1, 1, 1]

targets = [[1 if i == j else 0 for i in range(10)]
           for j in range(10)]

random.seed(0)
input_size = 25
num_hidden = 5
output_size = 10

hidden_layer = [[random.random() for _ in range(input_size + 1)]
                for _ in range(num_hidden)]

output_layer = [[random.random() for _ in range(num_hidden + 1)]
                for _ in range(output_size)]

network = [hidden_layer, output_layer]
