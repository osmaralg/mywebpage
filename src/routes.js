import React from "react";
import { Route } from "react-router-dom";

import ProjectList from './containers/ProjectListView';
import ProjectDetail from './containers/ProjectDetailView';
import ArticleList from "./containers/ArticleListView";
import ArticleDetail from "./containers/ArticleDetailView";
import Login from "./containers/Login";
import Signup from "./containers/Signup";
import Nothing from "./components/None"

const BaseRouter = () => (
  <div>
    <Route exact path="/article_list/" component={ArticleList} />{" "}
    <Route exact path="/articles/:articleID/" component={ArticleDetail} />{" "}
    <Route exact path="/login/" component={Login} />{" "}
    <Route exact path="/signup/" component={Signup} />{" "}
    <Route exact path='/project_detail_2/:projectID' component={ProjectDetail} />
	<Route exact path='/' component={ProjectList} />
	<Route exact path='/academic/' component={Nothing} />
  </div>
);

export default BaseRouter;
