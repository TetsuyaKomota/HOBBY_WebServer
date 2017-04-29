var TalkRoom = React.createClass(
    {
        getInitialState : function(){
            return {
                talk_id     : "",
                last_input  : 9999999999999,
                delay       : 1000
            };
        },

        componentDidMount : function(){
        },

        componentWillUnmount : function(){
        },

        handleInput : function(e){
            var date = new Date();
            this.setState({last_input : date.getTime()});
            setTimeout(this.checkValidation, this.state.delay, e.target);
        },

        checkValidation : function(target){
            var date = new Date()
            if(date.getTime() - this.state.last_input < this.state.delay){
                return;
            }
                $.ajax({
                url: 'http://ec2-13-113-169-250.ap-northeast-1.compute.amazonaws.com:5000/api/hikari_user_validation',
                type: 'POST',
                scriptCharset: 'UTF-8',
                data: {
                    'user_name' : target.value
                },
                dataType: 'json', 
                cache: false,
            })
        },

        render : function(){
            return (
                <div>
                    <h1>ひかりちゃんの部屋</h1>
                    <h2>エントランス</h2>
                    <div>
                        <p>ログイン</p>
                        <form action="/talk_room" method="GET">
                            <p>
                                ユーザーID:  <input type="text" name="client_id" onKeyPress={this.handleInput} size="100" />
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
                        <form action="/talk_room" method="GET">
                            <p>
                                ユーザーID:  <input type="text" name="client_id" onKeyPress={this.handleInput} size="100" />
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
                        <form action="/talk_room" method="GET">
                            <p>
                                ユーザーID:  <input type="text" name="client_id" onKeyPress={this.handleInput} size="100" />
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
