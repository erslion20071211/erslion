import os
import shutil
import traceback

def copy_dotfiles_to_a_dot(start_dir="images"):
    total_copied = 0
    error_files = []
    skipped_files = []

    print(f"Start copying .開頭檔案為 a.開頭。搜尋範圍：{start_dir}\n")

    for root, dirs, files in os.walk(start_dir):
        for filename in files:
            if filename.startswith(".") and len(filename) > 1:
                old_path = os.path.join(root, filename)
                new_filename = "a" + filename
                new_path = os.path.join(root, new_filename)
                try:
                    if os.path.exists(new_path):
                        print(f"[SKIP] 目標檔案已存在：{new_path}")
                        skipped_files.append(new_path)
                        continue
                    shutil.copy2(old_path, new_path)
                    print(f"[COPY] 已複製：{old_path} -> {new_path}")
                    total_copied += 1
                except Exception as e:
                    print(f"[ERROR] 複製失敗：{old_path} -> {new_path}")
                    print(f"        原因：{e}")
                    error_files.append((old_path, new_path, str(e)))
                    traceback.print_exc()

    print("\n------ 執行結果 ------")
    print(f"成功複製檔案數：{total_copied}")
    if skipped_files:
        print(f"\n[提示] 以下 a.開頭檔案已存在（未複製）:")
        for path in skipped_files:
            print("   ", path)
    if error_files:
        print(f"\n[錯誤] 以下檔案處理時發生錯誤：")
        for (old_path, new_path, error_msg) in error_files:
            print(f"   檔案：{old_path} -> {new_path}\n        {error_msg}")
    if not error_files:
        print("\n[完成] 全部步驟執行成功！")
    else:
        print("\n[注意] 有檔案處理失敗，請參考上方訊息！")

if __name__ == "__main__":
    copy_dotfiles_to_a_dot("images")