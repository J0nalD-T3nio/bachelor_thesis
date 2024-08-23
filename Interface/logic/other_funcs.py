"""
    File name: other_funcs.py
    
    Purpose: For other logic behind the gui
"""

from tkinter import filedialog

def open_file_dialog() -> str:
    """
        Summary:
            This is the event function for selecting
            a file

        Returns:
            str: The file path
    """
    file_path = filedialog.askopenfilename(
        title="Select a File", 
        filetypes=[("Text Files", "*.txt"),("PDF Files", "*.pdf"),("DOCX Files", "*.docx")]
    )
    print(f"Chosen file: {file_path}")
    return file_path
