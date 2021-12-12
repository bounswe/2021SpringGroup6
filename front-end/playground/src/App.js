import {React, Fragment, useEffect, lazy, Suspense, useState} from 'react'
// import logo from './logo.svg';
import './App.css';
import {Row} from 'react-bootstrap'
import { Routes, Route, Outlet, Link, Navigate } from 'react-router-dom';
import Header from './PermanentComponents/Header';
import SidebarComponent from './PermanentComponents/SidebarComponent';
// import PasswordChange from './PasswordChange';
import Footer from './PermanentComponents/Footer';

import {UserContext} from './UserContext'

import gif from './images/squadgamegif.gif'


const PasswordReset = lazy(() => import('./pages/PasswordReset/PasswordReset'));
const Profile = lazy(() => import('./pages/profile/Profile'));
const Login = lazy(() => import('./pages/Login/Login'));
const Register = lazy(() => import('./pages/Register/Register'));
const NewEvent = lazy(() => import('./pages/NewEvent/NewEvent'));
const SearchPage = lazy(() => import('./pages/SearchPage/SearchPage'));



function App() {
  const [user, setUser] = useState(JSON.parse(localStorage.getItem('user')) || {identifier: ""});
  const [sidebarToggle, setSidebarToggle] = useState(true)

  useEffect(() => {console.log('\nuser\n', user)}, [user])

  function Framework() {
    return (
    <Fragment>
      <div style={{minHeight: '98vh'}}>
        <Row style={{maxHeight: '8vh'}}>
          <Header />
        </Row>
        <Row style={{minHeight: '92vh',  alignItems: 'stretch'}}>
          <div style={{display: 'flex', flexDirection: 'row', flexWrap: 'wrap', alignContent: 'stretch'}}>
            <SidebarComponent toggle={sidebarToggle} setToggle={setSidebarToggle} />
            <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', flexGrow: 5, flexDirection: 'column'}}>
              <Outlet />
            </div>
          </div>
        </Row>
      </div>
      <Row>
        <Footer />
      </Row>
    </Fragment>)
  }

  function FrameworkLogin() {
    return (
    <Fragment>
      <div style={{minHeight: '98vh'}}>
        <Row style={{maxHeight: '8vh'}}>
          <Header />
        </Row>
        <Row style={{minHeight: '92vh',  alignItems: 'stretch'}}>
          <div style={{display: 'flex', flexDirection: 'row', flexWrap: 'wrap', alignItems: 'center', justifyContent: 'center'}}>
            <Outlet />
          </div>
        </Row>
      </div>
      <Row>
        <Footer />
      </Row>
    </Fragment>)
  }

  function HomePage() {
    return (<Fragment>
      <div id="deneme" 
        style={{height: '100%', display: 'flex', flexDirection: 'column', 
          justifyContent: user.token ? 'center' : 'space-around' , alignItems: 'center'}}>
        <img src={gif} width="250" alt="logo" />
        {user.token ? 
          <span className="main-logo">Squad Game</span> 
          : 
          <span>
            Welcome <Link to="/login">Login Here</Link>
            </span>}
      </div>
      
    </Fragment>)
  }

  return (
    <UserContext.Provider value={{user, setUser}}>
      <Routes>
        {user.token ? 
          <Route path="/" element={<Framework/>}>
          
            <Route index element={<HomePage/>} />

            <Route path="login" 
              element={
                <Suspense fallback={<>...</>}>
                  <Login/>
                </Suspense>}/>

            
            	    
	          <Route path="new-event" 
              element={
                <Suspense fallback={<>...</>}>
                  <NewEvent/>
                </Suspense>}/>

            	    
	          <Route path="search-page" 
              element={
                <Suspense fallback={<>...</>}>
                  <SearchPage/>
                </Suspense>}/>

            




	          <Route path="forgot-password" 
              element={
                <Suspense fallback={<>...</>}>
                  <PasswordReset/>
                </Suspense>}/>

            <Route path="profile" 
              element={
                <Suspense fallback={<>...</>}>
                  <Profile/>
                </Suspense>}/>

            

            {/* Using path="*"" means "match anything", so this route
                  acts like a catch-all for URLs that we don't have explicit
                  routes for. */}
            <Route path="*" element={<Navigate replace to="/" />} />
          </Route>

        :
          
          <Route path="/" element={<FrameworkLogin/>}>
          
            <Route index element={<HomePage/>} />

            <Route path="login" 
              element={
                <Suspense fallback={<>...</>}>
                  <Login/>
                </Suspense>}/>

            <Route path="register" 
              element={
                <Suspense fallback={<>...</>}>
                  <Register/>
                </Suspense>}/>

          
                      
            <Route path="forgot-password" 
              element={
                <Suspense fallback={<>...</>}>
                  <PasswordReset/>
                </Suspense>}/>
            

            {/* Using path="*"" means "match anything", so this route
                  acts like a catch-all for URLs that we don't have explicit
                  routes for. */}
            <Route path="*" element={<Navigate replace to="/" />} />
          </Route>}
      </Routes>
    </UserContext.Provider>
  );
}

export default App;
