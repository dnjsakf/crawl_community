import { all, call, put, fork, takeLatest } from 'redux-saga/effects'
import { INSERT_USER, INSERT_USER_SUCCESS, INSERT_USER_FAILURE } from '../reducers/user'
import { UPDATE_USER, UPDATE_USER_SUCCESS, UPDATE_USER_FAILURE } from '../reducers/user'
import { DELETE_USER, DELETE_USER_SUCCESS, DELETE_USER_FAILURE } from '../reducers/user'
import { SELECT_USER, SELECT_USER_SUCCESS, SELECT_USER_FAILURE } from '../reducers/user'
import { CHECK_USER, CHECK_USER_SUCCESS, CHECK_USER_FAILURE } from '../reducers/user'

import axios from './../utils/axios'

function requestSignIn( userinfo ){
  console.log( '[saga][user] requestSignIn', userinfo );
  return axios({
    method: 'POST'
    , url: '/auth/signin'
    , data: {
      userinfo: userinfo
    }
  });
}

function requestSignUp( userinfo ){
  console.log( '[saga][user] requestSignUp', userinfo );
  return axios({
    url: '/auth/signup'
    , data: {
      userinfo: userinfo
    }
  });
}

function requestSignCheck( userinfo ){
  console.log( '[saga][user] requestSignCheck', userinfo );
  return axios({
    url: '/auth/signchk'
  });
}

function* handleSelect( action ){
  try {
    const result = yield call( requestSignIn, action.payload );
    console.log('[saga][user] handleSelect', result);
    yield put({
      type: SELECT_USER_SUCCESS
      , payload: result.data
    });
  } catch ( error ){
    yield put({
      type: SELECT_USER_FAILURE
      , payload: error
    })
  } 
}

function* handleInsert( action ){
  try {
    const result = yield call( requestSignUp, action.payload )
    console.log('[saga][user] handleInsert', result);
    yield put({
      type: INSERT_USER_SUCCESS
      , payload: result.data
    });
  } catch ( error ){
    yield put({
      type: INSERT_USER_FAILURE
      , payload: error
    });
  }
}

function* handleCheck( action ){
  try {
    const result = yield call( requestSignCheck, action );
    console.log('[saga][user] handleCheck', result);
    yield put({
      type: SELECT_USER_SUCCESS
      , payload: result.data
    });
  } catch ( error ){
    yield put({
      type: CHECK_USER_FAILURE
      , payload: error
    });
  }
}

function* watchSelect(){
  yield takeLatest( SELECT_USER, handleSelect );
}
function* watchInsert(){
  yield takeLatest( INSERT_USER, handleInsert );
}
function* watchCheck(){
  yield takeLatest( CHECK_USER, handleCheck );
}

export default function* userSaga(){
  yield all([
    fork( watchSelect )
    , fork( watchInsert )
    , fork( watchCheck )
  ])
}