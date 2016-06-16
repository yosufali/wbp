var React = require('react');
var ReactRouter = require('react-router');
var Link = ReactRouter.Link;

var ProfilePage = React.createClass({
	render: function() {
		return (
			<div>
				<h1> Profile </h1>
				<p> This is my profile </p>
				<ul>
					<li> <Link to="/modules/"> Modules List </Link> </li>
				</ul>
			</div>
		);
	}
});

module.exports = ProfilePage;