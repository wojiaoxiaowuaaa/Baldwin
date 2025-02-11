import os

curl_command = """  curl 'https://www.baidu.com/sugrec?&prod=pc_his&from=pc_web&json=1&sid=61027_61986_62063_62058_62075_61879_62094_62114&hisdata=%5B%7B%22time%22%3A1737081181%2C%22kw%22%3A%22%E5%A5%B3%E7%94%9F%E9%95%BF%E7%9B%B8%E9%85%B7%E4%BC%BC%E5%BC%A0%E6%9B%BC%E7%8E%89%E8%B5%B0%E7%BA%A2%22%2C%22fq%22%3A2%7D%2C%7B%22time%22%3A1737439223%2C%22kw%22%3A%22deepseek%22%2C%22fq%22%3A2%7D%2C%7B%22time%22%3A1737444575%2C%22kw%22%3A%22uniswap%E6%95%99%E7%A8%8B%22%2C%22fq%22%3A2%7D%2C%7B%22time%22%3A1737629463%2C%22kw%22%3A%22%E6%AF%9B%E8%BF%9C%E6%96%B0%22%2C%22fq%22%3A2%7D%2C%7B%22time%22%3A1738744311%2C%22kw%22%3A%22bitch%22%7D%2C%7B%22time%22%3A1738916504%2C%22kw%22%3A%22hurry%20up%22%7D%2C%7B%22time%22%3A1738916512%2C%22kw%22%3A%22hurry%22%2C%22fq%22%3A2%7D%2C%7B%22time%22%3A1738997793%2C%22kw%22%3A%22hopper%20%E7%B3%BB%E5%88%97%22%7D%2C%7B%22time%22%3A1738997807%2C%22kw%22%3A%22%E7%BE%8E%E5%9B%BD%E4%B8%BA%E5%AE%89%E5%85%A8%E5%B0%81%E6%9D%80%E3%80%8A%E5%93%AA%E5%90%922%E3%80%8B%3F%E5%81%87%22%2C%22fq%22%3A2%7D%2C%7B%22time%22%3A1738998225%2C%22kw%22%3A%22%E5%85%B7%E4%BF%8A%E6%99%94%E8%A2%AB%E6%9B%9D%E8%B5%84%E4%BA%A7%E6%83%8A%E4%BA%BA%20%E6%97%A0%E9%A1%BB%E6%8C%82%E5%BF%B5%E5%A4%A7s%E9%81%97%E4%BA%A7%22%2C%22fq%22%3A2%7D%5D&_t=1739242161202&req=2&csor=0' \
  -H 'Accept: application/json, text/javascript, */*; q=0.01' \
  -H 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8' \
  -H 'Connection: keep-alive' \
  -H 'Cookie: BIDUPSID=84D9593FDEE5B1310099E6925879BB42; PSTM=1717481333; MCITY=-131%3A; BAIDUID=51B8849D7A9F82947F1017AAEB11BE67:SL=0:NR=10:FG=1; sug=3; sugstore=1; ORIGIN=0; bdime=0; H_WISE_SIDS_BFESS=61027_61178_61216_61206_61211_61213_61209_61230_61283; H_WISE_SIDS=61780_61889; BD_UPN=123253; BAIDUID_BFESS=51B8849D7A9F82947F1017AAEB11BE67:SL=0:NR=10:FG=1; BDRCVFR[PWqFiQhMAWs]=9xWipS8B-FspA7EnHc1QhPEUf; delPer=0; BD_CK_SAM=1; PSINO=2; ZFY=tOIxh:B6EZ0XAy5JljyMBW0SheD0:Ba7bEhU4Y35ttEMc:C; H_PS_PSSID=61027_61986_62063_62058_62075_61879_62094_62114; BD_HOME=1; BA_HECTOR=21248ha104ah0l2la085a08029fsb01jqlelh1u' \
  -H 'Ps-Dataurlconfigqid: 0xafa2a6ce0000210c' \
  -H 'Referer: https://www.baidu.com/?tn=02003390_122_hao_pg' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: ' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: '  """

response = os.popen(curl_command).read()

print(response) # 如果接口返回的是JSON那么这里的response就是JSON

print(type(response))