from tkinter import Tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from tkinter import StringVar
from os import path
from os import listdir


# 创建 GUI 页面
def get_gui():
    # 全局变量：最低版本、工程名、C++版本、PCL安装目录、输出目录、lib版本
    global low_ver_text, pro_name, c_plus_ver, pcl_dir, output_dir, lib_ver, root

    # 窗体初始化
    root = Tk()
    root.title("PCL工程自动生成CMakeLists")
    root_width = 380
    root_height = 250
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry("{}x{}+{}+{}".format(root_width, root_height, int((screen_width - 500) / 2), int((screen_height - 300) / 3)))
    root.maxsize(width=450, height=250)
    root.minsize(width=380, height=250)
    root.resizable(True, False)

    # 1: CMake 最低版本信息
    low_ver_text = StringVar()
    Label(text="设置CMake最低版本(默认为3.8)：", font=("微软雅黑", 10)).place(x=10, y=10)
    low_ver_text.set("3.8")
    version_list = ["3." + str(i) for i in range(0, 25)]
    ttk.Combobox(master=root, width=15, height=10, font=("", 10), state="readonly", textvariable=low_ver_text, values=version_list).place(x=210, y=12)

    # 2: 项目名称
    pro_name = StringVar()
    Label(text="设置项目名称：", font=("微软雅黑", 10)).place(x=10, y=40)
    Entry(root, textvariable=pro_name, width=34).place(x=100, y=40)

    # 3: C++版本
    c_plus_ver = StringVar()
    Label(text="设置C++版本号(默认为14)：", font=("微软雅黑", 10)).place(x=10, y=70)
    c_plus_ver.set("14")
    c_plus_list = [str(i) for i in range(1, 15)]
    ttk.Combobox(master=root, width=20, height=10, font=("", 10), state="readonly", textvariable=c_plus_ver, values=c_plus_list).place(x=180, y=72)

    # 4: PCL 安装根目录（bin文件夹的父路径）
    pcl_dir = StringVar()
    Label(root, textvariable=pcl_dir).place(x=105, y=130)
    Label(root, text="PCL库根目录：", font=("微软雅黑", 10)).place(x=10, y=130)

    # 打开系统文件夹选择器
    def choose_dir():
        file_path = filedialog.askdirectory()
        pcl_dir.set(file_path)

    Button(root, text="选择PCL根目录", font=("微软雅黑", 8), bg="#56FD79", command=choose_dir).place(x=90, y=100)

    # 5: 文件输出目录
    output_dir = StringVar()
    Label(root, textvariable=output_dir).place(x=105, y=155)
    Label(root, text="文件输出目录：", font=("微软雅黑", 10)).place(x=10, y=155)

    # 打开系统文件夹选择器
    def choose_out():
        p = filedialog.askdirectory()
        output_dir.set(p)

    Button(root, text="选择文件输出目录", font=("微软雅黑", 8), bg="#56FD79", command=choose_out).place(x=200, y=100)

    # 6: 依赖版本选择
    lib_ver = StringVar()
    Label(text="选择lib依赖版本：", font=("微软雅黑", 10)).place(x=10, y=180)
    lib_ver.set("debug")
    lib_ver_list = ["debug", "release"]
    ttk.Combobox(master=root, width=20, height=10, font=("", 10), state="readonly", textvariable=lib_ver, values=lib_ver_list).place(x=120, y=180)

    # 7: 创建文件按钮
    Button(root, text="生成文件", font=("微软雅黑", 8), width=30, bg="#358EFF", command=get_info).place(x=80, y=210)

    root.mainloop()


# 信息判空
def check_info(info: dict) -> bool:
    for value in info.values():
        if (value is None) or value == "" or len(value) == 0:
            return False


# 获取输入的所有信息
def get_info() -> dict:
    info = {}
    info['low_ver_text'] = low_ver_text.get()
    info['pro_name'] = pro_name.get()
    info['c_plus_ver'] = c_plus_ver.get()
    info['pcl_dir'] = pcl_dir.get()
    info['output_dir'] = output_dir.get()
    info['lib_ver'] = lib_ver.get()

    if check_info(info) == False:
        messagebox.showwarning("Warning", "请将所有信息填写完整！")
    else:
        root.quit()
        return info


# 根据PCL目录，得到包含目录、库目录、依赖库的内容
def get_dep_content(pcl_path: str) -> list:
    # 包含目录
    contains_dir = {}
    contains_dir["PCL_HEAD_FILE_PATH"] = pcl_path + "/include/" + listdir(pcl_path + "/include")[0]
    contains_dir["BOOST_HEAD_FILE_PATH"] = pcl_path + "/3rdParty/Boost/include/" + listdir(pcl_path + "/3rdParty/Boost/include")[0]
    contains_dir["EIGEN_HEAD_FILE_PATH"] = pcl_path + "/3rdParty/Eigen/" + listdir(pcl_path + "/3rdParty/Eigen")[0]
    contains_dir["FLANN_HEAD_FILE_PATH"] = pcl_path + "/3rdParty/FLANN/include"
    contains_dir["QHULL_HEAD_FILE_PATH"] = pcl_path + "/3rdParty/QHULL/include"
    contains_dir["VTK_HEAD_FILE_PATH"] = pcl_path + "/3rdParty/VTK/include/" + listdir(pcl_path + "/3rdParty/VTK/include")[0]
    contains_dir["OPENNI2_HEAD_FILE_PATH"] = pcl_path + "/3rdParty/OpenNI2/Include"

    # 库目录
    ku_dir = {}
    ku_dir["PCL_LIB_PATH"] = pcl_path + "/lib"
    ku_dir["BOOST_LIB_PATH"] = pcl_path + "/3rdParty/Boost/lib"
    ku_dir["FLANN_LIB_PATH"] = pcl_path + "/3rdParty/flann/lib"
    ku_dir["QHULL_LIB_PATH"] = pcl_path + "/3rdParty/Qhull/lib"
    ku_dir["OPENNI2_LIB_PATH"] = pcl_path + "/3rdParty/OpenNI2/Lib"
    ku_dir["VTK_LIB_PATH"] = pcl_path + "/3rdParty/VTK/lib"

    # 依赖库目录
    depend_list = []
    for key, value in ku_dir.items():
        temp_file = listdir(value)
        for tmp in temp_file:
            abv_path = ku_dir[key] + "/" + tmp
            # 只选择其中的文件
            if path.isfile(abv_path):
                depend_list.append(tmp)
    return [contains_dir, ku_dir, depend_list]


