# yuanshen-锄地用python脚本手柄版

## 简介
适用于pc手柄玩家原神联机锄地用python脚本，当前版本实现基本的全自动传送和路线切换——用于某shg锄地。

## 声明
- 本项目系个人随意开发，没有长期更新和维护的意图（maybe）。
- 本人没有任何python项目开发的相关经验，该程序未经任何安全性考量，优化过程，90%系XXX-4模型编写，出现bug应首先尝试重写，或者求助他人，解决问题之后可以发一份issue，作者会提供除了帮助以外的一切帮助。
- 本人意图借助远程仓库进行备份，无发行出售副本及相关行为。

- 不宣传提倡使用相关脚本，如遇卷卷系个人行为。

## 环境配置
### 适配
- 本脚本目前版本只适配xbox系列手柄。（作者无其他手柄投入测试，其他手柄用户或许需要自己写适配，详情参考vgamepad库接口文档，作者会提供除了帮助以外的一切帮助）
- 编写基于python3，测试运行在windows10/11 python3.10+环境。
- 测试环境为 原神纯净版 1920x1080 120~200帧率

### 运行
- 测试运行该脚本需要安装完整的python3环境。
- python环境中需要配置vgamepad和pygame库，以下是pip配置需要的指令

```shell
pip install vgamepad
pip install pygame
```

下载失败可临时更换清华源重新尝试

```shell
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple vgamepad
```

```shell
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pygame
```

## 打开方式
使用VScode或python相关集成环境打开目录，打开main.py文件，使用控制台或按键运行/调试。

## 路线更新
-  2024.5.11 新增路线-6线和镀金驮线
## 使用说明

 1. 开始运行后出现图形化窗口并没有出现报错即运行成功，双击右侧摇杆键暂停程序
 2. 使用前将地图移动速度调整至5速，吸附调整至最大。
 3. 十字键左右键切换点位,向前进点和向后退点
 4. 左肩键（LS）执行自动传送功能。注意：需要使用轮盘请先将程序暂停后再用
> 注：默认的手柄键位如下（因为是我的手柄键位）需要自定义请在gamepad_controller.py及文件中自行修改。
> 如遇各种延时偏差或许系咱们cpu时钟不能同频共振或着并没有在使用pc120帧纯净原神事宜达成默契等复杂原因。相关使用测试运行在图像设置为1920x1080 120~200帧率，如遇偏差可以自行在routes文件夹修改延时。

![image.png|600](https://picformscyanveg-1319504596.cos.ap-shanghai.myqcloud.com/pic/202405120219849.png)


> 注2：如果你没有使用文本编辑器或记事本修改代码的经验，可以通过GUI界面中`Edit Routes`按钮，点击顶栏“file -> open”打开routes文件夹内的路线py文件，修改后进行保存，以此对路线进行调整。
> 
![image.png|250](https://picformscyanveg-1319504596.cos.ap-shanghai.myqcloud.com/pic/202405120311715.png)

![image.png|250](https://picformscyanveg-1319504596.cos.ap-shanghai.myqcloud.com/pic/202405120315841.png)

## 关于
如果你看到了这里说明你对此脚本使用的困惑超过了作者本人，为此作者特地额外支付XXX-4共0.8刀乐创造了一份本人并没有经过跨环境测试的包体，或许可以帮助你在无需安装python的情况下运行本项目。
- 使用下载release进行解压，不更改文件夹结构的情况下运行RouteLoader.exe即可。
- 弹出报错有可能系Xbox手柄未链接，或ViGEmBus驱动未正确安装，请移步相关驱动官网或查找教程安装，压缩包中一并提供了截至2024-05-12日官网提供的最新版本下载包(ViGEmBus_1.22.0_x64_x86_arm64.exe)。
- 官网链接 [ViGEm Bus Driver - Efficient Virtual Gamepad Emulation](https://vigembus.com/)
- [官方驱动Github下载链接](https://github.com/nefarius/ViGEmBus/releases)
