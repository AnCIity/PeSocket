import json

from Am import code
from softMc import softMc

class amSocket:

    def __init__(self, p_Client, p_Addr):
        self.c_Client = p_Client

        print('进入 {0}'.format(p_Addr))

        while 1:
            #接收信息并解码
            L_data = self.c_Client.recv(1024).decode()
            L_msg = code.decode(L_data)
            # 解析msg  按 softType, funType 进行分发
            l_return = self.handAnaly(L_msg)

            # 处理完毕 或 无数据 即 离开
            if l_return or not L_data:
                print('离开 {0}'.format(p_Addr))
                break
        self.c_Client.close()
    def handAnaly(self, p_Msg):
        l_Dict = json.loads(p_Msg)
        l_SoftType = l_Dict['softType']
        l_FunType = l_Dict['funType']
        l_ParaInfo = l_Dict['paraInfo']

        if l_SoftType == 'softMc':
            softMc(self.c_Client, l_FunType, l_ParaInfo)

        return True