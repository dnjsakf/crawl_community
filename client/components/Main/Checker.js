import React, { memo, useState, useEffect, useCallback, useRef } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { withRouter } from 'react-router-dom';

import { actionSignCheck } from './../../reducers/auth'

const Checker = memo(( props )=>{
  const dispatch = useDispatch();

  const alreadySigned = Boolean(localStorage.getItem("logged"));
  const { logged } = useSelector((state)=>( state.auth ), []);

  const handleAuthCheck = useCallback(()=>{
    dispatch( actionSignCheck() );
  }, [ alreadySigned ]);

  useEffect(()=>{
    handleAuthCheck();

    console.log('[Checker][alreadySigned]', alreadySigned, logged);
    if( alreadySigned ){
      props.history.push('/');
    } else {
      console.log('[Checker][doSingIn]', alreadySigned, logged);
    }
    return ()=>{
      console.log('[Checker][prev]', alreadySigned, logged);
    }
  }, [ alreadySigned ]);

  useEffect(()=>{
    console.log('[Checker][logged]', logged)
  }, [ logged ]);

  return (
    <></>
  );
});

export default withRouter(Checker);