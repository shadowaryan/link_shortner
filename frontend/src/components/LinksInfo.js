import { Card } from 'antd';
import React, { useState } from 'react';
import DrawerCreateLink from './DrawerCreateLink';
import TopLink from './TopLink';
const tabList = [
  {
    key: 'tab1',
    tab: 'Recent Links',
  },
  {
    key: 'tab2',
    tab: 'Top Links',
  },
];
const contentList = {
  tab1: <TopLink/>,
  tab2: <p>content2</p>,
};


const LinksInfo = () => {
  const [activeTabKey1, setActiveTabKey1] = useState('tab1');


  const onTab1Change = (key) => {
    setActiveTabKey1(key);
  };

  return (
    <>
      <Card
        style={{
          width: '100%',
        }}
        title="Links Information"
        extra={<DrawerCreateLink/>}
        tabList={tabList}
        activeTabKey={activeTabKey1}
        onTabChange={(key) => {
          onTab1Change(key);
        }}
      >
        {contentList[activeTabKey1]}
      </Card>
    </>
  );
};

export default LinksInfo;