import React from 'react';

import { Route } from 'react-router-dom';
import ProjectList from './containers/ProjectListView';
import ProjectDetail from './containers/ProjectDetailView';

const BaseRouter  = () => (
	<div>
		<Route exac path='/projects' component={ProjectList} />
		<Route exac path='/project/:projectID' component={ProjectDetail} />

	</div>

	);

export default BaseRouter;