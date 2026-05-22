`scrcpy` 是一个开源的屏幕镜像工具，用于将 Android 设备的屏幕投影到计算机上，并允许通过计算机进行控制。以下是对 `scrcpy` 源码的一些介绍：

- 代码结构：`scrcpy` 的源码结构清晰，包含多个模块和文件。主要的模块包括：
  - `device`：用于与 Android 设备进行通信和控制。
  - `display`：用于处理屏幕显示和图像传输。
  - `input`：用于处理计算机端的输入事件，如鼠标和键盘操作。
  - `server`：用于启动服务器，接收和处理客户端连接。

- 技术栈：`scrcpy` 使用了一些流行的编程语言和库，主要包括：
  - Python：用于实现服务器端和客户端的主要逻辑。
  - `OpenCV`：用于图像处理和屏幕捕捉。
  - `FFmpeg`：用于视频编码和解码。
  - `Protocol Buffers`：用于序列化和反序列化数据。

- 功能实现：`scrcpy` 的主要功能包括：
  - 通过`ADB`（Android Debug Bridge）与 Android 设备建立连接。
  - 捕获设备屏幕的图像，并进行编码和传输。
  - 接收和处理计算机端的输入事件，将其发送到设备上。
  - 支持调整屏幕分辨率、帧率、比特率等参数。




scrcpy 是一个开源的 Android 屏幕镜像和控制工具，其架构主要分为 Client 端和 Server 端。下面是 scrcpy 的启动运行阶段的拆分介绍：

### 架构概述：
1. **Client 端：**
   - 它是运行在计算机上的客户端程序，负责接收用户输入、渲染屏幕内容，并将输入事件发送给 Server 端。

2. **Server 端：**
   - 它运行在 Android 设备上，负责捕获屏幕内容、接收输入事件，并将屏幕数据传输给 Client 端。

3. **通信方式：**
   - Client 和 Server 之间通过 Socket 进行通信。Client 发送输入事件，Server 发送屏幕内容。

### 启动运行阶段：
1. **通过 ADB 连接设备：**
   - scrcpy 通过 ADB（Android Debug Bridge）连接到 Android 设备，确保设备已连接并处于调试模式。

2. **推送文件到设备：**
   - scrcpy 将必要的文件推送到 Android 设备。这些文件包括：
     - `scrcpy-server`：Server 端的二进制文件，通常被推送到 `/data/local/tmp` 目录。
     - `scrcpy-client`：Client 端的二进制文件。

3. **启动 Server 端：**
   - 使用 ADB 在设备上启动 Server 端。通过运行 `scrcpy-server`，Server 端开始监听 Socket 连接。

4. **启动 Client 端：**
   - 在计算机上运行 `scrcpy` 命令，启动 Client 端。
   - Client 连接到 Server，建立 Socket 连接。

5. **交互与控制：**
   - 用户在 Client 界面上进行操作，输入事件被发送到 Server。
   - Server 捕获屏幕内容，将其传输到 Client 进行渲染。
   - Client 接收并显示屏幕内容，同时将用户输入事件传递给 Server。

### 文件推送内容：
推送到 Android 设备的主要文件包括：
- `scrcpy-server`：Server 端二进制文件，用于在设备上运行并捕获屏幕内容。
- `scrcpy-client`：Client 端二进制文件，用于在计算机上运行，接收用户输入和显示屏幕内容。

通过这种架构和启动流程，scrcpy 实现了将 Android 设备屏幕内容镜像到计算机上，并实现了通过计算机对设备进行控制的功能。


app_process 是 Android 系统中的一个核心二进制可执行文件，它用于启动 Android 应用程序的主进程。每个 Android 应用程序都有一个主进程，负责执行应用程序的代码、管理资源、处理用户交互等任务。

在提到 app_process 时，通常涉及到 Android 应用程序的启动和运行过程。这个二进制文件会被用来加载应用程序的 Java 代码，并创建应用程序的主线程。它是 Android 系统的一部分，负责桥接底层的 C/C++ 代码和应用程序的 Java 代码。

在 Android 开发中，app_process 是一个系统进程，它负责管理应用程序的生命周期和资源。每当一个应用程序被启动时，Android 系统都会创建一个新的 app_process 进程来运行该应用程序。

总体来说，DEX 文件是 Android 应用程序的执行单位，其中包含了应用的字节码以及一些额外的信息。这些文件在应用的构建和打包过程中起到关键作用，确保应用可以在 Android 设备上正确运行。

