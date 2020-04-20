import tkinter as tk
from Encoder import encoder
from Decoder import decoder


def encode():
    output, output_steps = encoder(encode_data.get(), encode_radio.get(), encode_secded.get(), int(encode_bits_option.get()))
    output_text.set(output)
    encode_explanation = ""
    for i in output_steps:
        encode_explanation = encode_explanation + i
    tex.delete('1.0', tk.END)
    tex.insert(tk.END, encode_explanation)
    tex.see(tk.END)

def decode():
    output = decoder(decode_data.get(), decode_radio.get(), decode_secded.get(), int(decode_bits_option.get()))
    output_text_decoder.set(output)

def step():
    count_step = count_step_var.get()
    output, output_steps = encoder(encode_data.get(), encode_radio.get(), encode_secded.get(),
                                   int(encode_bits_option.get()))
    encode_explanation = ""
    counter = 0
    for i in output_steps:
        if counter <= count_step:
            encode_explanation = encode_explanation + i
        counter += 1
    tex.delete('1.0', tk.END)
    tex.insert(tk.END, encode_explanation)
    tex.see(tk.END)
    count_step_var.set(count_step + 1)

def reset():
    tex.delete('1.0', tk.END)
    count_step_var.set(0)





win = tk.Tk()
win.title("Hamming Encoder/Decoder")
win.geometry("490x500")
win.resizable(width=False, height=False)


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
encode_output = tk.Entry(win, textvariable=output_text, state='readonly', width=40)
scroll = tk.Scrollbar(win, orient='horizontal', command=encode_output.xview)
encode_output.config(xscrollcommand=scroll.set)
encode_output_label = tk.Label(win)
encode_output_label["text"] = "Encoder Output: "

texLabel = tk.Label(win)
texLabel["text"] = "Explanation: "

tex = tk.Text(win, width=50, height=10, state='normal', wrap=tk.NONE, bg=win.cget("background"))
scroll_tex = tk.Scrollbar(win, orient='horizontal', command=tex.xview)

count_step_var = tk.IntVar(0)
step_button = tk.Button(win, text="Step", command=step)

reset_button = tk.Button(win, text="Reset", command=reset)


label_encoder.grid(row=0, column=0, sticky="W")
encode_data.grid(row=1, column=0)
encode_dropdown.grid(row=1, column=1)
encode_button.grid(row=1, column=2, sticky="E")
step_button.grid(row=2, column=2, sticky="E")
reset_button.grid(row=3, column=2, sticky="E")
encode_binary_radio.grid(row=2, column=0, sticky="W")
encode_decimal_radio.grid(row=3, column=0, sticky="W")
encode_hex_radio.grid(row=4, column=0, sticky="W")
texLabel.grid(row=7, column=0, sticky="W")
tex.grid(row=7, column=0, columnspan=3, sticky="E")
scroll_tex.grid(row=8, column=1)
encode_output.grid(row=5, column=0, sticky="E", columnspan=3)
scroll.grid(row=6, column=1, sticky="N")
encode_output_label.grid(row=5, column=0, sticky="W")
encode_secsed_radio.grid(row=2, column=1, sticky="W")
encode_secded_radio.grid(row=3, column=1, sticky="W")

# Decoder
decode_data = tk.Entry(width=60)

decode_button = tk.Button(win, text="Decode", command=decode)

decode_bits = []
for i in range(1, 33):
    decode_bits.append(i)
decode_bits_option = tk.StringVar(win)
decode_bits_option.set(decode_bits[0])
decode_dropdown = tk.OptionMenu(win, decode_bits_option, *decode_bits)

decode_radio = tk.StringVar()
decode_binary_radio = tk.Radiobutton(win, text="Binary", variable=decode_radio, value="binary")
decode_decimal_radio = tk.Radiobutton(win, text="Decimal", variable=decode_radio, value="decimal")
decode_hex_radio = tk.Radiobutton(win, text="Hexadecimal", variable=decode_radio, value="hex")
decode_radio.set("binary")

decode_secded = tk.BooleanVar()
decode_secsed_radio = tk.Radiobutton(win, text="SECSED", variable=decode_secded, value=False)
decode_secded_radio = tk.Radiobutton(win, text="SECDED", variable=decode_secded, value=True)
decode_secded.set(False)

label_decoder = tk.Label(win)
label_decoder["text"] = "Decoder"

output_text_decoder = tk.StringVar()
decoder_output = tk.Entry(win, state='readonly', textvariable=output_text_decoder, width=40)
scroll_decoder = tk.Scrollbar(win, orient='horizontal', command=decoder_output.xview)
decoder_output.config(xscrollcommand=scroll.set)
decoder_output_label = tk.Label(win)
decoder_output_label["text"] = "Decoder Output: "

label_decoder.grid(row=8, column=0, sticky="W")
decode_data.grid(row=9, column=0)
decode_dropdown.grid(row=9, column=1)
decode_button.grid(row=9, column=2)
decode_binary_radio.grid(row=10, column=0, sticky="W")
decode_decimal_radio.grid(row=11, column=0, sticky="W")
decode_hex_radio.grid(row=12, column=0, sticky="W")

decoder_output.grid(row=13, column=0, sticky="E", columnspan=3)
scroll_decoder.grid(row=14, column=1, sticky="N")
decoder_output_label.grid(row=13, column=0, sticky="W")
decode_secsed_radio.grid(row=10, column=1, sticky="W")
decode_secded_radio.grid(row=11, column=1, sticky="W")

win.mainloop()