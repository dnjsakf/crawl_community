import React, { memo, useState, useEffect, useCallback, useRef } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import 'axios'
import axios from 'axios';

const Main = ()=>{

  const handleClick = useCallback((event)=>{
    axios.get('http://localhost:3000/auth/signchk', { withCredentials: true })
      .then((result)=>{console.log('test',result )})
      .catch((error)=>{console.error( 'test',error )});
  },[]);

  return (
    <>
      <button onClick={ handleClick }>session</button>
    </>
  );
}

export default Main;