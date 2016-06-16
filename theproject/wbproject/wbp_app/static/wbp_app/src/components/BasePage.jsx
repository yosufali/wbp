var React = require('react');
var NavBar = require('./nav/NavBar.jsx');

var navLinks = [
	{
		title: "Profile",
		href: "/profile/"
	},
	{
		title: "My Modules",
		href: "/modules/"
	},
	// Pages: Notifications, LoggedIn name, Settings, 
	{
		title: "Log Out",
		href: "#",
		float: 'right'
	}
];

var BasePage = React.createClass({
	render: function() {
		var style = {
			paddingTop: 20
		};
		
		return (
			<div>
				<NavBar bgColor="white" titleColor="Red" linkColor="" navData={navLinks} />
				<div className="container" styl="style">
					<div className="row">
						<div className="col-sm-12">
							{this.props.children}
						</div>
					</div>
				</div>
			</div>
		);
	}
});

module.exports = BasePage;