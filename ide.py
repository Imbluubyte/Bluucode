import tkinter as tk
from tkinter import filedialog, messagebox
from interpreter import run_file

current_file = None


def new_file():
    global current_file

    current_file = None

    editor.delete("1.0", tk.END)

    root.title("Bluucode IDE - Untitled")


def open_file():
    global current_file

    filename = filedialog.askopenfilename(
        filetypes=[("Bluucode Files", "*.bluc")]
    )

    if not filename:
        return

    with open(filename, "r") as f:
        editor.delete("1.0", tk.END)
        editor.insert("1.0", f.read())

    current_file = filename

    root.title(f"Bluucode IDE - {filename}")


def save_file():
    global current_file

    if current_file is None:
        save_as()
        return

    with open(current_file, "w") as f:
        f.write(editor.get("1.0", tk.END))


def save_as():
    global current_file

    filename = filedialog.asksaveasfilename(
        defaultextension=".bluc",
        filetypes=[("Bluucode Files", "*.bluc")]
    )

    if not filename:
        return

    current_file = filename

    save_file()

    root.title(f"Bluucode IDE - {filename}")


def run_script():
    global current_file

    if current_file is None:
        messagebox.showerror(
            "Error",
            "Please save the file before running."
        )
        return

    save_file()

    try:
        result = run_file(current_file)

        output.config(state="normal")
        output.delete("1.0", tk.END)
        output.insert("1.0", result)
        output.config(state="disabled")

    except Exception as e:
        output.config(state="normal")
        output.delete("1.0", tk.END)
        output.insert("1.0", f"Error:\n{e}")
        output.config(state="disabled")

root = tk.Tk()
root.geometry("1000x700")
root.title("Bluucode IDE")


menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as)

menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)


editor = tk.Text(
    root,
    wrap="none",
    undo=True
)

editor.pack(
    fill="both",
    expand=True
)

run_button = tk.Button(
    root,
    text="Run",
    command=run_script
)

run_button.pack(fill="x")

output = tk.Text(
    root,
    height=10,
    state="disabled"
)

output.pack(fill="both")


root.bind("<F5>", lambda event: run_script())
root.bind("<Control-s>", lambda event: save_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-n>", lambda event: new_file())
root.mainloop()