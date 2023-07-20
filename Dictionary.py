#!/usr/bin/env python
# coding: utf-8

# In[2]:


def find_word(data, word):
    for eng, vie in data.items():
        if eng == word:
            return vie
    return None

def main():
    # Từ điển lưu trữ các từ tiếng Anh và tiếng Việt
    dictionary = {
        'hello': 'xin chào',
        'world': 'thế giới',
        'python': 'ngôn ngữ lập trình Python',
        'programming': 'lập trình',
        'computer': 'máy tính'
    }

    # Nhập từ cần tra cứu từ người dùng
    input_word = input("Nhập từ cần tra cứu (tiếng Anh): ")

    # Tìm từ trong từ điển
    translated_word = find_word(dictionary, input_word)

    # In ra kết quả
    if translated_word:
        print("Nghĩa của từ", input_word, "là:", translated_word)
    else:
        print("Từ", input_word, "không có trong từ điển.")

if __name__ == "__main__":
    main()

