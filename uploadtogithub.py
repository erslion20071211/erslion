import git
git.refresh(path="D:/misc/git/PortableGit/bin/git.exe")
import os

# 替換成你的 GitHub 帳號和專案資訊
repo_url = "https://github.com/erslion20071211/erslion.git"
local_path = r"D:/misc/Erslion Revival/非原始河東獅社團資料/河東獅社團資料/articles"  
# 請替換成你的資料夾路徑

# 檢查本地資料夾是否為 Git 儲存庫
try:
    repo = git.Repo(local_path)
except git.exc.InvalidGitRepositoryError:
    print("不是一個 Git 儲存庫，正在初始化...")
    repo = git.Repo.init(local_path)

# 檢查是否已連結遠端儲存庫
if "origin" not in repo.remotes:
    print("正在連結遠端儲存庫...")
    origin = repo.create_remote("origin", repo_url)
else:
    origin = repo.remotes.origin

# 加入所有變更
print("正在加入檔案...")
repo.git.add(all=True)

# 提交變更
print("正在提交變更...")
repo.index.commit("Initial commit using Python script")

# 推送到 GitHub
print("正在推送到 GitHub...")
origin.push()

print("上傳完成！")