import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'
import Navbar from "./components/Navigation/Navbar";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import CategoryDetail from "./components/Category/CategoryDetail";
import PostDetail from "./components/Posts/PostDetail";

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <Navbar/>
        <Switch>
          <Route path="/category/:id" exact component={CategoryDetail}/>
          <Route path="/post/:id" exact component={PostDetail}/>

        </Switch>
      </div>
    </BrowserRouter>
  )
}

export default App;
