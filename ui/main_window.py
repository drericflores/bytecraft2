"""Module: main_window"""

from PyQt5.QtWidgets import (
    QMainWindow, QAction, QFileDialog, QPlainTextEdit, QSplitter,
    QMessageBox, QInputDialog
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog

from core.file_handler import load_file, save_file, save_as_text
from core.hex_formatter import format_hex_view, decode_ascii
from core.search_engine import perform_search, find_and_replace
from core.highlighter import highlight_hex, highlight_text, clear_highlights
from ui.theme_manager import apply_theme

class HexEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ByteCraft2")
        self.setGeometry(100, 100, 800, 600)

        # State
        self.file_data = bytearray()
        self.current_file_path = ""
        self.is_hex_mode = True
        self.dark_mode_enabled = False
        self.is_split_view_enabled = False

        # Split View Setup
        self.splitter = QSplitter(Qt.Horizontal, self)
        self.hex_view = QPlainTextEdit(self.splitter)
        self.text_view = QPlainTextEdit(self.splitter)
        self.text_view.setReadOnly(True)
        self.setCentralWidget(self.splitter)

        font = QFont("Courier", 10)
        self.hex_view.setFont(font)

        self.text_view.hide()

        self.hex_view.cursorPositionChanged.connect(self.on_hex_selection)
        self.text_view.cursorPositionChanged.connect(self.on_text_selection)

        self.create_menu()

    def create_menu(self):
        menu = self.menuBar()

        # File
        file_menu = menu.addMenu("File")
        file_menu.addAction("Open", self.open_file)
        file_menu.addAction("Save", self.save_file)
        file_menu.addAction("Save As", self.save_file_as)
        file_menu.addAction("Print", self.print_file)
        file_menu.addAction("Close", self.close_file)
        file_menu.addAction("Quit", self.close)

        # Edit
        edit_menu = menu.addMenu("Edit")
        edit_menu.addAction("Cut", self.hex_view.cut)
        edit_menu.addAction("Copy", self.hex_view.copy)
        edit_menu.addAction("Paste", self.hex_view.paste)
        edit_menu.addAction("Undo", self.hex_view.undo)
        edit_menu.addAction("Redo", self.hex_view.redo)
        edit_menu.addAction("Search", self.search_text)
        edit_menu.addAction("Search and Replace", self.search_replace)

        # View
        view_menu = menu.addMenu("View")
        view_menu.addAction("Toggle Hex/ASCII Mode", self.toggle_hex_ascii)
        view_menu.addAction("Light/Dark Mode", self.toggle_theme)
        view_menu.addAction("Hex/Text Mode", self.toggle_split_view)

        # Help
        help_menu = menu.addMenu("Help")
        help_menu.addAction("About", self.show_about)

    # File actions
    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open File")
        if path:
            self.current_file_path = path
            self.file_data = load_file(path)
            self.refresh_hex_view()

    def save_file(self):
        if self.current_file_path:
            save_file(self.current_file_path, self.file_data)
        else:
            self.save_file_as()

    def save_file_as(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save As")
        if path:
            if path.endswith('.txt'):
                save_as_text(path, self.hex_view.toPlainText())
            else:
                save_file(path, self.file_data)
            self.current_file_path = path

    def print_file(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            self.hex_view.print_(printer)

    def close_file(self):
        self.hex_view.clear()
        self.text_view.clear()
        self.file_data.clear()
        self.current_file_path = ""

    # Edit actions
    def search_text(self):
        term, ok = QInputDialog.getText(self, "Search", "Text or hex:")
        if ok and term:
            index = perform_search(self.file_data, term, self.is_hex_mode)
            if index != -1:
                cursor = self.hex_view.textCursor()
                cursor.setPosition(index)
                self.hex_view.setTextCursor(cursor)
            else:
                QMessageBox.information(self, "Search", "Not found.")

    def search_replace(self):
        find, ok1 = QInputDialog.getText(self, "Find", "Find what:")
        if ok1 and find:
            replace, ok2 = QInputDialog.getText(self, "Replace", "Replace with:")
            if ok2:
                self.file_data = find_and_replace(self.file_data, find, replace, self.is_hex_mode)
                self.refresh_hex_view()

    def toggle_hex_ascii(self):
        self.is_hex_mode = not self.is_hex_mode
        self.refresh_hex_view()

    def toggle_theme(self):
        self.dark_mode_enabled = not self.dark_mode_enabled
        apply_theme(self.hex_view, self.dark_mode_enabled)
        apply_theme(self.text_view, self.dark_mode_enabled)

    def toggle_split_view(self):
        self.is_split_view_enabled = not self.is_split_view_enabled
        self.text_view.setVisible(self.is_split_view_enabled)
        if self.is_split_view_enabled:
            self.refresh_text_view()

    def refresh_hex_view(self):
        content = format_hex_view(self.file_data) if self.is_hex_mode else decode_ascii(self.file_data)
        self.hex_view.setPlainText(content)
        if self.is_split_view_enabled:
            self.refresh_text_view()

    def refresh_text_view(self):
        self.text_view.setPlainText(decode_ascii(self.file_data))

    def on_text_selection(self):
        text = self.text_view.textCursor().selectedText()
        if text:
            index = self.file_data.find(text.encode())
            if index != -1:
                highlight_hex(self.hex_view, index, len(text))

    def on_hex_selection(self):
        selected = self.hex_view.textCursor().selectedText().replace(" ", "").strip()
        if selected:
            try:
                data = bytearray.fromhex(selected)
                index = self.file_data.find(data)
                if index != -1:
                    highlight_text(self.text_view, index, len(data))
            except ValueError:
                pass

    def show_about(self):
        QMessageBox.about(self, "About ByteCraft2", (
            "ByteCraft2\n"
            "By: Dr. Eric Oliver FLosre\n"
            "May 2025\n"
            "A modular hex editor\n\n"
            "Built with Python and PyQt5\n"
            "Creative Commons Zero (CC0 1.0 Universal)"
        ))

