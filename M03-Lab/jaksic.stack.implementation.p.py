# Stack Notepad Exercise
# ----------------------
# You are building a simple command-line notepad using a stack.
# - Type a word to add it to your document (push onto the stack).
# - Type 'UNDO' to remove the last word you added(pop from the stack).
# - Type 'SHOW' to display the current document (all words in the stack).
#
# NOTE: You must use the methods from stack_implementation.py. Do not use a Python list directly.


from stack_implementation import push, pop, peek, is_empty, size

def add_word(word):
    """Add a word to the notepad (push onto stack)."""
    push(word)

def undo():
    """Undo the last added word (pop from stack)."""
    if not is_empty():
        removed = pop()
        print(f"Undid: {removed}")
    else:
        print("Nothing to undo!")

def show():
    """Display the current document (all words in stack)."""
    if is_empty():
        print("Document is empty.")
    else:
        # The stack might not have a direct way to iterate, so we'll pop into a temp list
        temp = []
        while not is_empty():
            temp.append(pop())
        # Reverse to show in the correct order (bottom to top of stack)
        document = " ".join(temp[::-1])
        print("Document:", document)
        # Push them back into the stack
        for word in temp[::-1]:
            push(word)

def main():
    """Main loop for the notepad."""
    print("Simple Stack Notepad")
    print("Type words to add them, 'UNDO' to undo, 'SHOW' to display, 'EXIT' to quit.\n")

    while True:
        command = input("Enter a word/command: ").strip()

        if command.upper() == "UNDO":
            undo()
        elif command.upper() == "SHOW":
            show()
        elif command.upper() == "EXIT":
            print("Goodbye!")
            break
        elif command == "":
            print("Please type something.")
        else:
            add_word(command)

if __name__ == '__main__':
    main()
