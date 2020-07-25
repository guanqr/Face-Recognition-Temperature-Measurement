import requests
import json
import numpy as np
import ast

msg = np.load(r'./Data_user/tempdata.npy')

tempName = msg[0]
tempTemp = msg[1]
tempDate = msg[2]

def access_token():
    """"
       获取access_token
    """
    APPID = 'wx9f0b65d9e2e8207c' # 小程序 ID
    APPSECRET = '' # 小程序秘钥
    WECHAT_URL = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + APPID + '&secret=' + APPSECRET
    response = requests.get(WECHAT_URL)
    result = response.json()
    return result["access_token"] # 将返回值解析获取 access_token

def databaseQuery(access_token):
    """
    检索数据库，获取用户 openid
    collection_name 集合的名称
    .limit() 括号内的数值限定返回的记录数
    """
    url = 'https://api.weixin.qq.com/tcb/databasequery?access_token=' + access_token
    
    # query = 'db.collection("user").limit(100).get()'
    query = 'db.collection("user").where({"name":"' + tempName + '"}).get()'
    
    data = {
        "env": "toolbox-01",
        "query": query
    }
    
    response = requests.post(url, data=json.dumps(data))
    length = len(response.json()['data'])
    user = response.json()['data'][length - 1]
    user_dict = ast.literal_eval(user)
    openId = user_dict.get('_openid')
    location = user_dict.get('location')
    
    #print(openId)
    #print(location)
    return [openId,location]

def databaseAdd(access_token):
    """
    新建记录并对内容进行定义
    collection_name 集合的名称
    """
    url = 'https://api.weixin.qq.com/tcb/databaseadd?access_token=' + access_token
    
    query = 'db.collection("temp").add({data:{_openid:"'+ openId +'",name:"'+ tempName +'",temperature:"'+ tempTemp +'",location: "'+ tempLct +'",date:"'+ tempDate +'"}})'
    
    data = {
        "env": "toolbox-01",
        "query": query
    }
    
    response = requests.post(url, data=json.dumps(data))
    result = response.json()
    print(result)

if __name__ == '__main__':
    accessToken = access_token()
    [openId, tempLct] = databaseQuery(accessToken)
    databaseAdd(accessToken)