import React from 'react';
import { List, Avatar } from 'antd';
import FeaturedPost from './FeaturedPost';
import Container from '@material-ui/core/Container';
import Grid from '@material-ui/core/Grid';



const Projects = (props) => {
	return (
	<div>
	<React.Fragment>
      <Container maxWidth="lg">
          <Grid container spacing={4}>
            {props.data.map(post => (
              <FeaturedPost key={post.title} post={post} />
            ))}
          </Grid>

      </Container>
    </React.Fragment>

	</div>
	)
}

export default Projects;