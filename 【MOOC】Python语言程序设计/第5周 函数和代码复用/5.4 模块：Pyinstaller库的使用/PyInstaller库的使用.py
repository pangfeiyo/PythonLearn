# 将.py文件转换成可直接执行文件，不需要py环境
# PyInstaller库是第三方库
# 官方网站：http://www.pyinstaller.org

# 路径中不能出现中文，包括文件名

'''
-h              查看帮助
--clean         清理打包过程中生成的临时文件
-D,--onedir     默认值，生成dist文件夹（尽量不要使用）
-F,--onefile    在dist文件夹中只生成独立的打包文件
-i <图标文件名.ico>   指定打包程序使用的图标(icon)文件
                      pyinstaller -i curve.ico -F SevenDigitsDrawV2.py
'''