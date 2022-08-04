from tkinter import Tk
from tkinter import StringVar
from tkinter import filedialog
from tkinter import Label
from tkinter import Button
from tkinter import messagebox
from os import path
from os import listdir
from winreg import OpenKey
from winreg import QueryValueEx
from winreg import HKEY_CURRENT_USER


# 创建 CUI 页面
def get_gui():
    global pcl_dir_text, root

    root = Tk()
    root.title("生成VS中PCL工程的设置文件")
    root_width = 400
    root_height = 120
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry("{}x{}+{}+{}".format(root_width, root_height, int((screen_width - 500) / 2), int((screen_height - 300) / 3)))
    root.resizable(False, False)

    pcl_dir_text = StringVar()
    Label(text="请选择PCL安装根目录：", font=("微软雅黑", 12)).place(x=10, y=10)
    Label(text="PCL根目录：", font=("微软雅黑", 10)).place(x=10, y=50)
    Label(textvariable=pcl_dir_text, font=("微软雅黑", 10)).place(x=95, y=50)

    # 打开系统文件夹选择器
    def choose_dir():
        file_path = filedialog.askdirectory()
        pcl_dir_text.set(file_path)

    Button(root, text="选择目录", font=("微软雅黑", 8), bg="orange", command=choose_dir).place(x=180, y=11)
    Button(root, text="生成文件", font=("微软雅黑", 9), width=30, fg="white", bg="blue", command=check_info).place(x=90, y=80)

    root.mainloop()


# 检查输入的信息是否为空
def check_info() -> str:
    p = pcl_dir_text.get()
    if (p is None) or (p == "") or (len(p) == 0):
        messagebox.showerror("Error", "请选择PCL根目录!")
    else:
        root.quit()
        return p


# 获取用户的桌面路径
def get_desktop() -> str:
    key = OpenKey(HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return QueryValueEx(key, "Desktop")[0]


# 存储包含目录
def save_contains(pcl_dir: str, desk: str):
    res = "" \
          + pcl_dir + "\\3rdParty\\FLANN\\include" + ";" \
          + pcl_dir + "\\3rdParty\\Qhull\\include\\" + ";" \
          + pcl_dir + "\\3rdParty\\OpenNI2\\Include" + ";" \
          + pcl_dir + "\\3rdParty\\VTK\\include\\" + listdir(pcl_dir + "\\3rdParty\\VTK\\include\\")[0] + ";" \
          + pcl_dir + "\\3rdParty\\Eigen\\" + listdir(pcl_dir + "\\3rdParty\\Eigen\\")[0] + ";" \
          + pcl_dir + "\\include\\" + listdir(pcl_dir + "\\include\\")[0] + ";" \
          + pcl_dir + "\\3rdParty\\Boost\\include\\" + listdir(pcl_dir + "\\3rdParty\\Boost\\include\\")[0] + ";"
    with open(desk + "\\包含目录.txt", "w", encoding="utf8") as f:
        f.write(res)


# 存储库目录
def save_ku(pcl_dir: str, desk: str):
    res = "" \
          + pcl_dir + "\\3rdParty\\Boost\\lib" + ";" \
          + pcl_dir + "\\3rdParty\\FLANN\\lib" + ";" \
          + pcl_dir + "\\3rdParty\\OpenNI2\\Lib" + ";" \
          + pcl_dir + "\\3rdParty\\Qhull\\lib" + ";" \
          + pcl_dir + "\\3rdParty\\VTK\\lib" + ";" \
          + pcl_dir + "\\lib" + ";"
    with open(desk + "\\库目录.txt", "w", encoding="utf8") as f:
        f.write(res)
    return res


# 存储lib目录
def save_libs(lib_list: list, desk: str):
    debug, release = "", ""
    for pa in lib_list:
        for item in listdir(pa):
            # debug 版本:
            # 文件名以 _debug.lib 结尾
            # 文件名含有 -mt-gd
            # 文件名以 以 -gd.lib 结尾
            # 文件名以 _d.lib 结尾
            # 文件名以 d.lib 结尾
            # 文件名以 y.lib 结尾
            if (item.endswith("debug.lib") or item.endswith("-gd.lib") or item.endswith("_d.lib")
                    or item.endswith("d.lib") or item.endswith("y.lib") or ("mt-gd" in item)):
                debug += item + ";"
            else:
                release += item + ";"
    # OpenNI2.lib 两者都有
    debug += "OpenNI2.lib;"
    release += "OpenNI2.lib;"

    with open(desk + "\\Debug版本.txt", "w", encoding="utf8") as fd:
        fd.write(debug)
    with open(desk + "\\Release版本.txt", "w", encoding="utf8") as fr:
        fr.write(release)
    with open(desk + "\\预编译命令.txt", "w", encoding="utf8") as fy:
        fy.write("_CRT_SECURE_NO_WARNINGS")
    with open(desk + "\\环境.txt", "w", encoding="utf8") as fe:
        fe.write(
            "PATH=$(PCL_ROOT)\bin;$(PCL_ROOT)\3rdParty\FLANN\bin;$(PCL_ROOT)\3rdParty\VTK\bin;$(PCL_ROOT)\Qhull\bin;$(PCL_ROOT)\3rdParty\OpenNI2\Tools;$(PATH)")


if __name__ == '__main__':
    get_gui()
    pcl_path = check_info().replace("/", "\\")
    desk_path = get_desktop()
    save_contains(pcl_path, desk_path)
    lib_path = save_ku(pcl_path, desk_path)
    lib_list = lib_path.split(";")[:-1]
    save_libs(lib_list, desk_path)
    messagebox.showinfo("Info", "全部文件生成完毕\n请到桌面查看！")
