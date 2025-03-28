import arrr
from pyscript import document


def translate_english(event):
    # Receive input from HTML file
    input_text = document.querySelector("#english")
    english = input_text.value

    # Run a Test Print Statement
    print('* This is a test print statement')
    print('* Input:', english)

    # Send pirate version back to the HTML file
    output_div = document.querySelector("#output")
    output_div.innerText = arrr.translate(english)
