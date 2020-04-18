import tkinter as tk
from Encoder import encoder
from Decoder import decoder


def encode():
    output = encoder(encode_data.get(), encode_radio.get(), encode_secded.get(), int(encode_bits_option.get()))
    output_text.set(output)

win = tk.Tk()
win.title("Hamming Encoder/Decoder")
win.geometry("500x300")

# Setup encode interface
encode_data = tk.Entry(width=60)

encode_button = tk.Button(win, text="Encode", command=encode)

encode_bits = []
for i in range(1, 33):
    encode_bits.append(i)
encode_bits_option = tk.StringVar(win)
encode_bits_option.set(encode_bits[0])
encode_dropdown = tk.OptionMenu(win, encode_bits_option, *encode_bits)

encode_radio = tk.StringVar()
encode_binary_radio = tk.Radiobutton(win, text="Binary", variable=encode_radio, value="binary")
encode_decimal_radio = tk.Radiobutton(win, text="Decimal", variable=encode_radio, value="decimal")
encode_hex_radio = tk.Radiobutton(win, text="Hexadecimal", variable=encode_radio, value="hex")
encode_radio.set("binary")

encode_secded = tk.BooleanVar()
encode_secsed_radio = tk.Radiobutton(win, text="SECSED", variable=encode_secded, value=False)
encode_secded_radio = tk.Radiobutton(win, text="SECDED", variable=encode_secded, value=True)
encode_secded.set(False)

label_encoder = tk.Label(win)
label_encoder["text"] = "Encoder"

output_text = tk.StringVar()
encode_output = tk.Entry(win, state='readonly', textvariable=output_text, width=40)
scroll = tk.Scrollbar(win, orient='horizontal', command=encode_output.xview)
encode_output.config(xscrollcommand=scroll.set)
encode_output_label = tk.Label(win)
encode_output_label["text"] = "Encode Output: "

label_encoder.grid(row=0, column=0, sticky="W")
encode_data.grid(row=1, column=0)
encode_dropdown.grid(row=1, column=1)
encode_button.grid(row=1, column=2)
encode_binary_radio.grid(row=2, column=0, sticky="W")
encode_decimal_radio.grid(row=3, column=0, sticky="W")
encode_hex_radio.grid(row=4, column=0, sticky="W")

encode_output.grid(row=5, column=0, sticky="E")
scroll.grid(row=6, column=0, sticky="N")
encode_output_label.grid(row=5, column=0, sticky="W")
encode_secsed_radio.grid(row=2, column=1, sticky="W")
encode_secded_radio.grid(row=3, column=1, sticky="W")

# Decoder
decode_data = tk.Entry(width=60)

decode_button = tk.Button(win, text="Encode", command=encode)

decode_bits = []
for i in range(1, 33):
    decode_bits.append(i)
decode_bits_option = tk.StringVar(win)
decode_bits_option.set(decode_bits[0])
decode_dropdown = tk.OptionMenu(win, decode_bits_option, *decode_bits)

win.mainloop()