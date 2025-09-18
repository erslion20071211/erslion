import os
import csv
import glob

# 設定檔案與資料夾路徑
csv_file = 'correctdot.csv' 
articles_folder = 'article'
images_folder_name = 'images'

# --- 步驟 1: 從 CSV 檔案建立網址對應表 ---
print("正在讀取 CSV 檔案並建立網址對應表...")
url_mapping = {}
try:
    # 嘗試使用 'utf-8-sig' 編碼，以處理可能存在的 BOM
    with open(csv_file, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        header = next(reader)  # 讀取標題列
    
    print(f"成功讀取 CSV 標題列：{header}")
    
    try:
        old_url_index = header.index('舊網址')
        new_path_index = header.index('新路徑')
    except ValueError:
        print("錯誤：CSV 檔案的欄位名稱不符，請確認包含 '舊網址' 和 '新路徑'。")
        input("按 Enter 鍵結束...")
        exit()

    with open(csv_file, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        next(reader)  # 跳過標題列
        for row in reader:
            if len(row) > max(old_url_index, new_path_index):
                old_url = row[old_url_index].strip()
                new_path = row[new_path_index].strip()
                relative_path = os.path.join('..', images_folder_name, new_path).replace(os.sep, '/')
                url_mapping[old_url] = relative_path
    
    print(f"成功從 {csv_file} 檔案中找到 {len(url_mapping)} 個圖片連結。")

except FileNotFoundError:
    print(f"錯誤：找不到檔案 {csv_file}。請確認檔案是否存在。")
    input("按 Enter 鍵結束...")
    exit()
except Exception as e:
    print(f"讀取 CSV 檔案時發生錯誤：{e}")
    input("按 Enter 鍵結束...")
    exit()

# --- 步驟 2: 批次修改 HTML 與 XML 檔案 ---
if url_mapping:
    files_to_process = glob.glob(os.path.join(articles_folder, '*.html'))
    files_to_process = glob.glob( 'tw-blog_2013-09-11_article.xml')
    files_to_process = glob.glob( '*.html')

    print(f'\n總共找到 {len(files_to_process)} 個檔案準備處理。')

    for file_path in files_to_process:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for old_url, new_url in url_mapping.items():
                content = content.replace(old_url, new_url)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f'成功處理檔案: {file_path}')
        except Exception as e:
            print(f'處理檔案時發生錯誤 {file_path}: {e}')

print('\n所有檔案處理完成。')
input("按 Enter 鍵結束...")