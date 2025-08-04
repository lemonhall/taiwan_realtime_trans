#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快捷键框架 - 通用快捷键监听框架
按下自定义快捷键时触发回调函数
"""

import time
import threading
from pynput import keyboard
from pynput.keyboard import Key
import hotkey_actions  # 导入快捷键动作模块

class HotkeyFramework:
    def __init__(self, debug_mode=False):
        self.keyboard_listener = None
        self.is_running = False
        self.debug_mode = debug_mode
        self.hotkey_actions = {}  # 存储快捷键和对应的回调函数
        self.modifiers_state = {
            'ctrl': False,
            'shift': False,
            'alt': False
        }  # 跟踪修饰键状态
        
    def register_hotkey(self, keys, callback):
        """
        注册快捷键和回调函数
        :param keys: 快捷键组合，如 [Key.ctrl, 'a']
        :param callback: 触发时调用的函数
        """
        self.hotkey_actions[tuple(keys)] = callback
        if self.debug_mode:
            print(f"✅ 注册快捷键: {keys}")

    def on_key_press(self, key):
        """处理键盘按键事件"""
        try:
            # 调试信息
            if self.debug_mode:
                print(f"🔍 按键检测: {key}")
            
            # 更新修饰键状态
            self._update_modifiers(key, True)
            
            # 检查是否匹配任何快捷键
            self._check_hotkeys(key)
                
        except Exception as e:
            print(f"❌ 按键处理异常: {e}")
            
    def on_key_release(self, key):
        """处理键盘释放事件"""
        try:
            if self.debug_mode:
                print(f"🔍 释放键检测: {key}")
            
            # 更新修饰键状态
            self._update_modifiers(key, False)
                
        except Exception as e:
            print(f"❌ 释放键处理异常: {e}")
    
    def _update_modifiers(self, key, is_pressed):
        """更新修饰键状态"""
        if key == Key.ctrl or key == Key.ctrl_l or key == Key.ctrl_r:
            self.modifiers_state['ctrl'] = is_pressed
        elif key == Key.shift or key == Key.shift_l or key == Key.shift_r:
            self.modifiers_state['shift'] = is_pressed
        elif key == Key.alt or key == Key.alt_l or key == Key.alt_r:
            self.modifiers_state['alt'] = is_pressed
    
    def _normalize_key(self, key):
        """统一按键表示形式"""
        # 特殊键映射表（虚拟键码到字符）
        vk_to_char = {
            84: 't',  # T键
            65: 'a',  # A键
            66: 'b',  # B键
            67: 'c',  # C键
            # 添加更多映射...
        }
        
        # 优先尝试获取字符表示
        if hasattr(key, 'char') and key.char:
            return key.char
        
        # 如果是特殊键，使用其名称
        if isinstance(key, Key):
            return key.name
        
        # 尝试使用虚拟键码映射
        if hasattr(key, 'vk') and key.vk in vk_to_char:
            return vk_to_char[key.vk]
        
        # 最后尝试使用名称或字符串表示
        if hasattr(key, 'name') and key.name:
            return key.name
        
        return str(key)

    def _check_hotkeys(self, pressed_key):
        """检查当前按键组合是否匹配任何注册的快捷键"""
        # 获取当前激活的修饰键
        active_modifiers = [k for k, v in self.modifiers_state.items() if v]
        
        # 构建当前按键组合（修饰键 + 最后按下的键）
        current_combo = active_modifiers + [pressed_key]
        
        # 将按键统一转换为字符串表示
        normalized_combo = [self._normalize_key(key) for key in current_combo]
        
        if self.debug_mode:
            print(f"🔍 当前按键组合: {normalized_combo}")
        
        # 检查是否匹配注册的快捷键
        for hotkey, callback in self.hotkey_actions.items():
            # 将注册的快捷键也统一为字符串表示
            normalized_hotkey = [self._normalize_key(key) for key in hotkey]
            
            if self.debug_mode:
                print(f"🔍 检查快捷键: {normalized_hotkey}")
            
            # 使用集合比较（无序匹配）
            if set(normalized_hotkey) == set(normalized_combo):
                if self.debug_mode:
                    print(f"🔥 触发快捷键: {normalized_hotkey}")
                try:
                    callback()  # 执行回调函数
                except Exception as e:
                    print(f"❌ 回调函数执行失败: {e}")
                return

    def start(self):
        """启动键盘监听"""
        print("🚀 快捷键框架已启动")
        print("📝 使用说明：")
        print("   • 使用 register_hotkey() 注册快捷键和回调函数")
        print("   • 按下 Ctrl+Q 组合键退出程序")
        if self.debug_mode:
            print("   • 调试模式：显示所有按键信息")
        print("⏳ 等待按键...")
        
        self.is_running = True
        
        try:
            # 创建键盘监听器
            self.keyboard_listener = keyboard.Listener(
                on_press=self.on_key_press,
                on_release=self.on_key_release
            )
            
            # 启动监听器
            self.keyboard_listener.start()
            print("✅ 键盘监听器启动成功")
            
            # 保持程序运行
            while self.is_running:
                time.sleep(0.1)
                
        except KeyboardInterrupt:
            print("⚠️ 检测到Ctrl+C，程序退出")
            self.stop()
        except Exception as e:
            print(f"❌ 键盘监听器启动失败: {e}")
            self.stop()
            
    def stop(self):
        """停止程序"""
        print("🛑 正在停止程序...")
        self.is_running = False
        if self.keyboard_listener:
            try:
                self.keyboard_listener.stop()
                print("✅ 键盘监听器已停止")
            except Exception as e:
                print(f"⚠️ 停止键盘监听器时出错: {e}")

# 示例用法
if __name__ == "__main__":
    print("🎯 快捷键框架示例")
    print("💡 提示：程序启动后，使用 Ctrl+Q 组合键退出程序")
    print("是否开启调试模式？(显示所有按键信息)")
    debug_choice = input("输入 y 开启调试模式，其他任意键关闭: ").strip().lower()
    debug_mode = debug_choice == 'y'
    
    framework = HotkeyFramework(debug_mode=debug_mode)
    
    # 注册快捷键示例（实际使用时替换为需要的功能）
    def sample_action():
        print("🎯 示例功能被触发!")
    
    # 注册快捷键
    framework.register_hotkey([Key.ctrl, Key.alt, 't'], hotkey_actions.action1)
    
    try:
        framework.start()
    except Exception as e:
        print(f"❌ 程序启动失败: {e}")
        print("💡 请确保已安装所需依赖: pip install pynput")
