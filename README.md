> 日常无聊，写的小脚本存放点，下方是每个脚本的功能及使用方式的介绍
>
> 每个项目中，`xxx.py` 为项目源码，`dist` 目录下的 `xxx.exe` 文件均为可执行文件



### 项目一：get_pcl_cmake

**脚本功能：自动生成 PCL 工程中的 CmakeLists.txt 文件**

PCL 点云库如果是使用默认路径安装的，那么在 PCL 工程的 `CMakeLists.txt` 文件中可以直接使用 `find_package(PCL REQUIRED)` 直接导入 PCL

但是如果是自定义的安装目录，据需要手动去设置 PCL 的库目录、包含目录、依赖目录、依赖文件等等，非常麻烦，该脚本就是为了解决该情况而写的

**项目结构**

![image-20220803213639811](https://my-pic-1309513254.cos.ap-shanghai.myqcloud.com//image-20220803213639811.png)

**脚本界面介绍**

![image-20220803213734293](https://my-pic-1309513254.cos.ap-shanghai.myqcloud.com//image-20220803213734293.png)

**【注意】**

1.  `PCL根目录` 指的是：PCL 安装路径中 `bin` 文件夹的父路径

![image-20220803214036401](https://my-pic-1309513254.cos.ap-shanghai.myqcloud.com//image-20220803214036401.png)

![image-20220803214052076](https://my-pic-1309513254.cos.ap-shanghai.myqcloud.com//image-20220803214052076.png)

2. 要使用该脚本，请确保 `OPENNI2` 的安装路径在 PCL 安装目录下的 `3rdParty` 文件夹下 

![image-20220803214437553](https://my-pic-1309513254.cos.ap-shanghai.myqcloud.com//image-20220803214437553.png)

---



### 项目二：pcl_setting_file

**脚本功能：生成 Visual Studio 中 PCL 工程的库目录、包含目录、依赖目录、环境、预编译指令等设置文件**

**脚本介绍**

脚本使用非常简单，双击运行 `exe` 可执行文件，选择 PCL 的根目录，然后点击生成，就会在桌面生成六个 `txt` 文本文件

![image-20220804205126387](https://my-pic-1309513254.cos.ap-shanghai.myqcloud.com//image-20220804205126387.png)

**【注意】**

`PCL根目录` 指的是：PCL 安装路径中 `bin` 文件夹的父路径

![image-20220803214036401](https://my-pic-1309513254.cos.ap-shanghai.myqcloud.com//image-20220803214036401.png)

将这几个文本文件的全部内容复制粘贴到下方对应的配置项中即可

文本文件与设置的对应关系如下：

+ `环境.txt`

![image-20220804205612064](https://my-pic-1309513254.cos.ap-shanghai.myqcloud.com//image-20220804205612064.png)

+ `包含目录.txt`

![image-20220804205832061](https://my-pic-1309513254.cos.ap-shanghai.myqcloud.com//image-20220804205832061.png)

+ `库目录.txt`

![image-20220804205857897](https://my-pic-1309513254.cos.ap-shanghai.myqcloud.com//image-20220804205857897.png)

+ `预编译命令.txt`

![image-20220804205937990](https://my-pic-1309513254.cos.ap-shanghai.myqcloud.com//image-20220804205937990.png)

+ `Debug版本.txt`：（与 `release` 版本设置位置一致，两者选择其一设置即可，根据自己的项目需求）

![image-20220804210043865](https://my-pic-1309513254.cos.ap-shanghai.myqcloud.com//image-20220804210043865.png)

+ `Release版本.txt` ：（与 `debug` 版本设置位置一致，两者选择其一设置即可，根据自己的项目需求）

![image-20220804210046731](https://my-pic-1309513254.cos.ap-shanghai.myqcloud.com//image-20220804210046731.png)















