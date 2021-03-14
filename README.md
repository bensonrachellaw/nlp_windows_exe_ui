# nlp_windows_exe_ui
[![star](https://gitee.com/bensonrachel/nlp_windows_exe_ui/badge/star.svg?theme=dark)](https://gitee.com/bensonrachel/nlp_windows_exe_ui/stargazers)
#### 介绍
python3.6-制作一个含有NLP基本功能系统（Windows exe）自然语言处理系统。系统功能：分词、词性标注、关键词提取、文本分类；由于要打包成exe的关系，我将原本的项目的多个文件的集成到一个python文件（窗体文件）里，只保留了使用这个系统所需要用的函数，方便打包，通俗地讲就是，比如生成词向量过程，装袋过程，模型训练过程的，以及一些中间步骤的程序代码，这些有些涉及很多库的，这些打包进去。但是整个项目里的东西是完整的（包括数据）

运行这个系统需要数据支持，所以请务必像我这样将所要用的数据跟exe放在同一个文件夹下，否则运行不了。
![输入图片说明](https://images.gitee.com/uploads/images/2021/0313/171139_e45ce058_8773742.png "屏幕截图.png")


#### 软件架构
系统实现：

分词：使用jieba中文分词（去停用词，精确模式）；

词性标注：使用jieba库里的posseg包进行词性标注；

关键词提取：基于lda模型结合tfidf的最合适前六个词；

文本分类：给复旦预料数据进行分词，生成词向量，装袋（词袋模型），接着训练集训练，多次调参，具体参数注释和代码中有，然后再选择相应测试预料进行测试，用的是skleran库的多项式朴素贝叶斯算法。

![输入图片说明](https://images.gitee.com/uploads/images/2021/0313/171914_f8a5c0df_8773742.png "屏幕截图.png")

#### 安装教程

使用步骤：打开项目，打开dist文件夹，运行ui.exe即可。
![输入图片说明](https://images.gitee.com/uploads/images/2021/0313/171918_f9ae3b17_8773742.png "屏幕截图.png")

#### 特技

使用Pyinstaller进行命令行打包

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
