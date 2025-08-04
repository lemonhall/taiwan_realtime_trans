import os
import time
import pyautogui
import pyperclip
from openai import OpenAI

def action1():
    """调用阿里巴巴百鍊平臺的Qwen大模型进行翻译"""
    try:
        # 确保焦点在输入框上
        print("⚠️ 请确保焦点在输入框上...")
        
        # 增加延迟确保焦点稳定
        time.sleep(1)
        
        # 模拟全选当前输入框内容
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(1)  # 增加延迟
        
        # 模拟复制内容到剪贴板
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)  # 增加延迟
        
        # 获取剪贴板内容
        original_text = pyperclip.paste()
        
        if not original_text.strip():
            print("❌ 剪贴板内容为空，请确保已选中文本")
            return
            
        print(f"✅ 获取文本: {original_text[:50]}...")  # 显示前50个字符
    except Exception as e:
        print(f"❌ 获取文本失败: {e}")
        return
    
    # 从环境变量获取API密钥和基础URL
    api_key = os.getenv("DASHSCOPE_API_KEY")
    base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    
    if not api_key or not base_url:
        print("❌ 请设置环境变量 DASHSCOPE_API_KEY 和 BAILIAN_BASE_URL")
        return
    
    # 初始化OpenAI客户端（兼容阿里巴巴百鍊平臺）
    client = OpenAI(
        api_key=api_key,
        base_url=base_url
    )
    
    try:
        # 创建翻译请求
        response = client.chat.completions.create(
            model="qwen3-235b-a22b",
            messages=[
                {"role": "system", "content": "你是一個台灣本地語言大師，男性IT工程師,精通台灣IT文化與俚語,你的任務是“翻譯”用戶的輸入，到台灣本地的語言習慣，讓即使是台灣本地人都看不出用戶是外地人，當然，翻譯的句子不要太冗長了，和用戶的輸入長度盡可能保持一致，不要翻譯成很機車的那種風格"},
                {"role": "user", "content": original_text},
            ],
            extra_body={"enable_thinking": False}
        )
        
        # 获取翻译结果
        translated_text = response.choices[0].message.content
        
        # 将翻译结果放入剪贴板
        pyperclip.copy(translated_text)
        time.sleep(0.5)
        
        # 模拟粘贴替换输入框内容
        pyautogui.hotkey('ctrl', 'v')
        
    except Exception as e:
        print(f"❌ 调用大模型失败: {e}")

def action2():
    """示例功能2"""
    print("✅ 快捷键触发：执行功能2")
