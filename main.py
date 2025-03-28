import arrr
from pyscript import document


def translate_english(event):
    # Receive input from HTML file
    input_text = document.querySelector("#english")
    english = input_text.value

    # Run a Test Print Statement
    # -> Prints don't display on HTML page
    print('* This is a test print statement')
    print('* Input:', english)

    # Try to open file
    with open(english, 'r') as input_file:
        # Read in contents of file
        # Send pirate version back to the HTML file
        output_div = document.querySelector("#output")
        output_div.innerText = input_file.read()
