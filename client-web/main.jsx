var App = React.createClass({
  render: function() {
    return(
      <div id="app">
        <Login />
      </div>
    );
  }
});

var Login = React.createClass({
  render: function() {
    return (
      <div id="login">
        <h1>Login</h1>
        <form class="pure-form">
          <fieldset class="pure-group">
              <input type="text" class="pure-input-1-2" placeholder="Email">
          </fieldset>

          <button type="submit" class="pure-button pure-input-1-2 pure-button-primary">Login</button>
        </form>

        <h1>Register</h1>
        <form class="pure-form">
          <fieldset class="pure-group">
              <input type="text" class="pure-input-1-2" placeholder="Email">
              <input type="text" class="pure-input-1-2" placeholder="Name">
          </fieldset>

          <button type="submit" class="pure-button pure-input-1-2 pure-button-primary">Register</button>
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
