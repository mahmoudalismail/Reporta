var cx = React.addons.classSet;
var ReactCSSTransitionGroup = React.addons.CSSTransitionGroup;

var canSynthesizeSpeech = ('speechSynthesis' in window);

var speechQueue = [];
var tts = function(text) {
  console.log("speaking");
  if (canSynthesizeSpeech) {
    console.log("native");
    var msg = new SpeechSynthesisUtterance(text);
    window.speechSynthesis.speak(msg);
  }
};

var App = React.createClass({
  getInitialState: function() {
    if (!localStorage.id) {
      tts("Hi, My name is Reporta.");
    } else {
      tts("Good to see you again " + localStorage.name);
    }
    return {
      id: localStorage.id,
      name: localStorage.name
    };
  },
  render: function() {
    return(
      <div id="app">
        {
          this.state.id ?
          <Timeline _id={this.state.id} name={this.state.name} app={this} /> :
          <Login app={this} />
        }
      </div>
    );
  }
});

var Timeline = React.createClass({
  mixins: [ReactFireMixin],
  getInitialState: function() {
    return {
      memory: null
    };
  },
  componentWillMount: function() {
    var self = this;
    this.isLoaded = false;
    this.firebaseRef = new Firebase("https://reporta-ajz.firebaseio.com/" + this.props._id);
    this.bindAsArray(this.firebaseRef, "memory");
    this.firebaseRef.on("child_added", function(new_child) {
      console.log("new data");
      var data = new_child.val();
      console.log(data);
      if (data.type == "reporta" && self.isLoaded) {
        tts(data.value);
      }

    });
  },
  eraseMemory: function() {
    this.firebaseRef.remove();
  },
  logout: function() {
    delete localStorage.id;
    delete localStorage.name;
    this.props.app.setState({
      id: null,
      name: null
    });
  },
  render: function() {
    var superNode;
    if (this.state.memory) {
      var reverse_history = this.state.memory.slice().reverse();
      var history_length = reverse_history.length;
      var nodes = _.map(reverse_history, function(memento, i) {
        var index = history_length - i - 1;
        switch(memento.type) {
          case "user":
            return <Speech key={index} role="user" text={memento.value} />;
          case "reporta":
            return <Speech key={index} role="reporta" text={memento.value} />;
          case "article":
            return <Article key={index} articles={memento.value} />;
          case "media":
            return <Media key={index} image={memento.value} />;
          default:
            return <div key={index}>Not yet supported</div>;
        }
      });
      this.isLoaded = true;
      superNode = (
        <div key="timeline">
          <form className="pure-form">
            <input className="pure-input-1" type="text" placeholder="Ask me a question!" />
          </form>
          <ReactCSSTransitionGroup transitionName="memory">
            {nodes}
          </ReactCSSTransitionGroup>
          <a href="#" onClick={this.logout}>Logout</a><br/>
          <a href="#" onClick={this.eraseMemory}>Clear</a>
        </div>
      );
    } else {
      superNode = (
        <h1 key="loading">
          I'm Coming {this.props.name}
        </h1>
      );
    }
    return (
      <div id="timeline">
        <ReactCSSTransitionGroup transitionName="timeline">
          {superNode}
        </ReactCSSTransitionGroup>
      </div>
    );
  }
});

var Speech = React.createClass({
  render: function() {
    var classes = cx({
      "speech": true,
      "user-speech": this.props.role == "user",
      "reporta-speech": this.props.role != "user"
    });
    return (
      <div className={classes}>
        {this.props.text}
      </div>
    );
  }
});

var Media = React.createClass({
  render: function() {
    return (
      <div className="media">
        <img src={this.props.image} />
      </div>
    );
  }
});

var Article = React.createClass({
  render: function() {
    var articleNode = null;
    if (this.props.articles.length > 1) {
      articleNode = _.map(this.props.articles, function(article) {
        return (
          <h2>
              <a href={article.url}>
                {article.headline}
              </a>
              <hr />
          </h2>
        );
      });
    } else if (this.props.articles.length == 1) {
      articleNode = (
        <div>
          <h2>
            <a href={article.url}>
              {article.headline}
            </a>
            <hr />
          </h2>
          {article.snippet}
        </div>
      );
    }
    return (
      <div className="articles">
        {articleNode}
      </div>
    );
  }
});

var Loading = React.createClass({
  render: function() {
    return(
      <div id="loading">
        <h1>
          Loading
        </h1>
      </div>
    );
  }
});

var Login = React.createClass({
  getInitialState: function() {
    return {
      message: ""
    };
  },
  handleLogin: function(e) {
    e.preventDefault();
    var id = this.refs.loginEmail.getDOMNode().value;
    var self = this;
    $.ajax({
      type: "POST",
      url: "/login",
      data: JSON.stringify({
        id: id,
      }),
      success: function(data) {
        if (data.status == 200) {
          localStorage.id = data.id;
          localStorage.name = data.name;
          self.props.app.setState({
            id: localStorage.id,
            name: localStorage.name
          });
        } else {
          self.setState({
            message: "Error logging in"
          });
        }
      },
      dataType: "json"
    });
    this.setState({
      message: "Logging in..."
    });
  },
  handleRegister: function(e) {
    e.preventDefault();
    var self = this;
    var id = self.refs.registerEmail.getDOMNode().value;
    var name = self.refs.registerName.getDOMNode().value;
    $.ajax({
    type: "POST",
      url: "/register",
      data: JSON.stringify({
        id: id,
        name: name
      }),
      success: function(data) {
        if (data.status == 200) {
          localStorage.id = id;
          localStorage.name = name;
          self.props.app.setState({
            id: localStorage.id,
            name: localStorage.name
          });
        } else {
          self.setState({
            message: "Error registering"
          });
        }
      },
      dataType: "json"
    });
    this.setState({
      message: "Registering..."
    });
  },
  render: function() {
    return (
      <div id="login">
        <h1>Login</h1>
        <div>{this.state.message}</div>
        <form className="pure-form" onSubmit={this.handleLogin}>
          <fieldset className="pure-group">
              <input type="text" className="pure-input-1-2" placeholder="Email" ref="loginEmail" />
          </fieldset>

          <button type="submit" className="pure-button pure-input-1-2 pure-button-primary">Login</button>
        </form>

        <h1>Register</h1>
        <form className="pure-form" onSubmit={this.handleRegister}>
          <fieldset className="pure-group">
              <input type="text" className="pure-input-1-2" placeholder="Email" ref="registerEmail" />
              <input type="text" className="pure-input-1-2" placeholder="Name" ref="registerName" />
          </fieldset>

          <button type="submit" className="pure-button pure-input-1-2 pure-button-primary">Register</button>
        </form>
      </div>
    );
  }
});

React.render(
  <App />,
  document.getElementById("main")
);
