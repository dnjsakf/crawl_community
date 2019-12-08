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

export const actionInsertUser = ( userinfo )=>({type: INSERT_USER, payload: userinfo})
export const actionUpdateUser = ( userinfo )=>({type: UPDATE_USER, payload: userinfo})
export const actionDeleteUser = ( userinfo )=>({type: DELETE_USER, payload: userinfo})
export const actionSelectUser = ( userinfo )=>({type: SELECT_USER, payload: userinfo})

const initState = {
  logged: 0
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
  switch( action.type ){
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
      }
    case INSERT_USER_FAILURE:
      return {
        ...state
        , logged: -1
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
      }
    case SELECT_USER_FAILURE:
      return {
        ...state
        , logged: -1
        , userinfo: initState.userinfo
      }
    default:
      return state
  }
}
export default userReducer