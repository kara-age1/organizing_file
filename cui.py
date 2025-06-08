import os
import shutil
import time
from pathlib import Path

# カテゴリ定義
CATEGORY_MAP = {
    "ドキュメント": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
    "画像": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "動画": [".mp4", ".mov", ".avi", ".mkv"],
    "音声": [".mp3", ".wav", ".m4a"],
    "アーカイブ": [".zip", ".rar", ".7z"],
    "アプリ": [".exe", ".msi"],
}

# フォルダパス（固定）
DOWNLOAD_DIR = Path(r"C:\Users\kara-\Downloads")
SORTED_BASE_DIR = Path(r"C:\Users\kara-\Documents") / "sorted_downloads"


def get_category(extension):
    for category, ext_list in CATEGORY_MAP.items():
        if extension.lower() in ext_list:
            return category
    return "その他"


def sort_files_with_move():
    for item in DOWNLOAD_DIR.iterdir():
        if item.is_file():
            category = get_category(item.suffix)
            dest_dir = SORTED_BASE_DIR / category
            dest_dir.mkdir(parents=True, exist_ok=True)
            dest_file = dest_dir / item.name

            # 同名ファイルの上書き防止
            counter = 1
            while dest_file.exists():
                dest_file = dest_dir / f"{item.stem} ({counter}){item.suffix}"
                counter += 1

            try:
                shutil.move(str(item), dest_file)
                print(f"✔ 移動: {item.name} → {dest_file}")
            except Exception as e:
                print(f"✘ 移動失敗: {item.name} → {e}")


if __name__ == "__main__":
    sort_files_with_move()
    time.sleep(10)
