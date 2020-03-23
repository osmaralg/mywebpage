import React from 'react';

import { Route } from 'react-router-dom';
import ProjectList from './containers/ProjectListView';
import ProjectDetail from './containers/ProjectDetailView';

const BaseRouter  = () => (
	<div>
	<Route exact path='/project/:projectID' component={ProjectDetail} />
	<Route exact path='/' component={ProjectList} />
	</div>

	);

export default BaseRouter;