import os
import shutil
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

CATEGORY_MAP = {
    "ドキュメント": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
    "画像": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "動画": [".mp4", ".mov", ".avi", ".mkv"],
    "音声": [".mp3", ".wav", ".m4a"],
    "アーカイブ": [".zip", ".rar", ".7z"],
    "アプリ": [".exe", ".msi"],
}

DOWNLOAD_DIR = Path(r"C:\Users\taiki\Downloads")
SORTED_BASE_DIR = Path(r"C:\Users\taiki\Documents") / "Sorted_Downloads"
"C:\Users\taiki\Documents - コピー"

def get_category(extension):
    for category, ext_list in CATEGORY_MAP.items():
        if extension.lower() in ext_list:
            return category
    return "その他"


def sort_files_with_move():
    sorted_count = 0
    for item in DOWNLOAD_DIR.iterdir():
        if item.is_file():
            category = get_category(item.suffix)
            dest_dir = SORTED_BASE_DIR / category
            dest_dir.mkdir(parents=True, exist_ok=True)
            dest_file = dest_dir / item.name

            counter = 1
            while dest_file.exists():
                dest_file = dest_dir / f"{item.stem} ({counter}){item.suffix}"
                counter += 1

            try:
                shutil.move(str(item), dest_file)
                sorted_count += 1
            except Exception as e:
                print(f"✘ 移動失敗: {item.name} → {e}")
    return sorted_count


def on_sort():
    count = sort_files_with_move()
    messagebox.showinfo("完了", f"{count} 個のファイルを分類して移動しました。")


def create_gui():
    root = tk.Tk()
    root.title("ファイル分類ツール")
    root.geometry("300x150")

    label = tk.Label(root, text="Downloadsフォルダを分類して移動します。")
    label.pack(pady=20)

    sort_button = tk.Button(root, text="分類を実行", command=on_sort)
    sort_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    create_gui()
