import numpy as np
from Encoder import encoder


def calculate_parity_value(data, parity_number):
    count = 0
    for i in range(1, data.size+1):
        binary = decimal_to_binary(i)
        # print(data)
        if int(binary[len(binary) - parity_number]) == 1 and int(data[i - 1]) == 1:
            count += 1
    return 0 if count % 2 == 0 else 1


def decimal_to_binary(n):
    binary = bin(n).replace("0b", "")
    while len(binary) < 64:
        binary = '0' + binary
    return binary


def decoder(data_string, data_type, secded, message_size):
    # Split secded for check later
    if secded:
        secded_bit = data_string[len(data_string) - 1]
        data_string = data_string[0:len(data_string)-2]

    # Check if message size is valid
    num_parity_bits = len(data_string) - message_size
    if 2**num_parity_bits < message_size + num_parity_bits + 1 or 2**(num_parity_bits - 1) >= message_size + num_parity_bits + 1:
        return "Error: invalid message_size for input data of length " + str(len(data_string))

    # Determine positioning of parity bits
    parity_positions = []
    for i in range(num_parity_bits):
        parity_positions.append(2 ** i - 1)

    # Construct supposed initial message
    message = ""
    for i in range(len(data_string)):
        if not i in parity_positions:
            message += data_string[i]

    # Calculate parity bits
    calculated_parity = encoder(message, 'binary', False, message_size)
    test = np.array(list(data_string))
    if(calculated_parity != data_string):
        bitNumber = ''
        for i in range(num_parity_bits):
            bitNumber = str(calculate_parity_value(test, i + 1)) + bitNumber
        return "Error at " + str(int(bitNumber, 2))

    return "No errors: message is " + calculated_parity

print(decoder('0010110', 'binary', False, 4))