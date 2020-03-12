import React from 'react';
import Projects from '../components/Project'
import axios from 'axios';


class ProjectList extends React.Component {

	state = {
		projects : [],
	}

	componentDidMount(){

		axios.get('http://127.0.0.1:8000/list/projects')
			.then(res => {
				console.log(res.data)
				for (var i = res.data.length - 1; i >= 0; i--) {
					console.log(res.data[i].image.replace("list/projects/", ""))
					res.data[i].image = res.data[i].image.replace("list/projects/", "")
				}
				this.setState({
					projects: res.data
				});

			
			})
	}

	render (){
		return (
			<Projects data={this.state.projects}/>
			)
	}
}

export default ProjectList;