import React from 'react';
import { List, Avatar } from 'antd';



const Projects = (props) => {
	return (

  <List
    itemLayout="vertical"
    size="large"
    pagination={{
      onChange: page => {
        console.log(page);
      },
      pageSize: 3,
    }}
    dataSource={props.data}
    footer={
      <div>
        <b>ant design</b> footer part
      </div>
    }
    renderItem={item => (
      <List.Item
        key={item.title}
        actions={[

        ]}
        extra={
          <img
            height={200}
            width={200}
            alt="logo"
            src={item.image}
          />
        }
      >
        <List.Item.Meta
          avatar={<Avatar src={item.avatar} />}
          title={<a href={`project/${item.id}`}>{item.title}</a>}
          description={item.description}
        />
        {item.content}
      </List.Item>
    )}
  />

		)
}

export default Projects;