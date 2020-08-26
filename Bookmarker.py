import webbrowser
import pickle
from PlanT import reset, enter, parseInp, exit

def shell():
    data = enter(".markrc")
    while True:
        inp = parseInp(input("> "))
        try:
            cmd = inp[0]
        except IndexError:
            continue
            
        if cmd in ["add", "update"]:
            data[inp[1]] = inp[2]
        elif cmd == "open":
            webbrowser.open(data[inp[1]])
            print(data[inp[1]])
        elif cmd == "remove":
            del data[inp[1]]
        elif cmd == "exit":
            exit(data, ".markrc")
