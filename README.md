# Taiwan Realtime Text Translator

一个基于快捷键的实时文本翻译工具，专为将文本转换为台湾本地语言习惯而设计。

## 功能特点

- 🎯 快捷键触发：使用 F11 快速翻译当前输入框文本
- 🔥 实时翻译：调用阿里巴巴百鍊平臺的Qwen大模型进行高质量翻译
- 💻 跨平台支持：Windows/macOS/Linux
- 🚀 简单易用：无需复杂配置，一键翻译

## 安装依赖

```bash
pip install pynput openai pyautogui pyperclip
```

## 使用说明

1. 设置环境变量（在 .bashrc 或系统环境变量中）：
```bash
export DASHSCOPE_API_KEY=your_api_key
```

2. 运行程序：
```bash
python hotkey_framework.py
```

3. 使用方式：
   - 将焦点放在任意文本输入框
   - 按下 F11 键
   - 系统将自动：
     1. 全选并复制当前输入框内容
     2. 调用AI翻译为台湾本地语言习惯
     3. 用翻译结果替换原文本

## 自定义翻译风格

如需修改翻译风格，编辑 `hotkey_actions.py` 文件中的系统提示词：
```python
{"role": "system", "content": "你是一個台灣本地語言大師，男性IT工程師,精通台灣IT文化與俚語,你的任務是“翻譯”用戶的輸入，到台灣本地的語言習慣，讓即使是台灣本地人都看不出用戶是外地人，當然，翻譯的句子不要太冗長了，和用戶的輸入長度盡可能保持一致，不要翻譯成很機車的那種風格"}
```

## 许可证

本项目采用 [MIT 许可证](LICENSE)
