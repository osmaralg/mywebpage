import React from 'react';
import { Layout, Menu, Breadcrumb } from 'antd';
import { Link } from 'react-router-dom';

import classNames from "classnames";
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";

// @material-ui/icons

// core components
import Header from "components/Header/Header.js";
import HeaderLinks from "components/Header/HeaderLinks.js";

//import Footer from "components/Footer/Footer.js";

import Parallax from "components/Parallax/Parallax.js";


const dashboardRoutes = ['hola', 'que'];
const { Head, Content, Foot } = Layout;
const CustomLayout = (props) => {
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
              <Parallax filter image={require("assets/img/landing-bg.jpg")} />
              <div style = {{ background: '#ddd' }} >
                <div style={{ background: '#fff', padding: 24, minHeight: 280, marginLeft: '25px',
                marginRight: '25px'}}>
                {props.children}
                </div>
                </div>

              </div>
    );
}
export default CustomLayout;
