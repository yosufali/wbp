var React = require('react');
var ReactRouter = require('react-router');
var Link = ReactRouter.Link;

var ModulesPage = React.createClass({
	render: function() {
		return (
			<div>
				<h1> Modules </h1>
				<ul>
					<li> This is a list of modules </li>
					<li> <Link to="/modules/55"> Module 55 </Link> </li>
					<li> <Link to="/modules/67"> Module 67 </Link> </li>
				</ul>
			</div>
		);
	}
});

module.exports = ModulesPage;