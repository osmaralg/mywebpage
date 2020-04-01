import React from 'react';
import axios from 'axios';
import { Card } from 'antd';
import CustomForm from '../components/Form';
import WorldMap from 'components/WorldMap.js';
import ProjectDetailTag from 'containers/ProjectDetailTagView.js'

function createMarkup(text) { return {__html: text}; };


class ProjectDetail extends React.Component {

	state = {
		project : {react_tag: 'foo'},
	}

	componentDidMount(){
		const projectID = this.props.match.params.projectID;
		axios.get(`/project/${projectID}`)
			.then(res => {
				this.setState({
					project: res.data
				});
				console.log("resdata", res.data)
			})
	}

	render (){
		const TagName = this.state.project.react_tag; 

		return (
			<div>
			<Card title={this.state.project.title}> 
			<div id="react_container" />			
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