var TalkRoom = React.createClass(
    {
        getInitialState : function(){
            return {
                face        : "normal",
                image_src   : "",
                talk        : "やっほー"
            };
        },

        componentDidMount : function(){
            this.changeFace(this.state.face);
        },

        changeFace : function(input){
            this.setState({image_src : "/static/images/talkRoom/TalkAI_graphics_"+input+".png"})
        },

        talk : function(){
            $.ajax({
                url: 'http://13.113.169.250:5000/api/hikari_talk',
                Type: 'GET',
                scriptCharset: 'UTF-8',
                data: {},
                dataType: 'json', 
                cache: false,
            }).done(function(data){
                this.setState({talk : data.talk});
            }.bind(this));
        },

        handleClick : function(){
            console.log("やっほー");
            this.changeFace("happy");
            this.talk();
        },

        render : function(){
            return (
                <div>
                    <h1>Hello TalkRoom_React</h1>
                    <div style={{display:"inline-block"}}>
                        <img src={this.state.image_src} />
                    </div>
                    <div style={{display:"inline-block"}}>
                        <p>{this.state.talk}</p>
                        <input type="button" value="なんか喋って" onClick={this.handleClick} />                
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
