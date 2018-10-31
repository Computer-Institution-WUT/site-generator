## C 语言环境配置教程

[TOC]

* 少量修改自：[知乎]('https://www.zhihu.com/question/40929777/answer/90015056')

### 具体步骤
1. 进入 [MingW](http://nuwen.net/mingw.html) 官网
    * 进入下载页，该页面下面的 How To Install中介绍了安装方法，即双击 EXE 解压到指定位置即可。等待安装完成后会在指定的目录下看到一个名为 MinGW 的文件夹，双击进入文件夹后应大致如下图所示：
    * 打开图中标识的 set_distro_paths.bat，它会自动帮你设置好环境变量。
    * 现在在 CMD/PowerShell使用 cd 进入你放 .c 文件的目录：
    * 使用文本编辑器（如 [Visual Studio Code](https://code.visualstudio.com/)，点击 Download 即可。）新建一个 hello.c：
    * 在 CMD/Powershell 中输入 gcc hello.c -o hello.exe，应该可以看到 exe 生成了。运行之，成功

2. 下面说怎么在 VSCode 中调试
    * 打开编辑器，按 F1 键打开命令功能，输入 ext install 并回车，可以显示扩展安装菜单。
    * 继续输入 gdb，可以看到一个叫做 Debug 的扩展，按回车安装之，成功的话 VSCode 会在一会儿之后提示重启，按他的要求重启编辑器。
    * 点击左侧第四个「调试」按钮，然后点击「齿轮」按钮，在弹出的列表中选择 GDB，启动 GDB 调试器支持
    * 此时你应该能看到窗口中显示了一个叫做 launch.json 的配置文件，并且左侧的文件列表中多了一个 .vscode 的目录，以及 launch.json 的文件。在 .vscode 目录下新建一个 tasks.json 的文件，然后把两个配置文件的内容如下设置：
    ```
    .vscode/launch.json：{
        "version": "0.2.0",
        "configurations": [{
            "name": "Debug",
            "type": "gdb",
            "request": "launch",
            "target": "./out.exe",
            "cwd": "${workspaceRoot}",
            "preLaunchTask": "gcc"
        }]
    }
    ```
    * .vscode/tasks.json：（第三行中的 hello.c 要和你正在编辑的 .c 文件名相同，如果更换了文件，此处也要对应修改。）
    ```
    {
        "version": "0.1.0",
        "command": "gcc",
        "args": ["-g", "hello.c", "-o", "out.exe"],
        "problemMatcher": {
            "owner": "c",
            "fileLocation": ["relative", "${workspaceRoot}"],
            "pattern": {
                "regexp": "^(.*):(\\d+):(\\d+):\\s+(warning|error):\\s+(.*)$",
                "file": 1,
                "line": 2,
                "column": 3,
                "severity": 4,
                "message": 5
            }
        }
    }
    ```
    * 点左侧第四个按钮切到调试界面，点击绿色三角（Launch，快捷键 F5），如果之前设置成功的话，此时调试器应该可以成功了。你可以试着点击下行号左侧的空白新建个断点然后启动调试，此时你应该看到一个黄色的箭头停在断点上，并且左侧显示出当前的局部变量（如此处是 x），此时就可以使用标准的调试功能了。