# 将 lib 分为 release 版本和 debug 版本
def split_dir(lib_list: list) -> list:
    debug_list, release_list = [], []

    for lib in lib_list:
        # debug 版本:
        # 文件名以 _debug.lib 结尾
        # 文件名含有 -mt-gd
        # 文件名以 以 -gd.lib 结尾
        # 文件名以 _d.lib 结尾
        # 文件名以 d.lib 结尾
        # 文件名以 y.lib 结尾
        if (lib.endswith("_debug.lib")) or ("-mt-gd" in lib) \
                or (lib.endswith("-gd.lib")) or (lib.endswith("_d.lib") \
                                                 or (lib.endswith("d.lib")) or (lib.endswith("y.lib"))):
            debug_list.append(lib)
        # OpenNI2.lib 该文件两者都要有
        elif lib == "OpenNI2.lib":
            debug_list.append(lib)
            release_list.append(lib)
        else:
            release_list.append(lib)
    return [debug_list, release_list]


# 生成文件头相关信息
def cmake_head_info(low_ver_text: str, pro_name: str, c_plus_ver: str, pcl_dir: str) -> str:
    res = ""
    res += "# 最低的CMake版本\n" + "cmake_minimum_required(VERSION {})".format(low_ver_text) + "\n\n"
    res += "# 项目名称\n" + "project({})".format(pro_name) + "\n\n"
    res += "# 编译环境\n" + "set(CMAKE_CXX_STANDARD {})".format(c_plus_ver) + "\n\n"
    res += "# PCL 根目录\n" + "set(PCL_DIR \"{}\")".format(pcl_dir)
    return res


# 生成包含目录相关信息
def cmake_contains_info(infos: dict, pcl_dir: str) -> str:
    res = "# 设置PCL的包含目录\n"
    for key, value in infos.items():
        tmp = value.replace(pcl_dir, "${PCL_DIR}")
        res += "set({0} \"{1}\")".format(key, tmp) + "\n"
    res += "\n# 将包含目录引入\ninclude_directories("
    for key in infos.keys():
        res += "${" + key + "} "
    res = res[:-1] + ")"
    return res


# 生成库目录相关信息
def cmake_ku_info(info: dict, pcl_dir: str) -> str:
    res = "# 设置PCL及第三方库所在的目录\n"
    for key, value in info.items():
        tmp = value.replace(pcl_dir, "${PCL_DIR}")
        res += "set({0} \"{1}\")".format(key, tmp) + "\n"
    res += "\n# 将库目录引入\nlink_directories("
    for key in info.keys():
        res += "${" + key + "} "
    res = res[:-1] + ")"
    return res


# 生成依赖目录相关信息
def cmake_lib_info(infos: list, lib_ver: str) -> str:
    res = "#将源代码添加到此项目的可执行文件\nadd_executable(${PROJECT_NAME} main.cpp)\n\n#设置附加依赖项\nset(\n"
    if lib_ver == "debug":
        for debug in infos[0]:
            res += debug + " " * 8 + "\n"
    else:
        for release in infos[1]:
            res += release + " " * 8 + "\n"
    res += ")\n\n"
    res += "#连接附加依赖项\ntarget_link_libraries(${PROJECT_NAME} ${PCL_LIBRARIES})"
    return res


# 储存生成的文件
def save_file(org_str: str, out_dir: str):
    with open(out_dir + "/CMakeLists.txt", "w", encoding="UTF8") as f:
        f.write(org_str)
    messagebox.showinfo("Info", "文件生成完毕\n请到输出目录中查看!")


# 主函数
def main():
    get_gui()
    info_dic = get_info()
    low_ver_text = info_dic['low_ver_text']
    pro_name = info_dic['pro_name']
    c_plus_ver = info_dic['c_plus_ver']
    pcl_dir = info_dic['pcl_dir']
    output_dir = info_dic['output_dir']
    lib_ver = info_dic['lib_ver']

    contents = get_dep_content(pcl_dir)

    head_info = cmake_head_info(low_ver_text, pro_name, c_plus_ver, pcl_dir)
    contains_dir_info = cmake_contains_info(contents[0], pcl_dir)
    ku_dir_info = cmake_ku_info(contents[1], pcl_dir)
    lib_dir_info = cmake_lib_info(split_dir(contents[2]), lib_ver)

    ori_str = head_info + "\n\n" + contains_dir_info + "\n\n" + ku_dir_info + "\n\n" + lib_dir_info
    save_file(ori_str, output_dir)


if __name__ == '__main__':
    main()
