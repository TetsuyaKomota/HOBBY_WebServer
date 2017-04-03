#coding:utf-8
import requests as req
import json
import re
import math

from setting import RAKUTEN_API_KEY

def Api_getBookInfo(input_Isbn, date):
        
        converted_Isbn = convert13To10(input_Isbn)

        url = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20130522" #最後の日付はapiのバージョンっぽい
        app_id  = RAKUTEN_API_KEY #自分のapp_idを入力
        isbn    = converted_Isbn

        payload = {
                'format':'json',
                'isbn':isbn,
                'applicationId':app_id
        }
        res = req.get(url,params=payload)
        data = res.json()

        # 楽天API に登録されていない（見つからない）場合
        if len(data[u'Items']) == 0:
            return  '&amazon('+converted_Isbn+'){large}\n'+ \
                    '*基本情報\n' +\
                    '{| width="500px" class="custom-css" style="color:#6e7955"\n' + \
                    '|タイトル||\n' + \
                    '|作者名||\n' + \
                    '|巻数||\n' + \
                    '|出版社||\n' + \
                    '|部室に追加した人|'+'|\n' + \
                    '|最終更新者|'+'|\n' + \
                    '|編集日|' + date + '|\n' + \
                    '|}'
        
        return  '&amazon('+converted_Isbn+'){large}\n'+ \
           '*基本情報\n' +\
           '{| width="500px" class="custom-css" style="color:#6e7955"\n' + \
           '|タイトル|'+data[u'Items'][0][u'Item'][u'title'].encode('utf-8')+'|\n' + \
           '|作者名|'+data[u'Items'][0][u'Item'][u'author'].encode('utf-8')+'|\n' + \
           '|巻数||\n' + \
           '|出版社|'+data[u'Items'][0][u'Item'][u'publisherName'].encode('utf-8')+'|\n' + \
           '|部室に追加した人|'+'|\n' + \
           '|最終更新者|'+'|\n' + \
           '|編集日|' + date + '|\n' + \
           '|}'

def convert13To10(isbn13):
        if isbn13.isdigit() == False or  (int(math.log10(int(isbn13)))+1 != 10 and int(math.log10(int(isbn13)))+1 != 13):
            return 9999999999
        elif int(math.log10(int(isbn13)))+1 == 10:
            return str(int(isbn13))
        isbn10 = str(isbn13)[3:12]
        check_digit = 0

        for i in range(len(isbn10)):
                check_digit += int(isbn10[i]) * (10 - i)

        check_digit = 11 - (check_digit % 11)

        if check_digit == 10:
            check_digit = 'X'
        elif check_digit == 11:
            check_digit = '0'
        else:
            check_digit = str(check_digit)

        isbn10 += check_digit
        return isbn10

if __name__ == "__main__":
        print(Api_getBookInfo('9784832252356', '2017-04-01'))
        

