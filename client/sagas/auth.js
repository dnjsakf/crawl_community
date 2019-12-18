import { all, call, put, fork, takeLatest, takeEvery } from 'redux-saga/effects'
import { SIGN_IN, SIGN_IN_SUCCESS, SIGN_IN_FAILURE } from '../reducers/auth'
import { SIGN_UP, SIGN_UP_SUCCESS, SIGN_UP_FAILURE } from '../reducers/auth'
import { SIGN_OUT, SIGN_OUT_SUCCESS, SIGN_OUT_FAILURE } from '../reducers/auth'
import { SIGN_CHECK, SIGN_CHECK_SUCCESS, SIGN_CHECK_FAILURE } from '../reducers/auth'
import { REFRESH_TOKEN, REFRESH_TOKEN_SUCCESS, REFRESH_TOKEN_FAILURE } from '../reducers/auth'

import axios from './../utils/axios'

const requestSignIn = ( payload )=> {
  console.log( '[saga][user] requestSignIn', payload );
  return axios({
    method: 'POST'
    , url: '/auth/signin'
    , data: {
      userinfo: payload
    }
  });
}

const requestSignUp = ( payload )=>{
  console.log( '[saga][user] requestSignUp', payload );
  return axios({
    method: 'POST'
    , url: '/auth/signup'
    , data: {
      userinfo: payload
    }
  });
}

const requestSignOut = ()=>{
  console.log( '[saga][user] requestSignOut');
  return axios({
    method: 'POST'
    , url: '/auth/signout'
  });
} 

const requestSignCheck = ()=>{
  console.log( '[saga][auth] requestSignCheck');
  return axios({
    method: 'POST'
    , url: '/auth/signchk'
  });
}

const requestRefreshToken = ( token )=>{
  console.log( '[saga][auth] requestRefreshToken');
  return axios({
    method: 'POST'
    , url: '/auth/refresh'
    , data: {
      token: token
    }
  })
}

function* handleSignIn({ payload }){
  try {
    const result = yield call( requestSignIn, payload );
    console.log('[saga][auth] handleSingIn', result);
    yield put({
      type: SIGN_IN_SUCCESS
      , payload: result.data
    });
  } catch ( error ){
    console.log(error.response);
    yield put({
      type: SIGN_IN_FAILURE
      , payload: error.response.data
    })
  } 
}

function* handleSignUp({ payload }){
  try {
    const result = yield call( requestSignUp, payload );
    console.log('[saga][auth] handleSignUp', result);
    yield put({
      type: SIGN_UP_SUCCESS
      , payload: result.data
    });
  } catch ( error ){
    console.log(error.response);
    yield put({
      type: SIGN_UP_FAILURE
      , payload: error.response.data
    })
  } 
}

function* handleSignOut({ payload }){
  try {
    const result = yield call( requestSignOut, payload );
    console.log('[saga][auth] handleSignOut', result);
    yield put({
      type: SIGN_OUT_SUCCESS
      , payload: result.data
    });
  } catch ( error ){
    console.log(error.response);
    yield put({
      type: SIGN_OUT_FAILURE
      , payload: error.response.data
    });
  }
}

function* handleSignCheck({ payload }){
  try {
    const result = yield call( requestSignCheck, payload );
    console.log('[saga][auth] handleSignCheck', result);
    yield put({
      type: SIGN_CHECK_SUCCESS
      , payload: result.data
    });
  } catch ( error ){
    console.log( error.response );
    const payload = error.response.data.payload;
    if( payload && payload['refresh'] ){
      const token = localStorage.getItem('token');
      yield put({
        type: REFRESH_TOKEN
        , payload: token
      });
    } else {
      yield put({
        type: SIGN_CHECK_FAILURE
        , payload: error.response.data
      });
    }
  }
}

function* handleRefreshToken({ payload }){
  try {
    const result = yield call( requestRefreshToken, payload );
    console.log('[saga][auth] handleRefreshToken', result);
    yield put({
      type: SIGN_CHECK
      , payload: result.data
    });
  } catch ( error ) {
    yield put({
      type: REFRESH_TOKEN_FAILURE
      , payload: error.response.data
    });
  }
}

function* watchSignIn(){
  yield takeLatest( SIGN_IN, handleSignIn );
}
function* watchSignUp(){
  yield takeLatest( SIGN_UP, handleSignUp );
}
function* watchSignOut(){
  yield takeLatest( SIGN_OUT, handleSignOut );
}
function* watchSignCheck(){
  yield takeLatest( SIGN_CHECK, handleSignCheck );
}
function* watchRefreshToken(){
  yield takeLatest( REFRESH_TOKEN, handleRefreshToken );
}

export default function* authSaga(){
  yield all([
    fork( watchSignIn )
    , fork( watchSignUp )
    , fork( watchSignOut )
    , fork( watchSignCheck )
    , fork( watchRefreshToken )
  ])
}