import glob
import os

# 匹配当前目录及其子目录中的所有 .obj 和 .lib 文件
files_to_remove = glob.glob('**/*.obj', recursive=True) + glob.glob('**/*.lib', recursive=True)

# 删除匹配到的文件
for file in files_to_remove:
    try:
        os.remove(file)
        print(f"Removed: {file}")
    except OSError as e:
        print(f"Error: {file} : {e.strerror}")

print("Cleanup completed.")



'''
chcp 65001
$env:SCRIPT_AES256_ENCRYPTION_KEY="fb496c0ac198a46d0a8852e38c9ee0c6f32e5f0069bec566357ec289671816e0"

scons platform=windows
scons platform=windows target=template_release
'''
