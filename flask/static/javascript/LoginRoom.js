var TalkRoom = React.createClass(
    {
        getInitialState : function(){
            return {
                talk_id     : "",
                last_input  : 9999999999999,
                delay       : 1000,
                cu_message     : ""
            };
        },

        componentDidMount : function(){
        },

        componentWillUnmount : function(){
        },

        handleInput : function(e){
            var date = new Date();
            this.setState({last_input : date.getTime()});
            setTimeout(this.checkValidation, this.state.delay, this.refs.cu_user_name);
        },

        checkValidation : function(target){

            console.log(this.hashing("hogehoge"));
            
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
            }).done(function(data){this.setState({cu_message:data.message})}.bind(this))
        },

        hashing : function(plain){
            jsSHA = require("jssha");
            var shaObj = new jsSHA("SHA-256", "TEXT", 1);
            shaObj.update(plain);
            return shaObj.getHash("HEX");
        },

        render : function(){
            return (
                <div>
                    <h1>ひかりちゃんの部屋</h1>
                    <h2>エントランス</h2>
                    <div>
                        <p>ログイン</p>
                        <form action="/api/hikari_login" method="POST">
                            <p>
                                ユーザーID:  <input type="text" name="user_name" size="100" />
                            </p>
                            <p>
                                パスワード:    <input type="password" name="password" size="100" />
                            </p>
                            <p>
                                <input type="submit" value="OK" />
                            </p>
                        </form>
                    </div>
                    <div>
                        <p>新規登録</p>
                        <p>注意！！</p>
                        <p>現在パスワードは超気休めです！わかりやすく言うとPOST データ見れば簡単に覗けます！</p>
                        <p>ハッシュ化すらしてません！生のままです！パスワードとは？</p>
                        <p>「いつも使ってるパスワード」とかの入力は絶対にやめてください！</p>
                        <p>パスワードは空でも登録できます！</p>
                        <form action="/api/hikari_create_user" method="POST">
                            <p>
                                ユーザーID:  <input ref="cu_user_name" type="text" name="user_name" onChange={this.handleInput} size="100" />
                                {this.state.cu_message}
                            </p>
                            <p>
                                パスワード:    <input type="password" name="password" size="100" />
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
