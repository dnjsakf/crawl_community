// Config React-init
import React from 'react';
import ReactDOM from 'react-dom';
import { AppContainer } from 'react-hot-loader';
import App from './components/App';

import './static/common.css';

// Config Redux
import { createStore, applyMiddleware } from 'redux';
import { Provider } from 'react-redux';
import rootReducer from './reducers';

// Config ReduxSaga
import createSagaMiddleware from 'redux-saga';
import rootSagas from './sagas';

const sagaMiddleware = createSagaMiddleware();
const devTools = window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__();
const store = createStore( rootReducer, applyMiddleware(sagaMiddleware) );

/*
store.subscribe(()=>{
	const state = store.getState()
	console.log( state.communities );
	console.log( state.sign );
	console.log( state.menus );
	console.log( state.tabs );
});
*/
			  
function render( Component ){
	ReactDOM.render( 
    <AppContainer>
			<Provider store={ store }>
				<Component />
			</Provider>
		</AppContainer>
	, document.getElementById('root') );
	
}
sagaMiddleware.run(rootSagas);

render(App);

if( module.hot ){
	module.hot.accept( ('./components/App'), () => render(App));
}