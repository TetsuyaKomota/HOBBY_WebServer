var TalkRoom = React.createClass(
    {
        getInitialState : function(){
            return {
                talk_id        : "",
                last_input     : 9999999999999,
                delay          : 1000,
                login_message  : "",
                cu_message     : "",
                login_disabled : false,
                cu_disabled    : true
            };
        },

        componentDidMount : function(){
        },

        componentWillUnmount : function(){
        },

        handleLogin : function(e){
            var hashedPass = this.laundering(this.refs.login_user_name.value, this.refs.login_password.value);
            $.ajax({
                url: 'http://ec2-13-113-21-149.ap-northeast-1.compute.amazonaws.com:5000/api/hikari_login',
                type: 'POST',
                scriptCharset: 'UTF-8',
                data: {
                    'user_name' : this.refs.login_user_name.value,
                    'password'  : hashedPass
                },
                dataType: 'json', 
                cache: false,
            }).done(function(data){
                        this.refs.login_password.value = "";
                        if(data.result == true){
                            window.location.href = "/talk_room";
                        }
                        else{
                            this.setState({login_message:data.message});
                        }
                    }.bind(this))
        },


        handleCreateUser : function(e){
            this.setState({cu_disabled : true});
            var hashedPass = this.laundering(this.refs.cu_user_name.value, this.refs.cu_password.value);
            $.ajax({
                url: 'http://ec2-13-113-21-149.ap-northeast-1.compute.amazonaws.com:5000/api/hikari_create_user',
                type: 'POST',
                scriptCharset: 'UTF-8',
                data: {
                    'user_name' : this.refs.cu_user_name.value,
                    'password'  : hashedPass
                },
                dataType: 'json', 
                cache: false,
            }).done(function(data){
                        this.refs.cu_user_name.value = "";
                        this.refs.cu_password.value = "";
                        if(data.result == true){
                            this.setState({cu_message:"Successfully created new user! Please Login!"});
                        }
                        else{
                            this.setState({cu_message:data.message});
                        }
                    }.bind(this))
        },

        handleInput : function(e){
            var date = new Date();
            this.setState({last_input : date.getTime()});
            setTimeout(this.checkValidation, this.state.delay, this.refs.cu_user_name);
        },

        checkValidation : function(target){
            this.setState({cu_disabled : true});
            var date = new Date()
            if(date.getTime() - this.state.last_input < this.state.delay){
                return;
            }
                $.ajax({
                url: 'http://ec2-13-113-21-149.ap-northeast-1.compute.amazonaws.com:5000/api/hikari_user_validation',
                type: 'POST',
                scriptCharset: 'UTF-8',
                data: {
                    'user_name' : target.value
                },
                dataType: 'json', 
                cache: false,
            }).done(function(data){
                        this.setState({cu_message:data.message});
                        if(data.status == true){
                            this.setState({cu_disabled : false});
                            this.setState({cu_message:"OK!"});
                        }
                    }.bind(this))
        },

        hashing : function(plain){
            // jsSHA = require("jssha");
            var shaObj = new jsSHA("SHA-256", "TEXT", 1);
            shaObj.update(plain);
            return shaObj.getHash("HEX");
        },

        laundering : function(user_id, password){
            var hashedpass = this.hashing(password);
            for(var i=0;i<1000;i++){
                hashedpass = this.hashing(hashedpass + this.hashing(user_id) + this.hashing(this.hashing(user_id) + password));
            }
            return hashedpass;
        },

        render : function(){
/*                        <form action="/api/hikari_login" method="POST">
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
*/ 
            return (
                <div>
                    <h1>ひかりちゃんの部屋</h1>
                    <h2>エントランス</h2>
                    <div>
                        <h3>ログイン</h3>
                            <p>
                                ユーザーID:  <input ref="login_user_name" type="text" size="100" />
                                {this.state.login_message}
                            </p>
                            <p>
                                パスワード:    <input ref="login_password" type="password" size="100" />
                            </p>
                            <p>
                                <input type="button" value="ログイン" onClick={this.handleLogin} disabled={this.state.login_disabled}/>
                            </p>
                    </div>
                    <div>
                        <h3>新規登録</h3>
                        <p>万全を期してはいますが，セキュリティ知識一週間弱の人間の万全なので，</p>
                        <p>「いつも使ってるパスワード」の登録はやめてください</p>
                        <p>パスワードは空でも登録できます</p>
                        <p>
                            ユーザーID:  <input ref="cu_user_name" type="text" onChange={this.handleInput} size="100" />
                            {this.state.cu_message}
                        </p>
                        <p>
                            パスワード:    <input ref="cu_password" type="password" size="100" />
                        </p>
                        <p>
                            <input type="button" value="新規登録" onClick={this.handleCreateUser} disabled={this.state.cu_disabled}/>
                        </p>
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
