from amMysql import amMysql

class softData:

    def __init__(self):
        self.Mysql = amMysql("106.14.163.129", "AnSoft", "Asanyunf1124", "AnSoft", "AsInfo")

    def softAdd(self, p_softInfo):
        return self.Mysql.add(p_softInfo)


    def softUp(self, p_softInfo):
        softInfo = self.Mysql.query('*', "As_Sign='%s'" % (p_softInfo['Sign']))[0]
        # 判断是否返回数据
        if len(softInfo) is not 0:
            if p_softInfo['nowVer'] == softInfo['As_Version']:
                return False
            else:
                return softInfo
                pass
        else:
            return False