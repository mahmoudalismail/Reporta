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
      <div>
        <label for="email">Email</label>
        <input type="text" id="email" name="email" />
        <label for="name">Name</label>
        <input type="text" id="name" name="name" />
      </div>
    );
  }
});

console.log("going");
React.render(
  <App />,
  document.getElementById("main")
);
