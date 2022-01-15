from .classes.Buttons import SelectionButton, RotateButton, SubmitButton
from .classes.ShipsText import ShipsText
from .constants import FOUR_BUTTON, THREE_BUTTON, TWO_BUTTON, ONE_BUTTON, FOUR_HIGHLIGHT, THREE_HIGHLIGHT, TWO_HIGHLIGHT, ONE_HIGHLIGHT, ROTATE_BUTTON_V, ROTATE_BUTTON_H, SUBMIT_BUTTON


def create_ship_buttons(texts):
    '''
    Creates four buttons for four different types of ships.\n
    Position of each button is based on position of the text accompaning that button.
    '''
    four_button = SelectionButton(FOUR_BUTTON, texts[0].x + 100, texts[0].y, False, FOUR_HIGHLIGHT, 4)
    three_button = SelectionButton(THREE_BUTTON, texts[1].x + 100, texts[1].y, False, THREE_HIGHLIGHT, 3)
    two_button = SelectionButton(TWO_BUTTON, texts[2].x + 100, texts[2].y, False, TWO_HIGHLIGHT, 2)
    one_button = SelectionButton(ONE_BUTTON, texts[3].x + 100, texts[3].y, False, ONE_HIGHLIGHT, 1)
    return four_button, three_button, two_button, one_button


def create_rotate_button(board):
    x = board.board_pos[0]
    y = board.board_pos[1]
    rotate_button = RotateButton(ROTATE_BUTTON_H, x + 250, y + 400, False, ROTATE_BUTTON_V)
    return rotate_button


def create_submit_button(board):
    x = board.board_pos[0]
    y = board.board_pos[1]
    submit_button = SubmitButton(SUBMIT_BUTTON, x + 50, y + 400, False, None)
    return submit_button


def create_text(board):
    '''
    Creates text corresponding to the buttons.\n
    Posttion of each text is based on position of the board.
    '''
    x = board.board_pos[0]
    y = board.board_pos[1]
    text4 = ShipsText(1, x + 500, y)
    text3 = ShipsText(2, x + 500, y + 100)
    text2 = ShipsText(3, x + 500, y + 200)
    text1 = ShipsText(4, x + 500, y + 300)
    return text4, text3, text2, text1