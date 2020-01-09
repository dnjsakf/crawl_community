import { createAction, handleActions } from 'redux-actions';

export const GET_COMMUNITIES = 'cnts/communities/GET_COMMUNITIES'
export const GET_COMMUNITIES_SUCCESS = 'cnts/communities/GET_COMMUNITIES_SUCCESS'
export const GET_COMMUNITIES_FAILURE = 'cnts/communities/GET_COMMUNITIES_FAILURE'

export const actionGetCommunities = createAction( GET_COMMUNITIES );

const initState = {
  success: false
  , data: []
}

const communitiesReducer = handleActions({
  /** GET_COMMUNITIES **/
  [GET_COMMUNITIES]: ( state )=>({
    ...state
  }),
  [GET_COMMUNITIES_SUCCESS]: ( state, action )=>({
    ...state
    , success: action.payload.success
    , data: action.payload.data
  }),
  [GET_COMMUNITIES_FAILURE]: ()=>( initState ),
}, initState );

export default communitiesReducer;