# 《请留遗言》FF14RP用随机抽词工具
为FF14 RP店游戏《请留遗言》设计

For FFXIV RP Dying Message

本软件用于辅助RP店游戏，欢迎光临最终幻想14中国区服务器豆豆柴大区太阳海岸服务器涅斯特RP店

This software is designed to assist with RP venue games. Welcome to 涅斯特 in 太阳海岸 on 豆豆柴 server of Final Fantasy XIV (China region).

以下介绍文本请以中文版为准，英文版使用AI翻译，可能存在描述不准确等问题，欢迎提交Issue协助改正

The following content shall prevail in the Chinese version. The English version is translated by AI and may contain inaccuracies. Welcome to submit Issues to assist with corrections.

## 使用前准备/Preparation

- （自编译时）需安装依赖 pyperclip

  (For self-compilation) Requires dependency: pyperclip

```python
pip install pyperclip
```
- 需准备TXT格式词表，并命名为wordlist，词语与词语之间需要使用换行符隔开

  Prepare a TXT-format word list named "wordlist", with each word separated by a line break.

## 功能介绍/Function
本软件将在`wordlist.txt`中随机抽选9个词语，每个词语用空格分隔，并复制到系统剪贴板中，

Nine words will be randomly selected from `wordlist.txt`, separated by spaces, and copied to the system clipboard.

随后继续抽取时，将抽取此前未被抽取的词语，直至剩余词语数不足9词为止

Subsequent draws will select from remaining unchosen words until the wordlist has fewer than 9 words left.
## 备注/Note

我不懂Python，代码完全交给deepseek撰写，我仅在本地测试其可用性，欢迎大家通过提交Issue向我反馈bug，我能修一定全力修

I don't know Python. I relied entirely on DeepSeek for the coding and only performed local functionality tests. Please submit Issues for any bugs found—I'll prioritize fixing them.
