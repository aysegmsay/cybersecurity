import file_object
import tkinter as tk
from tkinter import filedialog


class FileAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Analyzer")
        self.selected_file_path = ""
        self.root.configure(bg="#FFC0CB")


        # Başlık
        title_label = tk.Label(root, text="File Analyzer", font=("Arial", 24), bg="#FFC0CB", fg="black")
        title_label.grid(row=0, column=0, pady=50, columnspan=20)

        self.file_path_label = tk.Label(root, text="Selected File:", bg="#FFC0CB", fg="black")
        self.file_path_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Düğmeleri ortada konumlandırma
        self.browse_button = tk.Button(root, text="SELECT", command=self.browse_file, bg="#3498db", fg="white",
                                       height=2, width=20)
        self.browse_button.grid(row=2, column=0, pady=20, padx=10, sticky='e')

        self.analyze_button = tk.Button(root, text="SUBMIT", command=self.run_analysis, bg="#3498db", fg="white",
                                        height=2, width=20)
        self.analyze_button.grid(row=2, column=1, pady=20, padx=10, sticky='w')

        # Ortadaki sütunlara gizli bir 3. sütun ekleyerek başlıkları ortalamak için
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.selected_file_path = file_path
            self.file_path_label.config(text=f"Selected File: {file_path}")

    def run_analysis(self):
        obj = file_object.FileClass(self.selected_file_path)
        result = obj.analyze_file()
        print(obj.file_path, obj.file_sha256)
        print(obj.get_signature())
        result_window = tk.Toplevel(self.root)
        result_label = tk.Label(result_window, text=result, wraplength=500)
        result_label.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = FileAnalyzerApp(root)
    root.mainloop()

