
def line(queue):
    if not queue:
        print("The line is currently empty.")
    else:
        line_message = "The line is currently: " + " ".join(f"{i + 1}. {name}" for i, name in enumerate(queue))
        print(line_message)

def take_a_number(queue, name):
    queue.append(name)
    print(f"Welcome, {name}. You are number {len(queue)} in line.")

def now_serving(queue):
    if not queue:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {queue.pop(0)}.")
