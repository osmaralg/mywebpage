import React from 'react';
import axios from 'axios';
import { Card } from 'antd';
import CustomForm from '../components/Form';
import WorldMap from 'components/WorldMap.js';
import None from 'components/None.js';

import 'assets/css/App.css'

class ProjectDetailTag extends React.Component {

    components = {
        foo: None,
        WorldMap: WorldMap,
        none: None,
    };
	render (){
		console.log(this.props.react_tag)
		const TagName =  this.components[this.props.react_tag || 'foo'];

		return (
				<TagName  />

			)
	}
}

export default ProjectDetailTag;