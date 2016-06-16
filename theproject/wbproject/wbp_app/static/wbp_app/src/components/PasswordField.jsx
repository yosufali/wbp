var React = require('react');

var PasswordField = React.createClass({
	getInitialState: function() {
			return {value: ""};
	},

	onChange: function(e) {
			this.setState({value: e.target.value});
	},

	clear: function() {
		this.setState({value: ""})
	},

	render: function() {
		return (
			<input 
				className="form-control"
				type="password"
				placeholder={this.props.type} 
				onChange={this.onChange} 
				value={this.state.value}
			/>
		);
	}
});

module.exports = PasswordField;