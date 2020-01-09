import { all, call, put, fork, takeLatest } from 'redux-saga/effects'
import { GET_COMMUNITIES, GET_COMMUNITIES_SUCCESS, GET_COMMUNITIES_FAILURE } from '../../reducers/cnts/communities'

import axios from './../../utils/axios'

const requestGetCommunities = ( payload )=> {
  console.log( '[saga][cnts][communities] requestGetCommunities', payload );
  return axios({
    url: '/cnts/communities/list'
  });
}

function* handleGetCommunities({ payload }){
  try {
    const result = yield call( requestGetCommunities, payload );
    console.log('[saga][cnts][communities] handleGetCommunities', result);
    yield put({
      type: GET_COMMUNITIES_SUCCESS
      , payload: result.data
    });
  } catch ( error ) {
    yield put({
      type: GET_COMMUNITIES_FAILURE
      , payload: error.response
    });
  }
}

function* watchGetCommunities(){
  yield takeLatest( GET_COMMUNITIES, handleGetCommunities );
}

export default function* communitiesSaga(){
  yield all([
    fork( watchGetCommunities )
  ])
}