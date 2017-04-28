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

        handleInput : function(){
            console.log("inputed.");
        },

        render : function(){
            return (
                <div>
                    <h1>ひかりちゃんの部屋</h1>
                    <h2>エントランス</h2>
                    <div>
                        <p>ログイン</p>
                        <form action="/" method="post">
                            <p>
                                ユーザーID:  <input type="text" name="client_id" value="0000000000" onChange={this.handleInput} size="100" />
                            </p>
                            <p>
                                パスワード:    <input type="text" name="talk_id" onChange={this.handleInput} size="100" />
                            </p>
                            <p>
                                <input type="submit" value="OK" />
                            </p>
                        </form>
                    </div>
                    <div>
                        <p>新規登録</p>
                        <form action="/" method="post">
                            <p>
                                ユーザーID:  <input type="text" name="client_id" value="0000000000" onChange={this.handleInput} size="100" />
                            </p>
                            <p>
                                パスワード:    <input type="text" name="talk_id" onChange={this.handleInput} size="100" />
                            </p>
                            <p>
                                <input type="submit" value="OK" />
                            </p>
                        </form>
                    </div>
                    <div>
                        <p>退会</p>
                        <form action="/" method="post">
                            <p>
                                ユーザーID:  <input type="text" name="client_id" value="0000000000" onChange={this.handleInput} size="100" />
                            </p>
                            <p>
                                パスワード:    <input type="text" name="talk_id" onChange={this.handleInput} size="100" />
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
