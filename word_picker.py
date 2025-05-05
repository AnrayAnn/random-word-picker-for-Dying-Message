import os
import random
import sys
import pyperclip

def check_wordlist():
    if getattr(sys, 'frozen', False):
        exe_dir = os.path.dirname(sys.executable)
    else:
        exe_dir = os.path.dirname(os.path.abspath(__file__))
    
    file_path = os.path.join(exe_dir, 'wordlist.txt')
    
    if not os.path.exists(file_path):
        print("词汇表不存在，请将wordlist文件与程序放置于同一文件夹内")
        return None
    return file_path

def get_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            words = list(set(f.read().splitlines()))
            words = [w.strip() for w in words if w.strip()]
            return words
    except Exception as e:
        print(f"文件读取失败: {e}")
        return []

def main():
    try:
        file_path = check_wordlist()
        if not file_path:
            print("文件读取失败")
            input("\n按任意键退出程序...")
            return
        
        words = get_words(file_path)
        if not words:
            print("词汇表为空，请检查wordlist.txt文件")
            input("\n按任意键退出程序...")
            return
        
        remaining = words.copy()
        random.shuffle(remaining)
        
        while True:
            if len(remaining) < 9:
                print("剩余词语不足9个，程序终止")
                input("按任意键退出...")
                break
            
            selected = random.sample(remaining, 9)
            remaining = [w for w in remaining if w not in selected]
            
            result = ' '.join(selected)
            pyperclip.copy(result)
            
            print("已复制以下9个词语到剪贴板：")
            print(result)
            print("\n按回车继续抽取，按Ctrl+C退出...")
            
            try:
                input()
            except KeyboardInterrupt:
                print("程序已退出")
                break
    except BaseException as e:
        print(f"\n发生未捕获的异常: {str(e)}")
        print("代码运行发生错误，请将报错内容截图提交Issue")
        input("按任意键退出程序...")

if __name__ == "__main__":
    main()