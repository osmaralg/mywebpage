import React from 'react';
import axios from 'axios';
import { Card } from 'antd';
import CustomForm from '../components/Form';
import WorldMap from 'components/WorldMap.js';
import ProjectDetailTag from 'containers/ProjectDetailTagView.js'
import 'assets/css/App.css'

function createMarkup(text) { return {__html: text}; };


class ProjectDetail extends React.Component {

	state = {
		project : {react_tag: 'foo'},
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
		const TagName = this.state.project.react_tag; 

		return (
			<div>
			<Card title={this.state.project.title}> 
			<div dangerouslySetInnerHTML={createMarkup(this.state.project.content)} />

			
			</Card>
			<div className="row">
			<div>
				<ProjectDetailTag react_tag={this.state.project.react_tag} />
			</div>
			</div>
			{/**
			<CustomForm 
				requestType="put"
				projectID={this.props.match.params.projectID} 
				btnText="Update" 
				/>
			**/}
			</div>

			)
	}
}

export default ProjectDetail;