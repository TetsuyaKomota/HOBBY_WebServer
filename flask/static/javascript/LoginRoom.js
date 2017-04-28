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

        render : function(){
            return (
                <div>
                    <h1>ひかりちゃんの部屋</h1>
                    <h2>エントランス</h2>
                </div>
            );
        }
    }
);

ReactDOM.render(
    <TalkRoom />,
    document.getElementById('content')
);
