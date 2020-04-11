import numpy as np


def calculate_parity_value(data, parity_number):
    count = 0
    for i in range(1, data.size+1):
        binary = decimal_to_binary(i)
        if int(binary[len(binary) - parity_number]) == 1 and data[0, i - 1] == 0:
            count += 1

    return 0 if count % 2 == 0 else 1


def decimal_to_binary(n):
    binary = bin(n).replace("0b", "")
    while len(binary) < 64:
        binary = '0' + binary
    return binary


def hex_to_binary_string(n):
    return bin(int(n, 16)).replace("0b", "")


def decimal_to_binary_string(n):
    return bin(int(n)).replace("0b", "")


def encoder(data_string, data_type, secded, input_size):
    # Check for input errors and convert to binary
    valid_binary = ['0', '1']
    valid_decimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    valid_hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

    data_string = data_string.lower().strip()

    if data_type == 'binary':
        for i in range(len(data_string)):
            if not data_string[i] in valid_binary:
                return 'Error: invalid binary character'
    elif data_type == 'hex':
        for i in range(len(data_string)):
            if not data_string[i] in valid_hex:
                return 'Error: invalid hex character'
        data_string = hex_to_binary_string(data_string)
    else:
        for i in range(len(data_string)):
            if not data_string[i] in valid_decimal:
                return 'Error: invalid decimal character'
        data_string = decimal_to_binary_string(data_string)

    # Check input size and extend if necessary
    if input_size < len(data_string):
        return "Input too large for selected input size"
    elif input_size > len(data_string):
        while input_size > len(data_string):
            data_string = '0' + data_string

    # Calculate number of parity bits (not considering secded yet)
    print(data_string)
    data = np.array(list(data_string))
    num_parity_bits = 0
    while 2**num_parity_bits < len(data) + num_parity_bits + 1:
        num_parity_bits += 1

    # Create numpy array representing output string and recognize parity bit positioning
    out_w_parity = np.zeros((1, num_parity_bits + len(data)))
    parity_positions = []
    for i in range(num_parity_bits):
        parity_positions.append(2**i - 1)

    # Fill the rest of the array with data
    data_counter = 0
    for i in range(out_w_parity.size):
        if not i in parity_positions:
            out_w_parity[0, i] = data[data_counter]
            data_counter += 1

    # Calculate parity bits
    for i in range(num_parity_bits):
        out_w_parity[0, parity_positions[i]] = calculate_parity_value(out_w_parity, i + 1)

    secded_bit = 0 if int(np.sum(out_w_parity)) % 2 == 0 else 1
    if secded:
        out_w_parity = np.append(out_w_parity[0], secded_bit)
    return np.array2string(out_w_parity)


print(encoder('0110', 'binary', False, 4))
print(encoder('6', 'decimal', False, 4))
print(encoder('6', 'hex', False, 4))
