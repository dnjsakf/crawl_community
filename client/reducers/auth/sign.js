import { createAction, handleActions } from 'redux-actions';

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

export const REFRESH_TOKEN = 'auth/REFRESH_TOKEN';
export const REFRESH_TOKEN_SUCCESS ='auth/REFRESH_TOKEN_SUCCESS';
export const REFRESH_TOKEN_FAILURE = 'auth/REFRESH_TOKEN_FAILURE';

export const actionSignInit = createAction( SIGN_INIT );
export const actionSignIn = createAction( SIGN_IN );
export const actionSignUp = createAction( SIGN_UP );
export const actionSignOut = createAction( SIGN_OUT );
export const actionSignCheck = createAction( SIGN_CHECK );
export const actionRefreshToken = createAction( REFRESH_TOKEN );

const initState = {
  signed: 0
  , success: false
  , token: null
  , userinfo: {
    _id: null
    , email: null
    , username: null
    , role: null
    , settings: { }
    , isAdmin: false
  }
}

const signReducer = handleActions({
  /** SIGN_INIT **/
  [SIGN_INIT]: ()=>( initState ),

  /** SIGN_IN **/
  [SIGN_IN]: ( state )=>({
    ...state
  }),
  [SIGN_IN_SUCCESS]: ( state, action )=>({
    ...state
    , signed: 1
    , userinfo: action.payload.user
    , success: action.payload.success
    , token: action.payload.token
  }),
  [SIGN_IN_FAILURE]: ( state )=>({
    ...state
    , signed: -1
  }),

  /** SIGN_UP **/
  [SIGN_UP]: ( state )=>({
    ...state
  }),
  [SIGN_UP_SUCCESS]: ( state, action )=>({
    ...state
    , signed: 1
    , success: action.payload.success
  }),
  [SIGN_UP_FAILURE]: ( state )=>({
    ...state
    , signed: 0
  }),

  /** SIGN_OUT **/
  [SIGN_OUT]: ( state )=>({
    ...state
  }),
  [SIGN_OUT_SUCCESS]: ( state, action )=>({
    ...state
    , signed: 0
    , success: action.payload.success
  }),
  [SIGN_OUT_FAILURE]: ( state )=>({
    ...state
    , signed: 0
  }),

  /** SIGN_CHECK **/
  [SIGN_CHECK]: ( state )=>({
    ...state
  }),
  [SIGN_CHECK_SUCCESS]: ( state, action )=>({
    ...state
    , signed: 1
    , userinfo: action.payload.user
    , success: action.payload.success
  }),
  [SIGN_CHECK_FAILURE]: ( state )=>({
    ...state
    , signed: 0
  }),

  /** REFRESH_TOKEN **/
  [REFRESH_TOKEN]: ( state )=>({
    ...state
  }),
  [REFRESH_TOKEN_SUCCESS]: ( state, action )=>({
    ...state
    , token: action.payload.token
  }),
  [REFRESH_TOKEN_FAILURE]: ( state )=>({
    ...state
  })
}, initState );

export default signReducer;