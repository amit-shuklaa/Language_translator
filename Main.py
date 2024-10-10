import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from deep_translator import GoogleTranslator

class LanguageConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Converter")
        self.root.geometry("700x600")  # Set window size
        self.root.configure(bg="#e9ecef")  # Set background color

        # Create a frame for input text
        self.input_frame = tk.Frame(root, bg="#e9ecef")
        self.input_frame.pack(pady=20)

        self.input_label = tk.Label(self.input_frame, text="Enter text:", bg="#e9ecef", font=("Arial", 16, "bold"), fg="#495057")
        self.input_label.pack()

        self.input_text = tk.Text(self.input_frame, height=8, width=60, font=("Courier New", 14), wrap=tk.WORD, bd=2, relief=tk.GROOVE, bg="#ffffff", fg="#212529")
        self.input_text.pack(pady=5)

        # Create a frame for output text
        self.output_frame = tk.Frame(root, bg="#e9ecef")
        self.output_frame.pack(pady=20)

        self.output_label = tk.Label(self.output_frame, text="Translated text:", bg="#e9ecef", font=("Arial", 16, "bold"), fg="#495057")
        self.output_label.pack()

        self.output_text = tk.Text(self.output_frame, height=8, width=60, font=("Courier New", 14), wrap=tk.WORD, bd=2, relief=tk.GROOVE, bg="#ffffff", fg="#212529")
        self.output_text.pack(pady=5)

        # Language selection
        self.language_frame = tk.Frame(root, bg="#e9ecef")
        self.language_frame.pack(pady=20)

        self.source_language_label = tk.Label(self.language_frame, text="Source Language:", bg="#e9ecef", font=("Arial", 14), fg="#495057")
        self.source_language_label.grid(row=0, column=0, padx=10, pady=5)

        self.source_language = ttk.Combobox(self.language_frame, values=[], font=("Arial", 12), state="readonly")
        self.source_language.set("auto")  # Default to automatic language detection
        self.source_language.grid(row=0, column=1, padx=10, pady=5)

        self.target_language_label = tk.Label(self.language_frame, text="Target Language:", bg="#e9ecef", font=("Arial", 14), fg="#495057")
        self.target_language_label.grid(row=1, column=0, padx=10, pady=5)

        self.target_language = ttk.Combobox(self.language_frame, values=[], font=("Arial", 12), state="readonly")
        self.target_language.grid(row=1, column=1, padx=10, pady=5)

        # Create the convert button with a stylish look
        self.convert_button = tk.Button(root, text="Convert", command=self.convert_language, font=("Arial", 16), bg="#007bff", fg="white", padx=20, pady=10, relief=tk.RAISED)
        self.convert_button.pack(pady=20)

        # Initialize languages
        self.initialize_languages()

    def initialize_languages(self):
        # Get supported languages using an instance of GoogleTranslator
        self.translator_instance = GoogleTranslator(source='auto', target='en')  # Initialize instance
        self.supported_languages = self.translator_instance.get_supported_languages()  # Get supported languages

        # Update combobox values
        self.source_language['values'] = self.supported_languages
        self.target_language['values'] = self.supported_languages

    def convert_language(self):
        source_text = self.input_text.get("1.0", tk.END).strip()
        src_lang = self.source_language.get()
        dest_lang = self.target_language.get()

        if not source_text:
            messagebox.showerror("Input Error", "Please enter text to translate.")
            return

        try:
            # Attempt to translate the text
            translated = GoogleTranslator(source=src_lang, target=dest_lang).translate(source_text)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, translated)
        except Exception as e:
            # Show a user-friendly error message
            print("Error:", str(e))  # Debug print to show the error in the console
            messagebox.showerror("Translation Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageConverter(root)
    root.mainloop()
