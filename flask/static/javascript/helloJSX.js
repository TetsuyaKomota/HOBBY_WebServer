var Hello = React.createClass({
    render : function(){
        return (
            <h2 
                style={{
                    fontStyle : 'oblique', 
                    fontFamily : 'Arial', 
                    color : this.props.value >= 0 ? 'green' : 'red'
                }}
            >
                <p>Hello, JSX World!!!</p>
                <p>The number is {this.props.value}</p>
            </h2>
        );
    }
});

ReactDOM.render(
    <Hello value={Math.floor(Math.random() * 20) - 10} />,
    document.getElementById('hello')
);
