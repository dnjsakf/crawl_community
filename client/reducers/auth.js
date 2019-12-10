export const SIGN_INIT = 'auth/SIGN_INIT';

export const SIGN_UP = 'auth/SIGN_UP';
export const SIGN_UP_SUCCESS = 'auth/SIGN_UP_SUCCESS';
export const SIGN_UP_FAILURE = 'auth/SIGN_UP_FAILURE';

export const SIGN_IN = 'auth/SIGN_IN';
export const SIGN_IN_SUCCESS = 'auth/SIGN_IN_SUCCESS';
export const SIGN_IN_FAILURE = 'auth/SIGN_IN_FAILURE';

export const SIGN_OUT = 'auth/SIGN_OUT';
export const SIGN_OUT_SUCCESS = 'auth/SIGN_OUT_SUCCESS';
export const SIGN_OUT_FAILURE = 'auth/SIGN_OUT_FAILURE';

export const SIGN_CHECK = 'auth/SIGN_CHECK';
export const SIGN_CHECK_SUCCESS = 'auth/SIGN_CHECK_SUCCESS';
export const SIGN_CHECK_FAILURE = 'auth/SIGN_CHECK_FAILURE';

export const actionSignInit = ( payload )=>({ type: SIGN_INIT, payload: payload });
export const actionSignIn = ( payload )=>({ type: SIGN_IN, payload: payload });
export const actionSignUp = ( payload )=>({ type: SIGN_UP, payload: payload });
export const actionSignOut = ( payload )=>({ type: SIGN_OUT, payload: payload });
export const actionSignCheck = ( payload )=>({ type: SIGN_CHECK, payload: payload });

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

const authReducer = ( state=initState, action )=>{
  switch( action.type ){
    case SIGN_INIT:
      return initState
    /** SingIn **/
    case SIGN_IN:
      return {
        ...state
        , logged: 0
      }
    case SIGN_IN_SUCCESS:
      return {
        ...state
        , logged: 1
        , userinfo: action.payload.user
        , success: action.payload.success
      }
    case SIGN_IN_FAILURE:
      return {
        ...state
        , logged: -1
        , userinfo: initState.userinfo
        , success: action.payload.success
      }
    /** SignUp */
    case SIGN_UP:
      return {
        ...state
        , logged: 0
      }
    case SIGN_UP_SUCCESS:
      return {
        ...state
        , logged: 1
        , success: action.payload.success
      }
    case SIGN_UP_FAILURE:
      return {
        ...state
        , logged: 0
        , success: action.payload.success
      }
    /** SignOut */
    case SIGN_OUT:
      return {
        ...state
        , logged: 0
      }
    case SIGN_OUT_SUCCESS:
      return {
        ...state
        , logged: 0
        , success: action.payload.success
      }
    case SIGN_OUT_FAILURE:
      return {
        ...state
        , logged: 0
        , success: action.payload.success
      }
    /** Check **/
    case SIGN_CHECK:
      return {
        ...state
        , logged: 0
      }
    case SIGN_CHECK_SUCCESS:
      return {
        ...state
        , logged: 1
      }
    case SIGN_CHECK_FAILURE:
      return {
        ...state
        , logged: 0
      }
    default:
      return state
  }
}
export default authReducer