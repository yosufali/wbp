var React = require('react');

var ModulePage = React.createClass({
	getInitialState: function() {
		return {pid: ""}
	},

	componentDidMount: function() {
		this.setState({pid: this.props.params.moduleId});
	},

	// DidMount is only called at the beginning but we still need to refresh the when clicking buttons
	componentWillReceiveProps: function(nextProps) {
		this.setState({pid: nextProps.params.productId});
	},

	render: function() {
		return (
			<h1> Hi, I'm MODULE number {this.state.pid} </h1>
		);
	}
});

module.exports = ModulePage; 