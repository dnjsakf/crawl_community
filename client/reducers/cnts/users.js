import { createAction, handleActions } from 'redux-actions';

export const GET_USERS = 'cnts/users/GET_USERS';
export const GET_USERS_SUCCESS = 'cnts/users/GET_USERS_SUCCESS';
export const GET_USERS_FAILURE = 'cnts/users/GET_USERS_FAILURE';

export const actionGetUsers = createAction( GET_USERS );

const initState = {
  success: false
  , data: []
}

const usersReducer = handleActions({
  /** GET_USERS **/
  [GET_USERS]: ( state )=>({
    ...state
  }),
  [GET_USERS_SUCCESS]: ( state, action )=>({
    ...state
    , success: action.payload.success
    , data: action.payload.data
  }),
  [GET_USERS_FAILURE]: ()=>( initState ),
}, initState );

export default usersReducer;