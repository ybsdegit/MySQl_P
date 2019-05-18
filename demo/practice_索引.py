#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 0:44
# @Author  : Paulson
# @File    : practice_索引.py
# @Software: PyCharm
# @define  : function

from pymysql import connect


def main():
    # 创建 Connection 连接
    conn = connect(host='localhost', user='root', password='mima', port=3306, db='jing_dong', charset='utf8')
    # 创建的 Cursor 对象
    cursor = conn.cursor()  # cursor 游标对象
    
    # 插入100000条数据
    for i in range(100000):
        cursor.execute(f"insert into test_index values('ha-{i}')")
        
    # 提交数据
    conn.commit()


if __name__ == '__main__':
    main()
