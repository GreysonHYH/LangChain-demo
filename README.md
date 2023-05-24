# LangChain 实用基础案例
* LangChain & OpenAI & python & pinecone
* 这里没有多余的代码，没有复杂的配置。
* 只有用最精简的代码演示LangChain的部分基础功能，
* 极大地帮助你理解LangChain，构建自己的AI应用。

##

### 目前已更新以下案例，持续更新中，请关注。
* 1.完成一次问答。
* 2.读取本地材料并做出总结。
* 3.将数据插入向量数据库。
* 4.检索向量数据库中，从中得知问题参考了哪些向量数据。
* 5.根据提示词完成回答。
* 6.根据导入的数据 完成回答。
* 7.拥有记忆的聊天。

##

### LangChain介绍
LangChain是一个AI应用开发框架，用来简化使用大语言模型来赋能应用程序。核心思想是将不同的组件连接在一起，如提示模板、大语言模型、代理、记忆、数据库等。

##

### 常用功能概念介绍
#### Loader加载器
 * 从指定源进行加载数据，比如：txt格式，markdown格式，任意的网页 UnstructuredHTMLLoader、PDF PyPDFLoader、印象笔记 EverNoteLoader，当使用loader加载器读取到数据源后，数据源需要转换成 Document 对象后，后续才能进行使用。
#### 文本分割
 * 不管是把文本当作prompt发给openai api，还是还是使用openai api embedding功能都是有字符限制的。比如将一份300页的pdf发给openai api，让他进行总结，他肯定会报超过最大Token错。所以这里就需要使用文本分割器去分割loader进来的 Document。
#### 向量数据库
 * 数据相关性搜索其实是向量运算。不管是使用 openai api embedding 功能还是直接通过向量数据库直接查询，都需要将加载进来的数据进行向量化，才能进行向量运算搜索。
#### chain链
 * 可以把 Chain 理解为任务。一个 Chain 就是一个任务，当然也可以像链条一样，一个一个的执行多个链。
#### Embedding
 * 可理解为将数据转换为向量的过程。


