# time  : 2020/9/8 11:53
# author :wujiajia
# email :wujiajia666@qq.com
# file  : fa1.py
# Software: PyCharm
# python_version: 
# funcation:



# encoding='utf-8'
import pandas as pd
import numpy as np

# np.set_printoptions(suppress=True)
# pd.set_option('display.float_format', lambda x: '%.2f' % x)

def deal_str(data):
    data = str(data)+'\t'
    return data

# df['平台单号'] = df['平台单号'].map(deal_str)
# df.to_csv('D:/data/a.csv')


# pd.set_option('display.float_format',lambda x : '%.2f' % x)
#
# def main():
#     with open(r"C:\Users\admin\Desktop\fa2.html", "r") as f:       ###读入文件
#         htmll = f.read()
#     html_data = pd.read_html(htmll,converters={'2':str})
#     print(html_data)
    # # converters = {'列名': str}
    # for i in html_data:
    #     table_date = pd.DataFrame(i)
    #     print(table_date)
    #     table_date.to_csv(r'C:\Users\admin\Desktop\fa2.csv',encoding='utf-8-sig')
    #     #print table_date
    #     # 禁用科学计数法

def main():
    file = ""
    ht = pd.read_html(r"C:\Users\admin\Desktop\fa2.html")
    # df  = pd.DataFrame(ht[:10])



if __name__ == '__main__':
    main()
