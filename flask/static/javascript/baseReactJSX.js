var Calclator = React.createClass(
    {
        getInitialState : function(){
            return {
                expression : ''
            };
        },
        reCalcValue : function(e){
            if(e.key === 'Enter')
                this.setState(
                    {
                        expression : e.target.value
                    }
                );
        },
        render : function(){
            return (
                <div>
                    <input type='text' onKeyPress={this.reCalcValue} />
                    <h2>{eval(this.state.expression)}</h2>
                </div>
            );
        }
    }
);

ReactDOM.render(
    <Calclator />,
    document.getElementById('content')
);
