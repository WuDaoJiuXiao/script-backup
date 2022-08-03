日常无聊，写的小脚本存放点

#### 1 get_pcl_cmake

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