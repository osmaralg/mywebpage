import React from 'react';
import Projects from '../components/Project';
import CustomForm from '../components/Form'
import axios from 'axios';
import profile from "assets/img/faces/osmar.jpg";
import Button from "components/CustomButtons/Button.js";
import GridContainer from "components/Grid/GridContainer.js";
import GridItem from "components/Grid/GridItem.js";
import classNames from "classnames";
import { makeStyles } from "@material-ui/core/styles";
import styles from "assets/jss/material-kit-react/views/profilePage.js";


const ProfilePicutre = (props) => {
  const useStyles = makeStyles(styles);
  const classes = useStyles();
  const imageClasses = classNames(
    classes.imgRaised,
    classes.imgRoundedCircle,
    classes.imgFluid
  );
  return(
        <div>
          <div className={classes.container}>
            <GridContainer justify="center">
              <GridItem xs={12} sm={12} md={6}>
                <div className={classes.profile}>
                  <div>
                    <img src={profile} alt="..." className={imageClasses} />
                  </div>
                  <div className={classes.name}>
                    <h3 className={classes.title}>Osmar Alcala</h3>
                    <h6>DESIGNER</h6>
                    {/**<Button justIcon link className={classes.margin5}>
                      <i className={"fab fa-twitter"} />
                    </Button>
                    <Button justIcon link className={classes.margin5}>
                      <i className={"fab fa-instagram"} />
                    </Button>
                    <Button justIcon link className={classes.margin5}>
                      <i className={"fab fa-facebook"} />
                    </Button>**/}
                  </div>
                </div>
              </GridItem>
            </GridContainer>
            <div className={classes.description}>
              <p>
                An artist of considerable range, Chet Faker — the name taken by
                Melbourne-raised, Brooklyn-based Nick Murphy — writes, performs
                and records all of his own music, giving it a warm, intimate
                feel with a solid groove structure.{" "}
              </p>
            </div>
          </div>
        </div>
    );
}


class ProjectList extends React.Component {

	state = {
		projects : [],
	}

	componentDidMount(){

		axios.get('/list/projects/')
			.then(res => {
				console.log("" , res.data)

				for (var i = res.data.length - 1; i >= 0; i--) {
						res.data[i].image = res.data[i].image.replace("list/projects/", "")
				}

		this.setState({
			projects: res.data
		});

			
			})

	}


	render (){

		return (

			<div>
			    <ProfilePicutre />
				<Projects data={this.state.projects}/>
				<br />

				{/*
									<h2> Create a project </h2>
				<CustomForm 
					requestType="post" 
					projectID={null} 
					btnText="Create" /> */
				}

			</div>
			)

	}
}

export default ProjectList;