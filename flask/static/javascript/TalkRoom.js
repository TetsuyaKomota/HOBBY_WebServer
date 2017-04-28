var TalkRoom = React.createClass(
    {
        getInitialState : function(){
            return {
                face        : "normal",
                image_src   : "/static/images/talkRoom/TalkAI_graphics_normal.png",
                response    : "こんにちは．",
                idx         : ""
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
                // url: 'http://13.113.169.250:5000/api/hikari_change_state',
                url: 'http://ec2-13-113-169-250.ap-northeast-1.compute.amazonaws.com:5000/api/hikari_start_conversation',
                Type: 'GET',
                scriptCharset: 'UTF-8',
                data: {},
                dataType: 'json', 
                cache: false,
            }).done(function(data){
                this.setState({idx : data.new_idx})
            }.bind(this));
        },

        deleteAgent : function(){

            $.ajax({
                // url: 'http://13.113.169.250:5000/api/hikari_change_state',
                url: 'http://ec2-13-113-169-250.ap-northeast-1.compute.amazonaws.com:5000/api/hikari_end_conversation',
                Type: 'GET',
                scriptCharset: 'UTF-8',
                data: {'idx' : this.state.idx},
                dataType: 'json', 
                cache: false,
            }).done(function(data){
                console.log(data.num_of_talk); 
            }.bind(this));
        },


        changeState : function(){

            $.ajax({
                // url: 'http://13.113.169.250:5000/api/hikari_change_state',
                url: 'http://ec2-13-113-169-250.ap-northeast-1.compute.amazonaws.com:5000/api/hikari_change_state',
                Type: 'GET',
                scriptCharset: 'UTF-8',
                data: {
                    'query' : '今はこの入力に意味ないよ！',
                    'idx'   : this.state.idx
                },
                dataType: 'json', 
                cache: false,
            }).done(function(data){
                this.setState({image_src : "/static/images/talkRoom/TalkAI_graphics_"+data.state+".png"})
            }.bind(this));
        },

        talk : function(){
            $.ajax({
                // url: 'http://13.113.169.250:5000/api/hikari_talk',
                url: 'http://ec2-13-113-169-250.ap-northeast-1.compute.amazonaws.com:5000/api/hikari_talk',
                Type: 'GET',
                scriptCharset: 'UTF-8',
                data: {
                    'query' : this.refs.query.value,
                    'idx'   : this.state.idx
                },
                dataType: 'json', 
                cache: false,
            }).done(function(data){
                this.setState({response : data.response});
            }.bind(this));
        },

        handleClick : function(){
            this.changeState();
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
