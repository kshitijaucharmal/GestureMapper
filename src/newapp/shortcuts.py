import pyautogui as pag
import string

# whitelist = string.ascii_letters + string.digits +""
bad_chars = [";", ",", ":", "`", "~", "@", "#", "%", "^", "&", "*", "-", "_", " "]


def run_shortcut(str1, str2, str3):
    if str3 == "":
        pag.keyDown(str1)
        pag.keyDown(str2)
        pag.keyUp(str2)
        pag.keyUp(str1)
    else:
        """
        pag.keyDown(str1)
        pag.keyDown(str2)
        pag.keyDown(str3)
        pag.keyUp(str3)
        pag.keyUp(str2)
        pag.keyUp(str1)
        """
        pag.hotkey(str1, str2, str3)


def remove_symbol(str, bad_chars):
    new_s = "".join(map(lambda x: x if x not in bad_chars else "", str))
    return new_s


def get_word(str):
    new_str = str.split("+")
    return new_str


"""
s = "ctrl+right"
new_s = remove_symbol(s,bad_chars)
s2 = get_word(new_s)
print(s2)
run_shortcut(s2[0],s2[1])
"""
