#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/17 0:25
# @Author  : Paulson
# @File    : pratice_1.py
# @Software: PyCharm
# @define  : function
"""
查询数据
用面向对象的方法
"""
from pymysql import connect


class JD(object):
    
    def __init__(self):
        # 创建 Connection 连接
        self.conn = connect(host='localhost', user='root', password='mima', port=3306, db='jing_dong', charset='utf8')
        # 创建的 Cursor 对象
        self.cursor = self.conn.cursor()  # cursor 游标对象
    
    def __del__(self):
        # 关闭
        self.cursor.close()
        self.conn.close()
    
    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)
    
    def show_all_items(self):
        """
        显示所有的商品
        :return:
        """
        sql = 'select * from goods;'
        self.execute_sql(sql)
        
    def show_cates(self):
        sql = 'select name from goods_cates;'
        self.execute_sql(sql)
    
    def show_brands(self):
        sql = 'select name from goods_brands;'
        self.execute_sql(sql)
    
    @staticmethod
    def print_menu():
        print("------京东-------")
        print("1: 所有的商品")
        print("2: 所有的商品分类")
        print("3: 所有商品品牌分类")
        return input("请输入功能对应的序号")

    # 2. 调用这个对象的 run 方法，让其运行
    def run(self):
        while True:
            num = self.print_menu()
            
            if num == "1":
                # 查询所有商品
                self.show_all_items()
            elif num == "2":
                # 查询所有的商品分类
                self.show_cates()
            elif num == "3":
                # 查询所有商品品牌分类
                self.show_brands()
            else:
                print("输入有误，重新输入")


def main():
    # 1. 创建一个JD对象
    jd = JD()
    jd.run()


if __name__ == '__main__':
    main()
