# 总结:通过子类继承父类并实现其接口，我们可以在保持代码结构和逻辑清晰的同时，灵活地扩展和定制功能。这种方式使得代码更加模块化，
# 易于理解和维护。在面向对象编程中，这是一种非常常见且强大的设计模式。
# 父类提供了一个通用的框架或接口，而子类则提供了具体的实现.在面向对象编程中，这是实现多态性的关键技术之一.
from loguru import logger
from pathlib import Path
import re


class SearchEngineBase(object):
    """这段代码实现了一个简单的搜索引擎。它能够将文本文件添加到搜索库中，并允许用户通过关键词搜索这些文件。如果文件内容包含了用户的查询关键词，这个文件的路径会作为搜索结果返回。
    1. **`SearchEngineBase` 类**：定义了搜索引擎的基本框架，包括添加文本到搜索库(`add_corpus`)、处理文本(`process_corpus`)和搜索(`search`)的方法。这是一个抽象基类，具体的处理和搜索逻辑需要在子类中实现。

    2. **`SimpleEngine` 类**：`SearchEngineBase` 的一个具体实现。它通过一个字典(`__id_to_texts`)存储文件路径和文件内容的映射，实现了基本的文本处理和搜索功能。

    3. **`main` 函数**：接受一个搜索引擎实例作为参数，添加指定的文本文件到搜索库中，并允许用户输入查询关键词进行搜索，最后打印出搜索结果。

    关键代码块解释:
    - `class SearchEngineBase(object):` 定义了搜索引擎的基类，包含了添加文本(`add_corpus`)、处理文本(`process_corpus`)和搜索(`search`)的基本方法框架。

    - `def add_corpus(self, file_path):` 该方法用于添加文本文件到搜索库。它读取指定路径的文件内容，并调用 `process_corpus` 方法处理这些内容。

    - `def process_corpus(self, id, text):` 和 `def search(self, query):` 这两个方法在基类中只是抛出异常，具体的实现需要在子类中完成。

    - `class SimpleEngine(SearchEngineBase):` 继承自 `SearchEngineBase`，实现了具体的文本处理和搜索逻辑。

    - `self.__id_to_texts = {}` 在 `SimpleEngine` 的构造函数中初始化，用于存储文件路径和文件内容的映射。

    - `def process_corpus(self, id, text):` 实现了将文件路径和内容添加到 `__id_to_texts` 字典中的逻辑。

    - `def search(self, query):` 实现了搜索逻辑。它遍历 `__id_to_texts` 字典，检查每个文件的内容是否包含查询关键词，如果包含，则将文件路径添加到结果列表中。

    - `def main(search_engine_wl):` 函数接受一个搜索引擎实例，添加指定的文件到搜索库，并允许用户输入查询关键词进行搜索。搜索结果会被打印出来。

    执行流程:
    1. 创建 `SimpleEngine` 实例。
    2. 调用 `main` 函数，传入创建的搜索引擎实例。
    3. 在 `main` 函数中，将指定的文件添加到搜索库(字典)。
    4. 用户输入查询关键词。
    5. 显示搜索结果。
    6. 用户可以继续输入查询关键词进行搜索，直到程序结束"""

    def __init__(self):
        pass

    def add_corpus(self, file_path):
        # 将文件路径&&内容添加到字典中
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)

    def process_corpus(self, id, text):
        # 在Python中，raise NotImplementedError或Exception是一种常用的编程习惯，用于指示某个方法是抽象的，即它需要在子类中被重写和实现，而不是直接在当前类中使用。这种做法在定义基类（或抽象类）时特别有用，因为它为子类提供了一个明确的实现接口。
        raise Exception('process_corpus not implemented.')

    def search(self, query):
        raise Exception('search not implemented.')


class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super().__init__()
        self.__id_to_texts = {}  # 初始化了自己的私有变量，也就是这个用来存储文件名和文件内容的字典。

    def process_corpus(self, id, text):
        self.__id_to_texts[id] = text
        # logger.info(self.__id_to_texts)

    def search(self, query):
        results = []
        for id, text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results


class BOWEngine(SearchEngineBase):
    def __init__(self):
        super().__init__()
        self.__id_to_words = {}

    def process_corpus(self, id, text):
        self.__id_to_words[id] = self.parse_text_to_words(text)

    def search(self, query):
        query_words = self.parse_text_to_words(query)
        results = []
        for id, words in self.__id_to_words.items():
            if self.query_match(query_words, words):
                results.append(id)
        return results

    @staticmethod
    def query_match(query_words, words):
        for query_word in query_words:
            if query_word not in words:
                return False
        return True

    @staticmethod
    def parse_text_to_words(text):
        # 使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^w ]', ' ', text)
        # 转为小写
        text = text.lower()
        # 生成所有单词的列表
        word_list = text.split(' ')
        # 去除空白单词
        word_list = filter(None, word_list)
        # 返回单词的 set
        return set(word_list)


def main(search_engine):
    # 使用列表推导式 获取当前目录下所有指定格式的文件路径(递归搜索)
    for file_path in [f for f in Path.cwd().rglob('*.txt')]:
        search_engine.add_corpus(file_path)

    while True:
        if (query := input("请输入查询关键词：")) == 'exit':
            break
        results = search_engine.search(query)
        # logger.info('found {} result(s):'.format(len(results)))
        print(('found {} result(s):'.format(len(results))))
        for result in results:
            print(result)


search_engine = BOWEngine()

# main(SimpleEngine())

# main(search_engine)
