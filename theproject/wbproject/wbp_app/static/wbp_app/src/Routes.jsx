var React = require('react');
var ReactRouter = require('react-router');
var Router = ReactRouter.Router;
var Route = ReactRouter.Route;
var IndexRoute = ReactRouter.IndexRoute;
var Redirect = ReactRouter.Redirect;

var CreateHistory = require('history/lib/createHashHistory');

var History = new CreateHistory({
	queryKey: false
});

var BasePage = require('./components/BasePage.jsx');
var LoginPage = require('./components/LoginPage.jsx');
var ProfilePage = require('./components/ProfilePage.jsx');
var ModulePage = require('./components/ModulePage.jsx');
var ModulesPage = require('./components/ModulesPage.jsx');
// Pages: Notifications, LoggedIn name, Settings, 

var Routes = (
	<Router history={History}>
		<Route path="/">
			<IndexRoute component={LoginPage} />
		</Route>
		<Route component={BasePage}>
			<Route path="/profile/" component={ProfilePage} />
			<Route path="/modules/" component={ModulesPage} />
			<Route path="/modules/:moduleId" component={ModulePage} />
		</Route>
	</Router>
);

module.exports = Routes;