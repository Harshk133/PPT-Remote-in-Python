# Hello world Programmer
# Harsh Kale!
from flask import Flask, render_template
from pyvirtualdisplay import Display
import pyautogui


app = Flask(__name__, template_folder='templates', static_folder='static')

# Create a virtual display
display = Display(visible=0, size=(800, 600))
display.start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/change_slide_next', methods=['POST'])
def change_slide_next():
    try:
        pyautogui.press('right')
        # pyautogui.press('left')
        # pyautogui.hotkey('winleft', 'r')
        return 'Slide changed successfully!'
    except Exception as e:
        return f'Error changing slide: {str(e)}'

@app.route('/change_slide_previous', methods=['POST'])
def change_slide_previous():
    try:
        pyautogui.press('left')
        # pyautogui.press('left')
        # pyautogui.hotkey('winleft', 'r')
        return 'Slide changed successfully!'
    except Exception as e:
        return f'Error changing slide: {str(e)}'

@app.route('/start', methods=['POST'])
def start():
    try:
        pyautogui.press('f5')
        # Simulate Alt + V
        # pyautogui.press('left')
        # pyautogui.hotkey('winleft', 'r')
        return 'Slide changed successfully!'
    except Exception as e:
        return f'Error changing slide: {str(e)}'


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)


