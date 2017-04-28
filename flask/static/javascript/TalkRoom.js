var TalkRoom = React.createClass(
    {
        getInitialState : function(){
            return {
                face        : "normal",
                image_src   : "/static/images/talkRoom/TalkAI_graphics_normal.png",
                response    : "こんにちは．",
                user_id     : "0000",
                talk_id     : ""
            };
        },

        componentDidMount : function(){
            this.createAgent();
            // this.changeState(this.state.face);
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


        changeState : function(){

            $.ajax({
                url: 'http://ec2-13-113-169-250.ap-northeast-1.compute.amazonaws.com:5000/api/hikari_change_state',
                Type: 'GET',
                scriptCharset: 'UTF-8',
                data: {
                    'query' : '今はこの入力に意味ないよ！',
                    'talk_id'   : this.state.talk_id
                },
                dataType: 'json', 
                cache: false,
            }).done(function(data){
                this.setState({image_src : "/static/images/talkRoom/TalkAI_graphics_"+data.state+".png"})
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
            }.bind(this));
        },

        handleClick : function(){
            // this.changeState();
            this.talk();
        },

        render : function(){
            return (
                <div>
                    <h1>ひかりちゃんの部屋</h1>
                    <div style={{display:"inline-block"}}>
                        <img src={this.state.image_src} />
                    </div>
                    <div style={{display:"inline-block"}}>
                        <p>{this.state.response}</p>
                        <input ref="query" type="button" value="なんか喋って" onClick={this.handleClick} />                
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
