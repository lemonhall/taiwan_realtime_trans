# Hotkey Framework

一个通用的Python快捷键监听框架，支持自定义快捷键组合和回调函数。

## 功能特点

- 🎯 自定义快捷键组合（支持Ctrl、Alt、Shift等修饰键）
- 🔥 按键事件实时监听
- 🐞 内置调试模式，显示详细按键信息
- 🚀 简单易用的API
- 💻 跨平台支持（Windows/macOS/Linux）

## 安装依赖

```bash
pip install pynput
```

## 使用示例

```python
from pynput.keyboard import Key
from hotkey_framework import HotkeyFramework

# 创建框架实例
framework = HotkeyFramework(debug_mode=True)

# 定义回调函数
def my_action():
    print("快捷键触发！执行自定义操作...")

# 注册快捷键 Ctrl+Alt+T
framework.register_hotkey([Key.ctrl, Key.alt, 't'], my_action)

# 启动监听
framework.start()
```

## 运行示例

```bash
python hotkey_framework.py
```

程序启动后：
1. 输入 `y` 开启调试模式（显示详细按键信息）
2. 按下 `Ctrl+Alt+T` 组合键触发示例功能
3. 按下 `Ctrl+Q` 退出程序

## 贡献指南

欢迎提交Pull Request！请确保：
1. 代码符合PEP8规范
2. 添加必要的单元测试
3. 更新文档（README.md）

## 许可证

本项目采用 [MIT 许可证](LICENSE)
