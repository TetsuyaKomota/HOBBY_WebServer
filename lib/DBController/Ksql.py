#-*- coding:utf-8 -*-

from setting import DBC_USERNAME, DBC_PASSWORD, DBC_HOST, DBC_DBNAME 

import MySQLdb

class Ksql:

    def __init__(self):

        # 接続情報を設定ファイルから読み込み
        self.conn = MySQLdb.connect(
            user=DBC_USERNAME,
            passwd=DBC_PASSWORD,
            host=DBC_HOST,
            db=DBC_DBNAME,
            charset='utf8'
        )
    '''
    # テーブルの作成
    sql = 'create table test (id int, content varchar(32))'
    c.execute(sql)
    print('* testテーブルを作成\n')
    
    # テーブル一覧の取得
    sql = 'show tables'
    c.execute(sql)
    print('===== テーブル一覧 =====')
    print(c.fetchone())

    # レコードの登録
    sql = 'insert into test values (%s, %s)'
    c.execute(sql, (1, 'hoge'))  # 1件のみ
    datas = [
        (2, 'foo'),
        (3, 'bar')
    ]
    c.executemany(sql, datas)    # 複数件
    print('\n* レコードを3件登録\n')

    # レコードの取得
    sql = 'select * from test'
    c.execute(sql)
    print('===== レコード =====')
    for row in c.fetchall():
        print('Id:', row[0], 'Content:', row[1])

    # レコードの削除
    sql = 'delete from test where id=%s'
    c.execute(sql, (2,))
    print('\n* idが2のレコードを削除\n')

    # レコードの取得
    sql = 'select * from test'
    c.execute(sql)
    print('===== レコード =====')
    for row in c.fetchall():
        print('Id:', row[0], 'Content:', row[1])

    # データベースへの変更を保存
    conn.commit()

    c.close()
    conn.close()
    '''

    # 接続先を変更
    def changeConnection(self, userName = DBC_USERNAME, password = DBC_PASSWORD, hostName = DBC_HOST, dbName = DBC_DBNAME):
        # 接続情報を設定ファイルから読み込み
        self.conn = MySQLdb.connect(
            user=userName,
            passwd=password,
            host=hostName,
            db=dbName,
            charset='utf8'
        )
 
    # 挿入クエリを飛ばす．
    def insert(self, tableName, values = {}):
        cursor = self.conn.cursor()
        # SQL 文を生成
        sql = u'insert into ' + tableName + u"("

        count = 0
        for c in values:
            count = count + 1
            sql = sql + c
            if count < len(values):
                sql = sql + u","
            else:
                sql = sql + u") values("
            #
        #
        count = 0
        for c in values:
            count = count + 1
            sql = sql + u"'" + values[c] + u"'"
            if count < len(values):
                sql = sql + u","
            else:
                sql = sql + u")"
        # デバッグ．sql 文が正しく作れているか出力
        # print(sql)
        # print(type(sql))
        # 実行
        cursor.execute(sql)
        self.conn.commit()
        cursor.close()
        

    # 選択クエリを飛ばす．
    # 現状はとりあえず where 句のみ．join とかはできない
    def select(self, tableName, select = '*', where = {}):
        cursor = self.conn.cursor()
        # SQL 文を生成
        if isinstance(select, dict) == True:
            sql = u"hogehoge"
        elif select == '*':
            sql = u'select * from ' + tableName
        else:
            return {}
        # where 句を追記していく
        if len(where) > 0:
            sql = sql + u' where '
            for i in where:
                sql = sql + i + "=" + where[i] + " "
            #
        #
        # 実行
        cursor.execute(sql)
        # 取得したエントリーをほにゃほにゃする
        # hogehoge
        self.conn.commit()
        cursor.close()
 

    # ファイルを読み込んで DB に登録する
    # ファイルは 一行目に,\t 区切りのカラム名，二行目以降に,\t 区切りに値を書いたタプル
    def readFile(self, filePath):
        with open(filePath) as file:
            # 一行目を読み込み，登録するカラムを確認する
            line = file.readline()
            columns = line.split(",\t")
            # 無効なカラム名が存在したら終了
            c = self.conn.cursor()
            sql = ''
            for key in column:
                hogehoge


if __name__ == '__main__':
    main()
