var App = React.createClass({
  getInitialState: function() {
    return {
      id: localStorage.id,
      name: localStorage.name
    };
  },
  render: function() {
    return(
      <div id="app">
        <h1>Reporta</h1>
        {
          this.state.id ?
          <Timeline _id={this.id} name={this.state.name} app={this} /> :
          <Login app={this} />
        }
      </div>
    );
  }
});

var Timeline = React.createClass({
  logout: function() {
    delete localStorage.id;
    delete localStorage.name;
    this.props.app.setState({
      id: null,
      name: null
    });
  },
  render: function() {
    return(
      <div id="timeline">
        <h1>
          The Timeline
        </h1>
        <a href="#" onClick={this.logout}>Logout</a>
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
          console.log("Error");
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
          console.log("Error");
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

console.log("going");
React.render(
  <App />,
  document.getElementById("main")
);
