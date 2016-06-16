var React = require('react');
var ReactRouter = require('react-router');
var Link = ReactRouter.Link;
var UsernameField = require('./UsernameField.jsx');
var PasswordField = require('./PasswordField.jsx');

var Reflux = require('reflux');
var Actions = require('../reflux/Actions.jsx');
var LoginStore = require('../reflux/LoginStore.jsx');

var LoginPage = React.createClass({

	mixins:[Reflux.listenTo(LoginStore, 'onLogin')],

	onLogin: function(msg) {
		console.log(msg);
		alert(msg);
	},

	getInitialState: function() {
		return {username: "", password: ""};
	},


	login: function(e) {
		e.preventDefault();
		console.log(e);
		alert(e);

		var user = {
			username: this.refs.fieldUsername.state.value,
			password: this.refs.fieldPassword.state.value
		};

		console.log(user);
		alert(user);
		Actions.login(user);

		// Auth.login(this.state.username, this.state.password)
		// .catch(function(err){
		// 	console.log("Error logging in ", err);
		// });
	},

	render: function() {
		return (
			<div className="row">
				<div className="col-sm-6 col-sm-offset-3">
					<div className="panel panel-default">
						<div className="panel-heading"> Log In </div>
						<div className="panel-body">
							<form role="form">
								<div className="form-group">
									<UsernameField ref="fieldUsername" type="User" />
									<br />
									<PasswordField ref="fieldPassword" type="Password" />
								</div>
								<button className="btn btn-primary" type="submit" onClick={this.login}> Log In </button>
							</form>
						</div>
					</div>
					<Link to="/profile/"> Profile </Link>
				</div>
			</div>
		);
	}
});

module.exports = LoginPage;