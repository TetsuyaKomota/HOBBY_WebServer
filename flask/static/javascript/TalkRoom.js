var TalkRoom = React.createClass(
    {
        getInitialState : function(){
            return {
                face        : "normal",
                image_src   : "/static/images/talkRoom/TalkAI_graphics_normal.png",
                response    : "こんにちは．",
                user_id     : "0000",
                talk_id     : "",
                lock_flg    : false,
            };
        },

        componentDidMount : function(){
            this.createAgent();
            // login 情報を切り出してくる
            this.setState({user_id : document.cookie.split("login=")[1].split(";")[0]});
        },

        componentWillUnmount : function(){
            this.deleteAgent();
        },

        createAgent : function(){
            $.ajax({
                url: 'http://ec2-13-113-169-250.ap-northeast-1.compute.amazonaws.com:5000/api/hikari_start_conversation',
                Type: 'GET',
                scriptCharset: 'UTF-8',
                data: {
                    'user_id' : this.state.user_id
                },
                dataType: 'json', 
                cache: false,
            }).done(function(data){
                this.setState({talk_id : data.talk_id});
                this.setState({response : data.response});
            }.bind(this));
        },

        deleteAgent : function(){
            $.ajax({
                url: 'http://ec2-13-113-169-250.ap-northeast-1.compute.amazonaws.com:5000/api/hikari_end_conversation',
                Type: 'GET',
                scriptCharset: 'UTF-8',
                data: {
                    'user_id' : this.state.user_id,
                    'talk_id' : this.state.talk_id
                },
                dataType: 'json', 
                cache: false,
            }).done(function(data){
                console.log(data.num_of_talk); 
            }.bind(this));
        },

        talk : function(){
            $.ajax({
                url: 'http://ec2-13-113-169-250.ap-northeast-1.compute.amazonaws.com:5000/api/hikari_talk',
                Type: 'GET',
                scriptCharset: 'UTF-8',
                data: {
                    'query' : this.refs.query.value,
                    'talk_id'   : this.state.talk_id,
                    'user_id'   : this.state.user_id
                },
                dataType: 'json', 
                cache: false,
            }).done(function(data){
                this.setState({response : data.response});
                this.setState({image_src : "/static/images/talkRoom/TalkAI_graphics_"+data.state+".png"});
                this.setState({lock_flg : false})
            }.bind(this));
        },

        handleKeyPress : function(e){
            if(this.state.lock_flg == true){
                return
            }
            else if(e.key==="Enter"){
                this.setState({lock_flg : true});
                this.addLog("ひかり &gt; " + this.state.response);
                this.addLog(this.refs.query.value);
                this.talk();
                this.refs.query.value = "";
            }
        },
        
        addLog : function(text) {
            document.getElementById('holder').innerHTML = '<p>' + text + '</p>\n' + document.getElementById('holder').innerHTML;
        },

        render : function(){
            return (
                <div>
                    <h1>ひかりちゃんの部屋</h1>
                    <div style={{display:"inline-block"}}>
                        <img src={this.state.image_src} />
                    </div>
                    <div style={{display:"inline-block"}}>
                        <input ref="query" type="text" size="100" onKeyPress={this.handleKeyPress} />
                        <p>{this.state.response}</p>
                        <div id="holder">
                        </div>
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
