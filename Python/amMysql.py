import pymysql

class amMysql:

    def __init__(self, p_localhost, p_user, p_pass, p_db, p_table):
        self.c_localhost = p_localhost
        self.c_user = p_user
        self.c_pass = p_pass
        self.c_db = p_db
        self.c_table = p_table
        # 建立连接并获取游标
        self.c_conn = None
        self.c_cursor = None


    @staticmethod # 将列表用字符串连接
    def joinList(p_items, p_text = ", "):
        if p_items is not str:
            p_items = map(str, p_items)

        itemStr = ""
        for item in p_items:
            if itemStr is not "":
                itemStr = itemStr + p_text
            itemStr = itemStr + item

        return itemStr# Str


    @staticmethod  # 将字典键值用字符串连接
    def joinKeyValue(p_items, p_text = "="):
        keys = p_items.keys()
        itemList = []
        for key in keys:
            itemText = key + p_text + p_items[key]
            itemList.append(itemText)
        return itemList# List


    def conn(self):
        self.c_conn = pymysql.connect(self.c_localhost,
                                      self.c_user,
                                      self.c_pass,
                                      self.c_db,
                                      charset='utf8',
                                      cursorclass = pymysql.cursors.DictCursor)
        self.c_cursor = self.c_conn.cursor()


    def close(self):
        self.c_conn.close()


    def submit(self, p_sql):
        self.conn()
        try:
            # 执行sql语句
            self.c_cursor.execute(p_sql)
            # 提交到数据库执行
            self.c_conn.commit()
            results = True
        except:
            # 如果发生错误则回滚
            self.c_conn.rollback()
            results = False
        return results


    def add(self, p_dict):
        # 增
        sql = "INSERT INTO %s(%s) VALUES (%s)" % (self.c_table, self.joinList(p_dict.keys()), self.joinList(p_dict.values()))
        return self.submit(sql)


    def less(self, p_clause):
        # 删
        sql = "DELETE FROM %s WHERE %s" % (self.c_table, p_clause)
        return self.submit(sql)


    def up(self, p_dict, p_clause=str):
        # 改
        sql = "UPDATE %s SET %s WHERE %s" % (self.c_table, self.joinList(self.joinKeyValue(p_dict)), p_clause)
        return self.submit(sql)


    def query(self, p_field, p_clause):
        self.conn()
        # 查
        sql = "SELECT %s FROM %s WHERE %s" % (p_field, self.c_table, p_clause)
        try:
            # 执行SQL语句
            self.c_cursor.execute(sql)
            # 获取所有记录列表
            results = self.c_cursor.fetchall()
        except:
            print("Error: unable to fetch data")
            results = False
        self.close()
        return results