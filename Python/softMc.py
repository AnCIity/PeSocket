from dataOper import softData
import json

class softMc:
    def __init__(self, p_Client, p_FunType, p_ParaInfo):
        self.c_Client = p_Client
        self.c_softData = softData()
        if p_FunType == 'softAdd':
            self.softAdd(p_ParaInfo)
        elif p_FunType == 'softUp':
            self.softUp(p_ParaInfo)
        else:
            pass


    def softAdd(self, p_ParaInfo):
        if self.c_softData.softAdd(p_ParaInfo) is False:
            pass
        else:
            pass


    def softUp(self, p_ParaInfo):
        result = self.c_softData.softUp(p_ParaInfo)

        if result is False:
            pass
        else:
            result = json.dumps(result, ensure_ascii=False)
            self.c_Client.send(result.encode())