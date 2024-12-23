import tkinter
from tkinter import *
import random

questions = [
    "How many Keywords are there in C Programming language ?",
    "Which of the following functions takes A console Input in Python ?",
    "Which of the following is the capital of India ?",
    "Which of The Following is must to Execute a Python Code ?",
    "The Taj Mahal is located in  ?",
    "The append Method adds value to the list at the  ?",
    "Which of the following is not a costal city of india ?",
    "Which of The following is executed in browser(client side) ?",
    "Which of the following keyword is used to create a function in Python ?",
    "To Declare a Global variable in python we use the keyword ?",
]

answers_choice = [
    ["23","32","33","43",],
    ["get()","input()","gets()","scan()",],
    ["Mumbai","Delhi","Chennai","Lucknow",],
    ["TURBO C","Py Interpreter","Notepad","IDE",],
    ["Patna","Delhi","Benaras","Agra",],
    ["custom location","end","center","beginning",],
    ["Bengluru","Kochin","Mumbai","vishakhapatnam",],
    ["perl","css","python","java",],
    ["function","void","fun","def",],
    ["all","var","let","global",],
]

indexes = []
def gen():
    global indexes
    while(len(indexes) < 5):
        x = random.randint(0, 9)
        if x in indexes:
            continue
        else:
            indexes.append(x)
    print(indexes)

def startQuiz():
    # Add a scrollable frame
    canvas = Canvas(root)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    scrollable_frame = Frame(canvas)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Generate unique indexes for random questions
    gen()

    # Create individual IntVar for each question
    variables = [IntVar(value=-1) for _ in range(len(indexes))]

    for idx, question_index in enumerate(indexes):
        # Display question
        lblQuestion = Label(
            scrollable_frame,
            text=questions[question_index],
            font=("Comic sans MS", 20),
            wraplength=800,
            justify="center",
        )
        lblQuestion.pack(pady=(10, 20))

        # Display options for the question
        for option_index, option in enumerate(answers_choice[question_index]):
            Radiobutton(
                scrollable_frame,
                text=option,
                font=("Comic sans MS", 16),
                value=option_index,
                variable=variables[idx],  # Use a unique IntVar for each question
            ).pack(anchor="w")

    # Add a submit button at the end
    Button(
        scrollable_frame,
        text="Submit",
        font=("Comic sans MS", 16),
        command=lambda: print([var.get() for var in variables]),  # Debugging output
    ).pack(pady=20)


def bt1Ispressed():
    labelText.destroy()
    bt1.destroy()
    start.destroy()
    startQuiz()


root = tkinter.Tk()
root.title("QUIZEE")
root.geometry("800x600")

labelText = Label(
    root,
    text="QUIZEE",
    font=("Comic sans MS", 32, "bold")
)
labelText.pack(pady=(0, 50))

start = Entry(root, width=30)
start.pack()
start.insert(0, "Enter your name")

bt1 = Button(root, text="ENTER", command=bt1Ispressed)
bt1.pack(pady=(20, 10))

root.mainloop()