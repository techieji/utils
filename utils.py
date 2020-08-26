from Bookmarker import shell as bshell
from PlanT import shell as pshell
from Schedule import shell as sshell

def shell():
    while True:
        cmd = input('> ')
        if cmd == "bookmark":
            print("Entering 'bookmark'...")
            bshell()
        elif cmd == "planner":
            print("Entering 'planner'...")
            pshell()
        elif cmd == "schedule":
            print("Entering 'schedule'...")
            sshell()
        elif cmd == "exit":
            return
        else:
            print(
                "Not a command. Choose from 'bookmark', 'planner', or 'schedule'."
            )

if __name__ == "__main__":
    shell()
