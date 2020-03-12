import React from 'react';
import './App.css';
import 'antd/dist/antd.css'
import CustomLayout from './containers/Layout';
import { BrowserRouter as Router } from 'react-router-dom';
import BaseRouter from './routes';

function App() {
  return (
    <div className="App">
    <Router>
      <CustomLayout>
      	<BaseRouter />
      </CustomLayout>
     </Router>
    </div>
  );
}

export default App;
