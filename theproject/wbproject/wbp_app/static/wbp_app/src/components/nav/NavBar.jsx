var React = require('react');
var NavItem = require(('./NavItem.jsx'));
var ReactRouter = require('react-router');
var Link = ReactRouter.Link;

var NavBar = React.createClass({
	render: function() {

		var navStyle = {
			WebkitBoxShadow: "0 0 4px egba(0,0,0,0.4)",
			MozBoxShadow: "0 0 4px rgba(0,0,0,0.4)",
			boxShadow: "0 0 4px rgba(0,0,0,0.4)",
			borderRadius: 0
		};

		var titleStyle = {};
		var linkStyle = {};

		if (this.props.bgColor) {
			navStyle.background = this.props.bgColor;
		};

		if (this.props.titleColor) {
			titleStyle.color = this.props.titleColor;
		};

		if (this.props.linkColor) {
			linkStyle.color = this.props.linkColor;
		};

		// TODO: Pull the logout button to the right 

		var createLinkItem = function(item, index) {
			return <NavItem aStyle={linkStyle} key={item.title + index} href={item.href} float={item.float} title={item.title} />;
		};

		return (
			<div>
				<nav style={navStyle} className="navbar navbar-default">
					<div className="navbar-header">
						<button type="button" className="navbar-toggle collapsed" data-toggle="collapse" data-target="#nav-collapse">
							<span className="icon-bar"> </span>
							<span className="icon-bar"> </span>
							<span className="icon-bar"> </span>
						</button>
						<Link style={titleStyle} className="navbar-brand" to="/profile/"> City CS Administration </Link>
					</div>

					<div className="collapse navbar-collapse" id="nav-collapse">
						<ul className="nav navbar-nav">
							{this.props.navData.map(createLinkItem)}
						</ul>
					</div>
				</nav>
			</div>
		);
	}
});

module.exports = NavBar;