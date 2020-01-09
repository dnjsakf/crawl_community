import { all, call, put, fork, takeLatest } from 'redux-saga/effects'
import { GET_USERS, GET_USERS_SUCCESS, GET_USERS_FAILURE } from '../../reducers/cnts/users'

import axios from './../../utils/axios'

const requestGetUsers = ( payload )=> {
  console.log( '[saga][cnts][users] requestGetUsers', payload );
  return axios({
    url: '/cnts/users/list' + ( payload ? '?'+payload : '' )
  });
}

function* handleGetUsers({ payload }){
  try {
    const result = yield call( requestGetUsers, payload );
    console.log('[saga][cnts][users] handleGetUsers', result);
    yield put({
      type: GET_USERS_SUCCESS
      , payload: result.data
    });
  } catch ( error ) {
    yield put({
      type: GET_USERS_FAILURE
      , payload: error.response
    });
  }
}

function* watchGetUsers(){
  yield takeLatest( GET_USERS, handleGetUsers );
}

export default function* usersSaga(){
  yield all([
    fork( watchGetUsers )
  ])
}