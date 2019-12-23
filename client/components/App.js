import React, { memo } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom/';

import Checker from './Common/Checker';
import SignIn from './SignIn/SignIn';
import SignUp from './SignUp/SignUp';
import Paperbase from './Theme/Paperbase';

const App = memo(( props )=>{
  return (
    <BrowserRouter>
      {/* <SearchAppBar /> */}
      <Switch>
        <Route exact path="/" component={()=>(<Paperbase />)}/>
        <Route exact path="/auth/signin" component={()=>(<SignIn />)}/>
        <Route exact path="/auth/signup" component={()=>(<SignUp />)}/>
      </Switch>
      <Checker/>
    </BrowserRouter>
  );
});

export default App;