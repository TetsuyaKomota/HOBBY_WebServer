var BookInfo = React.createClass(
    {
        getInitialState : function(){

            var dd = new Date();

            var year = String(dd.getFullYear());
            var month = String(dd.getMonth()+1);
            if(month.length <= 1){
                month = '0' + month;
            }
            var date = String(dd.getDate());
            if(date.length <= 1){
                date = '0' + date;
            }

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
                currentDate : year + '-' + month + '-' + date,
                isbn : '',
                title : '',
                author : '',
                publisher : ''
            }
        },

        sendIsbn : function(e){
            
            if(e.key === 'Enter'){
                this.setState({
                    isbn : '',
                    title : '',
                    author : ''
                });
                let a = $.ajax({
                    url: 'http://ec2-13-113-21-149.ap-northeast-1.compute.amazonaws.com:5000/api/book_info',
                    Type: 'GET',
                    scriptCharset: 'UTF-8',
                    data: {'isbn' : e.target.value},
                    dataType: 'json', 
                    cache: false,
                })
                a.done(function(data){
                    this.setState({
                        pressed : data.bodydata,
                        isbn : data.isbn,
                        title : data.title,
                        author : data.author
                    });
                    console.log(this.state);
                    this.generateTemplate();
                    if(
                        this.state.isbn != '' &&
                        this.state.title != '' &&
                        this.state.author != '' 
                    ){
                        // this.insertToDB();
                    }
                    else{
                        console.log("something wrong...");
                    }

                }.bind(this)).fail(function(XMLHttpRequest, textStatus, errorThrown){
                    console.log("-1:"+XMLHttpRequest.status);
                    console.log("-2:"+textStatus);
                    console.log("-3:"+errorThrown);
                });
                e.target.value = '';
            }
        },

        insertToDB : function() {
                 $.ajax({
                    url: 'http://13.113.169.250:5000/api/book_insert',
                    Type: 'GET',
                    scriptCharset: 'UTF-8',
                    data: {
                        'isbn' : this.state.isbn,
                        'title' : this.state.title,
                        'author' : this.state.author
                    },
                    dataType: 'json', 
                    cache: false
                }).fail(function(XMLHttpRequest, textStatus, errorThrown){
                    console.log("-4:"+XMLHttpRequest.status);
                    console.log("-5:"+textStatus);
                    console.log("-6:"+errorThrown);
                });

            
        },

        handleChange : function(e){
            console.log("handleChange は動いてるよ");
            console.log(e.target.name + ", "+e.target.value);
            if(e.key === 'Enter'){
                    if(e.target.name === 'isbn'){
                        this.setState({isbn : e.target.value});
                    }
                    else if(e.target.name === 'title'){
                        this.setState({title : e.target.value});
                    }
                    else if(e.target.name === 'author'){
                        this.setState({author : e.target.value});
                    }
                    else if(e.target.name === 'publisher'){
                        this.setState({publisher : e.target.value});
                    }
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

        manualGenerate : function(){
        
            let template = '&amazon('+this.refs.isbn.value+'){large}\n'
                + '*基本情報\n'
                + '{| width="500px" class="custom-css" style="color:#6e7955"\n'
                + '|タイトル|'+this.refs.title.value+'|\n' 
                + '|作者名|'+this.refs.author.value+'|\n'
                + '|巻数||\n'
                + '|出版社|'+this.refs.publisher.value+'|\n'
                + '|部室に追加した人|'+'|\n'
                + '|最終更新者|'+'|\n'
                + '|編集日|' + this.state.currentDate + '|\n'
                + '|}';
            
            var temp = template.split('\n');
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

            $.ajax({
                url: 'http://13.113.169.250:5000/api/book_insert',
                Type: 'GET',
                scriptCharset: 'UTF-8',
                data: {
                    'isbn' : this.refs.isbn.value,
                    'title' : this.refs.title.value,
                    'author' : this.refs.author.value
                },
                dataType: 'json', 
                cache: false
            }).fail(function(XMLHttpRequest, textStatus, errorThrown){
                console.log("-7:"+XMLHttpRequest.status);
                console.log("-8:"+textStatus);
                console.log("-9:"+errorThrown);
            });



        },

        render : function(){
            return (
                <div>
                    <p>
                        AUTO_ISBN
                        <input type='text' value={this.inputisbn} onKeyPress={this.sendIsbn} />
                    </p>
                        登録されていない場合は，ここに入力してください(まだ何も起こらないので無視してください)
                    <p>
                        ISBN
                        <input type='text' ref="isbn" name='isbn' value={this.isbn} onKeyPress={this.handleChange} />
                    </p>
                    <p>
                        タイトル
                        <input type='text' ref="title" name='title' value={this.title} onKeyPress={this.handleChange} />
                    </p>
                    <p>
                        作者
                        <input type='text' ref="author" name='author' value={this.author} onKeyPress={this.handleChange} />
                    </p>
                    <p>
                        出版社
                        <input type='text' ref="publisher" name='publisher' value={this.publisher} onKeyPress={this.handleChange} />
                    </p>
                    <input type='button' value="手動追加" onClick={this.manualGenerate}/>

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
