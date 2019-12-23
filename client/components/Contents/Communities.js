import React, { memo, useState, useEffect, useCallback, useRef } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { withRouter } from 'react-router-dom';

import { actionGetCommunities } from './../../reducers/cnts/communities';

const Communities = memo(( props )=>{
  const dispatch = useDispatch();
  
  const { success, communities } = useSelector((state)=>( state.communities ));

  const handleGetCommuities = useCallback((event)=>{
    dispatch(actionGetCommunities());
  }, [ communities ]);

  useEffect(()=>{
    handleGetCommuities();
  },[ ]);

  useEffect(()=>{
    console.log( communities );
  }, [ communities ]);

  return (
    <>
      {
        success ?
        ( <ul>
          {
            communities.map((data)=>{
              return <li key={data._id}>{ data.community }</li>
            })
          }
          </ul> 
        ) : 
        '데이터가 없습니다.'
      }
    </>
  );
});

export default withRouter(Communities);