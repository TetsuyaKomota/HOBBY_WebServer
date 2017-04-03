var BookInfo = React.createClass(
    {
        getInitialState : function(){
            return {
                inputisbn : '',
                pressed : '',
                splited_0  : '-',
                splited_1  : '-',
                splited_2  : '-',
                splited_3  : '-',
                splited_4  : '-',
                splited_5  : '-',
                splited_6  : '-',
                splited_7  : '-',
                splited_8  : '-',
                splited_9  : '-',
                splited_10 : '-',
                title : '',
                author : '',
                publisher : ''
            }
        },

        sendIsbn : function(e){
            
            if(e.key === 'Enter'){
                let a = $.ajax({
                    url: 'http://13.113.169.250:5000/api/book_info',
                    Type: 'GET',
                    scriptCharset: 'UTF-8',
                    data: {'isbn' : e.target.value},
                    dataType: 'json', 
                    cache: false,
                    complete: function(data) {
                        console.log(data);
                    }
                })
                a.done(function(data){
                    console.log(data.bodydata);
                    this.setState({pressed : data.bodydata});
                    this.generateTemplate();
                }.bind(this)).fail(function(XMLHttpRequest, textStatus, errorThrown){
                    console.log("-1:"+XMLHttpRequest.status);
                    console.log("-2:"+textStatus);
                    console.log("-3:"+errorThrown);
                });
                e.target.value = '';
            }
        },

        handleChange : function(e, key){
            if(key === 'title'){
                this.setState({title : e.target.value});
                e.target.value = this.state.title;
            }
            else if(key === 'author'){
                this.setState({author : e.target.value});
                e.target.value = this.state.author;
            }
            else if(key === 'publisher'){
                this.setState({publisher : e.target.value});
                e.target.value = this.state.publisher;
            }
        },

        generateTemplate : function(){

            var temp = this.state.pressed.split('\n');
            this.setState({
                splited_0 : temp[0],
                splited_1 : temp[1],
                splited_2 : temp[2],
                splited_3 : temp[3],
                splited_4 : temp[4],
                splited_5 : temp[5],
                splited_6 : temp[6],
                splited_7 : temp[7],
                splited_8 : temp[8],
                splited_9 : temp[9],
                splited_10 : temp[10],
            });

        },

        render : function(){
            return (
                <div>
                    <p>
                        ISBN
                        <input type='text' value={this.inputisbn} onKeyPress={this.sendIsbn} />
                    </p>
                        登録されていない場合は，ここに入力してください(まだ何も起こらないので無視してください)
                    <p>
                        タイトル
                        <input type='text' value={this.title} onKeyPress={this.handleChange('title')} />
                    </p>
                    <p>
                        作者
                        <input type='text' value={this.author} onKeyPress={this.handleChange('author')} />
                    </p>
                    <p>
                        出版社
                        <input type='text' value={this.publisher} onKeyPress={this.handleChange('publisher')} />
                    </p>
                    <input type='button' value="追加" />
                 
                    <h2>{this.state.splited_0}</h2>
                    <h2>{this.state.splited_1}</h2>
                    <h2>{this.state.splited_2}</h2>
                    <h2>{this.state.splited_3}</h2>
                    <h2>{this.state.splited_4}</h2>
                    <h2>{this.state.splited_5}</h2>
                    <h2>{this.state.splited_6}</h2>
                    <h2>{this.state.splited_7}</h2>
                    <h2>{this.state.splited_8}</h2>
                    <h2>{this.state.splited_9}</h2>
                    <h2>{this.state.splited_10}</h2>
                </div>
            );
        }
    }
);

ReactDOM.render(
    <BookInfo />,
    document.getElementById('content')
);
