import React from 'react';
import axios from 'axios';
import { Card } from 'antd';

class ProjectDetail extends React.Component {

	state = {
		project : {},
	}

	componentDidMount(){
		const projectID = this.props.match.params.projectID;
		axios.get(`http://127.0.0.1:8000/project/${projectID}`)
			.then(res => {
				this.setState({
					project: res.data
				});
				console.log(res.data)
			})
	}

	render (){
		return (
			<Card title={this.state.project.title}> 
				<p>{this.state.project.content}</p>
			</Card>
			)
	}
}

export default ProjectDetail;