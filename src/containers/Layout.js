import React from 'react';
import { Layout, Menu, Breadcrumb } from 'antd';
import { Link } from 'react-router-dom';
import profile from "assets/img/faces/osmar.jpg";
import Button from "components/CustomButtons/Button.js";
import GridContainer from "components/Grid/GridContainer.js";
import GridItem from "components/Grid/GridItem.js";
import classNames from "classnames";
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";
import styles from "assets/jss/material-kit-react/views/profilePage.js";

// @material-ui/icons

// core components
import Header from "components/Header/Header.js";
import HeaderLinks from "components/Header/HeaderLinks.js";

//import Footer from "components/Footer/Footer.js";

import Parallax from "components/Parallax/Parallax.js";




const CustomLayout = (props) => {
  const useStyles = makeStyles(styles);
  const dashboardRoutes = ['hola', 'que'];
  const { Head, Content, Foot } = Layout;
  const classes = useStyles();
  const imageClasses = classNames(
    classes.imgRaised,
    classes.imgRoundedCircle,
    classes.imgFluid
  );
  return(

          <div>
                <Header
        color="transparent"
        routes={dashboardRoutes}
        rightLinks={<HeaderLinks />}
        brand="osmaralg"
        fixed
        changeColorOnScroll={{
          height: 400,
          color: "white"
        }}

      />            
      <Parallax small filter image={require("assets/img/profile-bg.jpg")} />

                <div style={{ background: '#fff', padding: 24, minHeight: 280, marginLeft: '25px',
                marginRight: '25px'}}>
                {props.children}
                </div>


              </div>
    );
}
export default CustomLayout;
