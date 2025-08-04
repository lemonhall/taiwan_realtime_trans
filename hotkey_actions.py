import os
from openai import OpenAI

def action1():
    """调用阿里巴巴百鍊平臺的Qwen大模型"""
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
        # 创建聊天完成请求
        response = client.chat.completions.create(
            model="qwen3-235b-a22b",  # 指定模型，例如"qwen"
            messages=[
                {"role": "system", "content": "你是一個台灣本地語言大師，男性IT工程師,精通台灣IT文化與俚語,你的任務是“翻譯”用戶的輸入，到台灣本地的語言習慣，讓即使是台灣本地人都看不出用戶是外地人，當然，翻譯的句子不要太冗長了，和用戶的輸入長度盡可能保持一致，不要翻譯成很機車的那種風格"},
                {"role": "user", "content": "你仔細閱讀一下根目錄下的README.md文檔"},
            ],
            extra_body={"enable_thinking": False}
        )
        # 打印模型回复
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"❌ 调用大模型失败: {e}")

def action2():
    """示例功能2"""
    print("✅ 快捷键触发：执行功能2")
