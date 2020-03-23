import React from "react";
import { Form, Input, Button } from "antd";
import axios from "axios";

const FormItem = Form.Item;


class CustomForm extends React.Component {
  
  handleFromSubmit = (event, requestType, projectID) => {
    const title = event.target.elements.title.value;
    const content = event.target.elements.content.value;
    console.log(requestType)
    switch ( requestType ) {
      case 'post': 
          return axios.post('http://127.0.0.1:8000/create_project/', {
            title: title, 
            content: content
          })
          .then( res => console.log(res))
          .catch( err => console.log(err));
      case 'put': 
          return axios.put(`http://127.0.0.1:8000/update_project/${projectID}`, {
            title: title, 
            content: content
          })
          .then( res => console.log(res))
          .catch( err => console.log(err));
    }
  }

  render() {


    return (
      <div>
        <Form onSubmit={(event) => this.handleFromSubmit(
          event,
          this.props.requestType,
          this.props.projectID,
          )}>
          <FormItem label="Title">
            <Input name="title" placeholder="Put a title here" />
          </FormItem>
          <FormItem label="Content">
            <Input name="content" placeholder="Enter some content ..." />
          </FormItem>
          <FormItem>
            <Button type="primary" htmlType="submit">
              {this.props.btnText}
            </Button>
          </FormItem>
        </Form>
      </div>
    );
  }
}



export default CustomForm;