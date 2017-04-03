var HelloWorld = React.createClass({
    render : function() {
        return React.createElement(
                'h2',
                {
                    style:{
                        fontStyle:'oblique',
                        fontFamily:'Arial',
                        color:'green'
                    }
                },
                'Hello ' + this.props.name + ' World!!'
        );
    }
});

var Evaluate = React.createClass(
    {
        render : function(){
            return React.createElement(
                'h2',
                 null,
                 eval(this.props.text)
            )
        }
    }
);

var Calclator = React.createClass(
    {
        getInitialState : function(){
            return {
                expression : ''
            };
        },
        reCalcValue : function(e){
            if(true)
                this.setState(
                    {
                        expression : e.target.value
                    }
                );
        },
        render : function(){
            return React.DOM.div(
                null,
                React.createElement(
                    'input',
                    {
                        type : 'text',
                        onKeyPress : this.reCalcValue
                    }
                ),
                React.createElement(
                    'h2',
                    null,
                    eval(this.state.expression)
                )
            );
/*
            return (
                <div>
                    <input type='text' onKeyPress={this.reCalcValue} />
                    <h2>{eval(this.state.expression)}</h2>
                </div>
            );
*/
        }
    }
);

ReactDOM.render(
//    React.createElement(HelloWorld, {name : 'komota'}),
//    React.createElement(Evaluate, {text : '10/2'}),
    React.createElement(Calclator),
//    <Calclator />
    document.getElementById('content')


);
