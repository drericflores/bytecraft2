"""Module: highlighter"""

from PyQt5.QtGui import QTextCursor, QTextCharFormat, QColor
from PyQt5.QtWidgets import QPlainTextEdit

def highlight_hex(view: QPlainTextEdit, start: int, length: int):
    """Highlight hex selection based on byte index."""
    cursor = view.textCursor()
    clear_highlights(view)

    # Estimate: 3 chars per hex byte ("xx "), plus 10 chars for offset and margin
    char_start = (start * 3) + 10
    char_len = length * 3

    cursor.setPosition(char_start)
    cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, char_len)

    fmt = QTextCharFormat()
    fmt.setBackground(QColor("yellow"))
    cursor.setCharFormat(fmt)

def highlight_text(view: QPlainTextEdit, start: int, length: int):
    """Highlight ASCII text based on byte offset."""
    cursor = view.textCursor()
    clear_highlights(view)

    cursor.setPosition(start)
    cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, length)

    fmt = QTextCharFormat()
    fmt.setBackground(QColor("lightgreen"))
    cursor.setCharFormat(fmt)

def clear_highlights(view: QPlainTextEdit):
    """Clear all text formatting in the given view."""
    cursor = view.textCursor()
    cursor.select(QTextCursor.Document)
    fmt = QTextCharFormat()
    cursor.setCharFormat(fmt)

