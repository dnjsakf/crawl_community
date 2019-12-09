export const INIT_USER = 'user/INIT_USER';

export const INSERT_USER = 'user/INSERT_USER';
export const INSERT_USER_SUCCESS = 'user/INSERT_USER_SUCCESS';
export const INSERT_USER_FAILURE = 'user/INSERT_USER_FAILURE';

export const UPDATE_USER = 'user/UPDATE_USER';
export const UPDATE_USER_SUCCESS = 'user/UPDATE_USER_SUCCESS';
export const UPDATE_USER_FAILURE = 'user/UPDATE_USER_FAILURE';

export const DELETE_USER = 'user/DELETE_USER';
export const DELETE_USER_SUCCESS = 'user/DELETE_USER_SUCCESS';
export const DELETE_USER_FAILURE = 'user/DELETE_USER_FAILURE';

export const SELECT_USER = 'user/SELECT_USER';
export const SELECT_USER_SUCCESS = 'user/SELECT_USER_SUCCESS';
export const SELECT_USER_FAILURE = 'user/SELECT_USER_FAILURE';

export const actionInitUser = ()=>({type: INIT_USER});
export const actionInsertUser = ( payload )=>({type: INSERT_USER, payload: payload});
export const actionUpdateUser = ( payload )=>({type: UPDATE_USER, payload: payload});
export const actionDeleteUser = ( payload )=>({type: DELETE_USER, payload: payload});
export const actionSelectUser = ( payload )=>({type: SELECT_USER, payload: payload});

const initState = {
  logged: 0
  , success: false
  , userinfo: {
    _id: null
    , email: null
    , username: null
    , role: null
    , settings: { }
    , isAdmin: false
  }
}

const userReducer = ( state=initState, action )=>{
  console.log('[reducer] userReducer', action);

  switch( action.type ){
    case INIT_USER:
      return initState
    /** SignUp */
    case INSERT_USER:
      return {
        ...state
        , logged: 0
      }
    case INSERT_USER_SUCCESS:
      return {
        ...state
        , logged: 1
        , success: action.payload.success
      }
    case INSERT_USER_FAILURE:
      return {
        ...state
        , logged: -1
        , success: action.payload.success
      }
    /** SingIn **/
    case SELECT_USER:
      return {
        ...state
        , logged: 0
      }
    case SELECT_USER_SUCCESS:
      return {
        ...state
        , logged: 1
        , userinfo: action.payload.user
        , success: action.payload.success
      }
    case SELECT_USER_FAILURE:
      return {
        ...state
        , logged: -1
        , userinfo: initState.userinfo
        , success: action.payload.success
      }
    default:
      return state
  }
}
export default userReducer