var ColoredButton = React.createClass({

    render : function(){
        return (
            <button {...this.props} />
        );
    }

});


ReactDOM.render(
    <ColoredButton 
        style={{
            color : '#A04020', 
            backgroundColor : '#90C0A0',
            fontFamily : "Serif",
            fontSize : 22
        }}
        type='button'
        disabled={false}
    >
        Check Me!!
    </ColoredButton>,
    document.getElementById('button')
);
