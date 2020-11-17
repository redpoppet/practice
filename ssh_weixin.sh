#!/bin/bash
###SCRIPT_NAME:weixin.sh###
###send message from weixin for login monitor###
###cuiss###
###V1-2016-02-23###

CropID='xxxxxxxxx'
Secret='xxxxxxxxxxxxxxxxxxxx'
GURL="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=$CropID&corpsecret=$Secret"
Gtoken=$(/usr/bin/curl  $GURL -H "DNT: 1" -H "Accept-Encoding: gzip, deflate" -H "Accept-Language: zh-CN,zh;q=0.8" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 BIDUBrowser/8.1 Safari/537.36" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" -H "X-DevTools-Emulate-Network-Conditions-Client-Id: B546FC80-414C-403F-95F0-EB0F70E58EF7" -H "Connection: keep-alive" -H "Cache-Control: max-age=0" --compressed | awk -F \" '{print $4}')

PURL="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=$Gtoken"
function body() {
        local int appId=1
        local userId=$1
        local partyId=2
        local msg='有用户上线请注意:\n主机名：'`hostname`'\n主机ip：'`curl ipecho.net/plain`'\n登录用户：'`whoami`'\n登录时间：'`date`
        printf '{\n'
        printf '\t"touser":"'"$userId"\"",\n"
        printf '\t"toparty":"'"$partyId"\"",\n"
        printf '\t"msgtype": "text",'"\n"
        printf '\t"agentid":"'"$appId"\"",\n"
        printf '\t"text":{\n'
        printf '\t\t"content":"'"$msg"\"
        printf '\n\t},\n'
        printf '\t"safe":"0"\n'
        printf '}\n'
}
/usr/bin/curl --data-ascii "$(body $1)" $PURL
