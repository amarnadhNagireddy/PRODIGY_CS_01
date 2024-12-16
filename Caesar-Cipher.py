import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def encrypt(shiftKey, msg):
    res = ""
    for char in msg:
        if char.isupper():
            res += chr((ord(char) + shiftKey - 65) % 26 + 65)
        elif char.islower():
            res += chr((ord(char) + shiftKey - 97) % 26 + 97)
        else:
            res += char  
    return res

def decrypt(shiftKey, msg):
    res = ""
    for char in msg:
        if char.isupper():
            res += chr((ord(char) - 65 - shiftKey) % 26 + 65)
        elif char.islower():
            res += chr((ord(char) - 97 - shiftKey) % 26 + 97)
        else:
            res += char  
    return res

# GUI PART
def create_gui():
    def process_cipher():
        shiftKey = int(shift_key_dropdown.get())
        msg = input_text.get("1.0", tk.END).strip()
        if not msg:
            messagebox.showerror("Input Error", "Please enter text to encrypt or decrypt.")
            return
        if action_dropdown.get() == "Encrypt":
            result = encrypt(shiftKey, msg)
            result_label.config(text="Ciphertext:")
        elif action_dropdown.get() == "Decrypt":
            result = decrypt(shiftKey, msg)
            result_label.config(text="Plaintext:")
        else:
            messagebox.showerror("Action Error", "Please select a valid action (Encrypt/Decrypt).")
            return
        result_text.delete("1.0", tk.END) 
        result_text.insert(tk.END, result) 

    root = tk.Tk()
    root.title("Caesar Cipher")
    root.geometry("600x500")
    root.config(bg="#f0fff0")
    title_label = tk.Label(root, text="Caesar Cipher Tool", font=("Helvetica", 20, "bold"), fg="#4682b4", bg="#f0f8ff")
    title_label.pack(pady=10, fill=tk.X)
    action_label = tk.Label(root, text="Select Action:", font=("Helvetica", 12), bg="#f0f8ff")
    action_label.pack(pady=2)
    action_dropdown = ttk.Combobox(root, values=["Encrypt", "Decrypt"], state="readonly", font=("Helvetica", 12))
    action_dropdown.pack(pady=1)
    action_dropdown.set("Encrypt")
    shift_key_label = tk.Label(root, text="Select Shift Key (1-25):", font=("Helvetica", 12), bg="#f0f8ff")
    shift_key_label.pack(pady=1)
    shift_key_dropdown = ttk.Combobox(root, values=list(range(1, 26)), state="readonly", font=("Helvetica", 12))
    shift_key_dropdown.pack(pady=1)
    shift_key_dropdown.set(1)
    input_label = tk.Label(root, text="Enter Text:", font=("Helvetica", 12), bg="#f0f8ff")
    input_label.pack(padx=10,pady=5)

    input_frame = tk.Frame(root)
    input_frame.pack(padx=10,pady=5)

    input_scrollbar = tk.Scrollbar(input_frame, orient=tk.VERTICAL)
    input_text = tk.Text(input_frame, height=5, font=("Helvetica", 12), wrap=tk.WORD, yscrollcommand=input_scrollbar.set)
    input_scrollbar.config(command=input_text.yview)
    input_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    input_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    process_button = tk.Button(root, text="Process", font=("Helvetica", 14, "bold"), bg="#4682b4", fg="white", command=process_cipher)
    process_button.pack(pady=10)
    result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f8ff")
    result_label.pack(pady=5,padx=10)
    result_frame = tk.Frame(root)
    result_frame.pack(pady=5,padx=10)
    result_scrollbar = tk.Scrollbar(result_frame, orient=tk.VERTICAL)
    result_text = tk.Text(result_frame, height=5, font=("Helvetica", 12), wrap=tk.WORD, yscrollcommand=result_scrollbar.set)
    result_scrollbar.config(command=result_text.yview)
    result_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
