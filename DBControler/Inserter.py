#-*- coding:utf-8 -*-

from setting import DBC_USERNAME, DBC_PASSWORD, DBC_HOST, DBC_DBNAME 


class Inserter:

    def __init__(self):
        self.conn = MySQLdb.connect(
            user=DBC_USERNAME,
            passwd=DBC_PASSWORD,
            host=DBC_HOST,
            db=DBC_DBNAME
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
