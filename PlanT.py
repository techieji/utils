"""
A simple terminal based planner app. Stores data in a .planrc file. Does not
ever delete data, make sure to reset it every now and then.
"""

import pickle
import datetime

def reset(filename=".planrc"):
    with open(filename, "bw") as f:
        pickle.dump({}, f)

def enter(filename='.planrc'):
    with open(filename, "rb") as f:
        return pickle.load(f)
    
def parseDate(s, style='month/day/year'):
    if s == 'today':
        return datetime.date.today()
    elif s[0:2] == 't+':
        return datetime.date.today() + datetime.timedelta(int(s[2:]))
    else:
        s = map(int, s.split('/'))
        style = style.split('/')
        return datetime.date(**dict(zip(style, s)))

def doMAction(data, date, action, *args):
    # Mutating Action
    if date not in data.keys():
        data[date] = {"rem": [], "done": []}

    if action == 'new':
        data[date]["rem"].append(args[0])
    elif action == 'done':
        for x in data[date]["rem"]:
            if x == args[0]:
                data[date]["done"].append(x)
                data[date]["rem"].remove(x)
    elif action == 'delete':
        for x in data[date]["rem"]:
            if x == args[0]:
                data[date]["rem"].remove(x)

        for x in data[date]["done"]:
            if x == args[0]:
                data[date]["done"].remove(x)
    elif action == 'revive':
        for x in data[date]["done"]:
            if x == args[0]:
                data[date]["rem"].append(x)
                data[date]["done"].remove(x)

def doIAction(data, date, action, *args):
    # IO Action
    try:
        if action == "seeRem":
            print(
                " * " + "\n * ".join(data[date]["rem"])
            )
        elif action == "seeDone":
            print(
                " * " + "\n * ".join(data[date]["done"])
            )
        elif action == "seeAll":
            print("=== Reminders ===")
            doIAction(data, date, "seeRem", *args)
            print("=== Finished ====")
            doIAction(data, date, "seeDone", *args)
    except KeyError:
        print("Date has no information attached to it.")

def exit(data, filename='.planrc'):
    with open(filename, "bw") as f:
        pickle.dump(data, f)

### Shell

def parseInp(text):
    elements = []
    acc = ""
    level = False
    for x in text + " ":
        if x == '"':
            level = not level
        elif x == " " and not level:
            elements.append(acc)
            acc = ""
        else:
            acc += x
    return elements

def shell():
    data = enter()
    while True:
        inp = parseInp(input("> "))
        try:
            cmd = inp[0]
            date = parseDate(inp[1])
        except:
            if cmd == 'exit':
                exit(data)
                return
            elif cmd == 'data':
                print(data)
            continue
        if cmd in ['new', 'done', 'delete']:
            # print("Mutating...")
            doMAction(data, date, cmd, *inp[2:])
        elif cmd in ['seeRem', 'seeDone', 'seeAll']:
            # print("Printing...")
            doIAction(data, date, cmd, *inp[2:])
        else:
            print(f"Unrecognized command '{cmd}'")
