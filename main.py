import arrr
from pyscript import document
from tkinter import filedialog


def translate_english(event):
    # Receive input from HTML file
    input_text = document.querySelector("#english")
    english = input_text.value

   user_input = filedialog.askopenfile(initialdir='/', title='Select a Question File to Open', filetypes=(('Text File', '*.txt'), ('PDF File', '*.pdf'), ('DOCX File', '*.docx')))

    # Send the file path to the output
    output_div = document.querySelector('#output')
    output_div.innerText = user_input

    """
    # Try to open file
    with open(user_input, 'r') as input_file:
        # Read in contents of file
        # Send pirate version back to the HTML file
        output_div = document.querySelector("#output")
        output_div.innerText = input_file.read()
    """