编译过程： 在 Android 应用程序的开发过程中，Java 源代码首先被编译成 Java 字节码（.class 文件）。然后，通过 Android 的构建工具链，这些 Java 字节码文件被转换成 DEX 文件。

Android设备侧不断录屏、编码，将视频流传输给PC，PC进行解码和渲染。

由Client端执行adb push把Server程序上传到设备侧，然后执行app_process将Server端程序运行起来的。完整的命令是adb -s serial shell CLASSPATH=/data/local/tmp/scrcpy-server.jar app_process / com.genymobile.scrcpy.Server 1.25 [PARAMS] 

app_process的好处一个是方便我们在安卓侧运行一个纯java程序（是dalvik的字节码，不是jvm字节码），二个是提权，使程序拥有root权限或者shell同等权限。

app_process 是 Android 系统中的一个核心二进制可执行文件，它用于启动 Android 应用程序的主进程。每个 Android 应用程序都有一个主进程，负责执行应用程序的代码、管理资源、处理用户交互等任务。

app_process 是 Android 上的一个原生程序，是 APP 进程的主入口点。总之就是个可以让虚拟机从 main() 方法开始执行一个 Java 程序的东西啦。

adb forward tcp:6100 localabstract:scrcpy
这个命令的含义是将本地主机上的 tcp 端口 6100 与设备上的 localabstract:scrcpy 端口进行映射。这样，通过本地主机的 localhost:6100 地址就能访问设备上 localabstract:scrcpy 端口的服务。
通常，这样的端口映射可以用于在 PC 端与 Android 设备之间建立通信通道，实现数据传输或远程控制等功能。在这个场景中，可能是为了通过 scrcpy 工具在 PC 上查看并控制 Android 设备的屏幕。

adb forward --list - 列举出当前所有的映射

adb forward tcp:5000 localabstract:scrcpy

adb push ./scrcpy-server /data/local/tmp/scrcpy-server.jar

adb shell CLASSPATH=/data/local/tmp/scrcpy-server.jar app_process / com.genymobile.scrcpy.Server 1.22 log_level=info bit_rate=8000000 tunnel_forward=true lock_video_orientation=0 send_frame_meta=false encoder_name=OMX.qcom.video.encoder.avc

adb shell CLASSPATH=/data/local/tmp/scrcpy-server.jar app_process / com.genymobile.scrcpy.Server SCRCPY_VERSION log_level=info bit_rate=8000000 tunnel_forward=true

1. Server在每次启动scrcpy的时候运行于Android端，对采集到的画面进行编码，并使用多线程，通过socket传输到PC。PC端则使用FFmpeg对画面进行实时解码显示。其中Server使用Java开发，Client使用C开发。


2. 在scrcpy启动时，将scrcpy_sdk中的一个jar push到了安卓设备上.(这个jar并不是java的.class文件，是class Java字节码通过dx工具转换成了dex文件，所以这个jar解压后就有一个dex，这个是安卓上的字节码，是可以直接运行的。)


scrcpy-server.jar主要做三件事情：
开启LocalSocket和PC链接，相应PC端传递过来操作。

源源不断的将屏幕画面输出到PC，使得Mediacodec编码。PC通过FFmpeg解码播放。

使用adb来提高scrcpy-server.jar的运行权限。

===
这里的关键是app_process，但app_process是什么？
这里先说一下正常安卓APP启动的过程，当我们点击Launcher桌面程序的APP图标时，Launcher程序会调用startActivity()函数，通过Binder跨进程通信，发送消息给system_server进程。在system_server进程中，由AMS通过socket通信告知Zygote进程fork出一个子进程(APP进程)。而zygote运行分为三个主要部分：

app_process创建虚拟机，设置虚拟机属性

进入java世界，加载资源

裂变进程：启动system_server、启动app。

也就是说，app_process是启动运行代码的核心。著名的Xposed框架就是利用替换app_process达到Hook目的。
但app_process只能执行dex，不能执行java的class，所以我们是把APK（服务端） push到手机上，APK里有个classes.dex，我们再使用app_process执行这个dex里com.genymobile.scrcpy.Server的public static void main(String... args)方法。
这操作我直接惊呼 WOC！太妙了！而且代码里还写上的进程退出就会自己删除服务端，这会儿真的可以说的神不知鬼不觉的，全程让用户一点感知都没有。我合理怀疑作者写Scrcpy一开始可能不是干正事的。XD