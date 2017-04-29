var TalkRoom = React.createClass(
    {
        getInitialState : function(){
            return {
                talk_id     : ""
            };
        },

        componentDidMount : function(){
        },

        componentWillUnmount : function(){
        },

        handleInput : function(e){
            console.log("inputed." + e.key);
            if(e.key === 'j'){
                $.ajax({
                    url: 'http://ec2-13-113-169-250.ap-northeast-1.compute.amazonaws.com:5000/api/hikari_user_validation',
                    Type: 'POST',
                    scriptCharset: 'UTF-8',
                    data: {
                        'user_name' : e.target.value
                    },
                    dataType: 'json', 
                    cache: false,
                })
            }
        },

        render : function(){
            return (
                <div>
                    <h1>ひかりちゃんの部屋</h1>
                    <h2>エントランス</h2>
                    <div>
                        <p>ログイン</p>
                        <form action="/talk_room" method="POST">
                            <p>
                                ユーザーID:  <input type="text" name="client_id" defaultValue="0000000000" onKeyPress={this.handleInput} size="100" />
                            </p>
                            <p>
                                パスワード:    <input type="text" name="talk_id" onKeyPress={this.handleInput} size="100" />
                            </p>
                            <p>
                                <input type="submit" value="OK" />
                            </p>
                        </form>
                    </div>
                    <div>
                        <p>新規登録</p>
                        <form action="/talk_room" method="post">
                            <p>
                                ユーザーID:  <input type="text" name="client_id" value="0000000000" onKeyPress={this.handleInput} size="100" />
                            </p>
                            <p>
                                パスワード:    <input type="text" name="talk_id" onKeyPress={this.handleInput} size="100" />
                            </p>
                            <p>
                                <input type="submit" value="OK" />
                            </p>
                        </form>
                    </div>
                    <div>
                        <p>退会</p>
                        <form action="/talk_room" method="post">
                            <p>
                                ユーザーID:  <input type="text" name="client_id" value="0000000000" onKeyPress={this.handleInput} size="100" />
                            </p>
                            <p>
                                パスワード:    <input type="text" name="talk_id" onKeyPress={this.handleInput} size="100" />
                            </p>
                            <p>
                                <input type="submit" value="OK" />
                            </p>
                        </form>
                    </div>
               </div>
            );
        }
    }
);

ReactDOM.render(
    <TalkRoom />,
    document.getElementById('content')
);
