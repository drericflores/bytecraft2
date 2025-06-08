"""Module: theme_manager"""

from PyQt5.QtWidgets import QPlainTextEdit

def apply_theme(view: QPlainTextEdit, dark_mode: bool):
    """Apply a dark or light stylesheet to the given view."""
    if dark_mode:
        view.setStyleSheet("""
            QPlainTextEdit {
                background-color: #1e1e1e;
                color: #d4d4d4;
                font-family: Courier, monospace;
            }
        """)
    else:
        view.setStyleSheet("""
            QPlainTextEdit {
                background-color: white;
                color: black;
                font-family: Courier, monospace;
            }
        """)

