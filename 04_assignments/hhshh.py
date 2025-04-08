import curses
import re

def check_password_strength(password):
    length_score = len(password) >= 8
    upper_case = bool(re.search(r'[A-Z]', password))
    lower_case = bool(re.search(r'[a-z]', password))
    digit = bool(re.search(r'[0-9]', password))
    special_char = bool(re.search(r'[^A-Za-z0-9]', password))

    strength_score = sum([length_score, upper_case, lower_case, digit, special_char])
    return strength_score, length_score, upper_case, lower_case, digit, special_char

def draw_strength_meter(stdscr, password):
    strength_score, length_score, upper_case, lower_case, digit, special_char = check_password_strength(password)
    stdscr.clear()

    stdscr.addstr(0, 0, "Password: " + password)

    # Determine the strength and color
    if strength_score == 0:
        strength_message = "Very Weak"
        color = curses.color_pair(1)  # Red
    elif strength_score == 1:
        strength_message = "Weak"
        color = curses.color_pair(2)  # Yellow
    elif strength_score == 2:
        strength_message = "Fair"
        color = curses.color_pair(3)  # Blue
    elif strength_score == 3:
        strength_message = "Good"
        color = curses.color_pair(4)  # Cyan
    elif strength_score == 4:
        strength_message = "Strong"
        color = curses.color_pair(5)  # Green
    else:
        strength_message = "Very Strong"
        color = curses.color_pair(6)  # Green

    # Draw the strength message and meter
    stdscr.addstr(2, 0, f"Strength: {strength_message}", color)
    stdscr.addstr(3, 0, f"Strength Meter: {'=' * strength_score}{' ' * (5 - strength_score)}", color)

    # Display suggestions
    stdscr.addstr(5, 0, "Suggestions:")

    if not length_score:
        stdscr.addstr(6, 0, "- Password is too short, add at least 8 characters.")
    if not upper_case:
        stdscr.addstr(7, 0, "- Add at least one uppercase letter.")
    if not lower_case:
        stdscr.addstr(8, 0, "- Add at least one lowercase letter.")
    if not digit:
        stdscr.addstr(9, 0, "- Add at least one digit.")
    if not special_char:
        stdscr.addstr(10, 0, "- Add at least one special character (e.g., !@#$%^&*).")

    stdscr.refresh()

def main(stdscr):
    # Initialize color pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_GREEN, curses.COLOR_BLACK)

    password = ""
    while True:
        key = stdscr.getch()

        if key == 10:  # Enter key to finish
            break
        elif key == 127:  # Backspace
            password = password[:-1]
        else:
            password += chr(key)

        draw_strength_meter(stdscr, password)

if __name__ == "__main__":
    curses.wrapper(main)
