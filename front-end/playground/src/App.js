import {React, Fragment, useEffect, lazy, Suspense, useState} from 'react'
// import logo from './logo.svg';
import './App.css';
import {Row} from 'react-bootstrap'
import { Routes, Route, Outlet, Link, Navigate, useLocation } from 'react-router-dom';
import Header from './PermanentComponents/Header';
import SidebarComponent from './PermanentComponents/SidebarComponent';
// import PasswordChange from './PasswordChange';
import Footer from './PermanentComponents/Footer';

import {UserContext} from './UserContext';
import UseWindowSize from './PermanentComponents/WindowSizing';

import gif from './images/squadgamegif.gif'

const PasswordReset = lazy(() => import('./pages/PasswordReset/PasswordReset'));
const Profile = lazy(() => import('./pages/profile/Profile'));
const Login = lazy(() => import('./pages/Login/Login'));
const Register = lazy(() => import('./pages/Register/Register'));
const CreateEvent = lazy(() => import('./pages/Event/Creation/Create'));
const EventSettingsPage = lazy(() => import('./pages/Event/EventSettingsPage'));
const EventPage = lazy(() => import('./pages/Event/EventPage'));


function App() {
  const [user, setUser] = useState(JSON.parse(localStorage.getItem('user')) || {identifier: ""});
  const [window_width, window_height] = UseWindowSize();
  // const location = useLocation();
  // console.log('location\n', location)
  // let state = location.state as { backgroundLocation?: Location };

  function Framework() {
    return (
    <Fragment>
      <div style={{maxHeight: '8vh'}}>
        <Header />
      </div>
      <div className="body-part" style={{minHeight: '92vh'}}>
        <SidebarComponent />
        <Outlet />
      </div>
      <div>
        <Footer />
      </div>
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
    return (<div className="default-body">
      <div
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
      
    </div>)
  }

  return (
    <UserContext.Provider value={{user, setUser}}>
      <Routes //location={(location.state && location.state.backgroundLocation) || location}
      >
        {user.token ? 
          <Route path="/" element={<Framework/>}>
          
            <Route index element={<HomePage/>} />

            {/* <Route path="login" 
              element={
                <Suspense fallback={<>...</>}>
                  <Login/>
                </Suspense>}/>

            <Route path="forgot-password" 
              element={
                <Suspense fallback={<>...</>}>
                  <PasswordReset/>
                </Suspense>}/> */}

            <Route path="profile" 
              element={
                <Suspense fallback={<>...</>}>
                  <div className="default-body"><Profile/></div>
                </Suspense>}/>

            <Route path="create-event" 
              element={
                <Suspense fallback={<>...</>}>
                  <CreateEvent/>
                </Suspense>}/>

            <Route path="event">
              <Route index 
                element={
                  <Suspense fallback={<>...</>}>
                    <EventSettingsPage/>
                  </Suspense>}/>
              
              {/* <Route path="modal/:id" 
                element={
                  <Suspense fallback={<>...</>}>
                    <div>hello</div>
                  </Suspense>}/> */}
              
              <Route path=":id" 
                element={
                  <Suspense fallback={<>...</>}>
                    <EventPage/>
                  </Suspense>}/>
            </Route>
            

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

            <Route path="create-event" 
              element={
                <Suspense fallback={<>...</>}>
                  <CreateEvent/>
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
