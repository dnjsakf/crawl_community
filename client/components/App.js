import React, { memo } from 'react';
import { BrowserRouter, Route, Link, Switch } from 'react-router-dom/'

import Main from './Main/Main'
import SignIn from './SignIn/SignIn'
import SignUp from './SignUp/SignUp'
import SearchAppBar from './Bars/SearchAppBar'

const App = memo(()=>{
  return (
    <BrowserRouter>
      <SearchAppBar />
      <Switch>
        <Route path="/auth/signin" component={()=>(<SignIn />)}/>
        <Route path="/auth/signup" component={()=>(<SignUp />)}/>
        <Route path="/" component={()=>(<Main />)}/>
      </Switch>
    </BrowserRouter>
  );
});

export default App;