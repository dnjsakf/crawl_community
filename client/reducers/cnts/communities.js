export const GET_COMMUNITIES = 'cnts/communities/GET_COMMUNITIES'
export const GET_COMMUNITIES_SUCCESS = 'cnts/communities/GET_COMMUNITIES_SUCCESS'
export const GET_COMMUNITIES_FAILURE = 'cnts/communities/GET_COMMUNITIES_FAILURE'

export const actionGetCommunities = ( payload )=>({ type: GET_COMMUNITIES, payload: payload });

const initState = {
  success: false
  , communities: []
}

const communitiesReducer = (state=initState, action)=>{
  switch(action.type){
    case GET_COMMUNITIES:
      return {
        ...state
      }
    case GET_COMMUNITIES_SUCCESS:
      return {
        ...state
        , success: action.payload.success
        , communities: action.payload.data
      }
    case GET_COMMUNITIES_FAILURE:
      return initState
    default:
      return state;
  }
}

export default communitiesReducer;