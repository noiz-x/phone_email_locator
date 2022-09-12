"""
Purpose:
    Locate Emails and Phone numbers
Target System:
    WINDOWS
Interface:
    Command-line
Functional Requirement:
    Locates phone numbers and emails in a text copied by the user and asks the
    user for the email or phone number he/she wants to copy
"""
import contextlib
import re
import pyperclip


print("Phone Number and Email Locator".center(200))
x = []
phonenum = re.compile(r"""(
    \+\d+\s\d+|
    \d\d\d-\d\d\d-\d\d\d\d|
    \d\d\d\d\d\d\d\d\d\d\d|
    \d\d\d\s\d\d\d\s\d\d\d\d|
    \+\d\d\d\d\d\d\d\d\d\d\d\d\d
    )""", re.VERBOSE)
email = re.compile(r"[a-zA-Z0-9]+@\w+\.\w+""")
text = pyperclip.waitForPaste()
p = phonenum.findall(text)
e = email.findall(text)
x.extend(p)
x.extend(e)
x.sort()
if x:
    print("The email and phone number found in the text are:")
    for index, i in enumerate(set(x)):
        print(f"{index + 1}. {i}")
    while True:
        try:
            print("Press \"n\" if you don't want to copy any of them.")
            if len(x) > 1:
                num = input("Which of the emails or phone numbers do you want: ").lower()
            else:
                num = input("Which of the email or phone number do you want: ").lower()
            with contextlib.suppress(Exception):
                v = int(num)
            if num == "none":
                print("OK!")
                break
            if v > 0:
                print(x[v - 1])
                pyperclip.copy(x[v - 1])
                print("It has  been copied to your clipboard")
                break
            print(f"The list starts from \"1\" not \"{num}\"")
        except (ValueError, TypeError) as errors:
            print(errors)
        except IndexError:
            if len(x) > 1:
                print(f"You have only {len(x)} terms in the list")
            else:
                print(f"You have only {len(x)} term in the list")

else:
    print("No phone numbers or emails found.")
    print("Sorry")
