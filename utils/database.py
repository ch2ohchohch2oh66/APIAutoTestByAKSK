# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2024/11/18
# Description: Keep Hungry Keep Foolish
import logging

import pymysql
from typing import List, Dict, Any
from utils.cofig_cache import EnvConfig

logger = logging.getLogger()


class DatabaseHelper:
    def __init__(self):
        # 从全局配置中获取数据库连接信息
        database_config = EnvConfig.get('database')
        logger.info(f'数据库信息为：{database_config}')
        self.host = database_config.get('host')
        self.port = database_config.get('port')
        self.user = database_config.get('user')
        self.password = database_config.get('password')
        self.database = database_config.get('database')
        self.connection = None

    def connect(self):
        """建立数据库连接"""
        try:
            self.connection = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
                charset='utf8mb4'
            )
            logger.info("数据库连接成功")
        except Exception as e:
            logger.info(f"数据库连接失败: {str(e)}")
            raise

    def execute_query(self, sql: str, params: tuple = None) -> List[Dict[str, Any]]:
        """执行查询SQL并返回结果"""
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql, params)
                result = cursor.fetchall()
                return result
        except Exception as e:
            logger.info(f"查询执行失败: {str(e)}")
            raise

    def execute_update(self, sql: str, params: tuple = None) -> int:
        """执行更新SQL并返回影响行数"""
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                rows = cursor.execute(sql, params)
                self.connection.commit()
                return rows
        except Exception as e:
            self.connection.rollback()
            logger.info(f"更新执行失败: {str(e)}")
            raise

    def close(self):
        """关闭数据库连接"""
        if self.connection:
            self.connection.close()
            logger.info("数据库连接已关闭")


# 使用示例
if __name__ == '__main__':
    # 加载环境配置
    EnvConfig.load()

    # 创建数据库助手实例，无需手动传入配置
    db = DatabaseHelper()

    try:
        # 执行查询示例
        query = "SELECT * FROM customers WHERE id = %s"
        results = db.execute_query(query, (3,))
        print("查询结果:", results)

        # 执行更新示例
        update = "UPDATE customers SET name = %s WHERE id = %s"
        affected_rows = db.execute_update(update, ('Be Positive and Constructive', 3))
        print(f"更新影响行数: {affected_rows}")

        query = "SELECT * FROM customers WHERE id = %s"
        results = db.execute_query(query, (3,))
        print("查询结果:", results)

    finally:
        # 确保关闭数据库连接
        db.close()
