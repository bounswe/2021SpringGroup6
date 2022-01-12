import {React, Fragment, useEffect, lazy, Suspense, useState} from 'react'
// import logo from './logo.svg';
import './App.css';
import {Row} from 'react-bootstrap'
import { Routes, Route, Outlet, Link, Navigate, useLocation } from 'react-router-dom';
import Header from './PermanentComponents/Header';
import SidebarComponent from './PermanentComponents/SidebarComponent';
// import PasswordChange from './PasswordChange';
import Footer from './PermanentComponents/Footer';
import ActivityStream from './pages/ActivityStream/ActivityStream'

import {UserContext} from './UserContext';
import UseWindowSize from './PermanentComponents/WindowSizing';

import gif from './images/squadgamegif.gif'
import Notifications from "./pages/Notifications";



const PasswordReset = lazy(() => import('./pages/PasswordReset/PasswordReset'));
const Profile = lazy(() => import('./pages/profile/Profile'));
const ProfileView = lazy(() => import('./pages/profile/ProfileView'));
const Login = lazy(() => import('./pages/Login/Login'));
const Register = lazy(() => import('./pages/Register/Register'));
const EventSettingsPage = lazy(() => import('./pages/Event/EventSettingsPage'));
const EventPage = lazy(() => import('./pages/Event/EventPage'));
const NewEvent = lazy(() => import('./pages/NewEvent/NewEvent'));
const NewEquipment = lazy(() => import('./pages/NewEquipment/NewEquipment'));
const NewField = lazy(() => import('./pages/NewField/NewField'));
const SearchPage = lazy(() => import('./pages/SearchPage/SearchPage'));
const SearchEquipmentPage = lazy(() => import('./pages/SearchEquipment/SearchEquipment'));
const SearchFieldPage = lazy(() => import('./pages/SearchField/SearchField'));
const ModifyEvent = lazy(() => import('./pages/Event/ModifyEvent/ModifyEvent'))
const EquipmentInformationFunctional = lazy(() => import('./pages/EquipmentInformation/EquipmentInformationFunctional'))



function App() {
  // localStorage.setItem("user",localStorage.getItem('user') || JSON.stringify({identifier: ""}));
  const [user, setUser] = useState(JSON.parse(localStorage.getItem('user')) || {identifier: ""});
  // const [window_width, window_height] = UseWindowSize();

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
        <Row style={{minHeight: '92vh', alignItems: 'stretch'}}>
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
    return (
    <Fragment>
      {user.token ?
          <ActivityStream token={user.token}/>
          :
          <div id="deneme"
            style={{height: '100%', display: 'flex', flexDirection: 'column',
              justifyContent: 'space-around' , alignItems: 'center'}}>
            <div style={{display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center'}}>
              <img src={gif} width="250" alt="logo" />
              <span className="main-logo">Squad Game</span>
            </div>
            <span>
              Welcome <Link to="/login">Login Here</Link>
            </span>
          </div>
      }
    </Fragment>)
  }

  return (
    <UserContext.Provider value={{user, setUser}}>
      <Routes //location={(location.state && location.state.backgroundLocation) || location}
      >
        {user.token ?
          <Route path="/" element={<Framework/>}>

            <Route index element={<HomePage/>} />

	          <Route path="new-event"
              element={
                <Suspense fallback={<>...</>}>
                  <div className="default-body"><NewEvent/></div>
                </Suspense>}/>


            <Route path="new-equipment"
              element={
                <Suspense fallback={<>...</>}>
                  <div className="default-body"><NewEquipment/></div>
                </Suspense>}/>


            <Route path="new-field"
              element={
                <Suspense fallback={<>...</>}>
                  <div className="default-body"><NewField/></div>
                </Suspense>}/>


	          <Route path="search-page"
              element={
                <Suspense fallback={<>...</>}>
                  <div className="default-body"><SearchPage/></div>
                </Suspense>}/>


            <Route path="equipment/:id"  element={
                <Suspense fallback={<>...</>}>
                  <div className="default-body"><EquipmentInformationFunctional/></div>
                </Suspense>}/>


            <Route path="search-equipment-page"
              element={
                <Suspense fallback={<>...</>}>
                  <div className="default-body"><SearchEquipmentPage/></div>
                </Suspense>}/>


            <Route path="search-field-page"
              element={
                <Suspense fallback={<>...</>}>
                  <div className="default-body"><SearchFieldPage/></div>
                </Suspense>}/>

            <Route path="profile">
                <Route index
                  element={
                    <Suspense fallback={<div className="default-body"><div>...</div></div>}>
                      <Profile/>
                    </Suspense>}/>
                <Route path=":id"
                element={
                  <Suspense fallback={<>...</>}>
                    <ProfileView/>
                  </Suspense>}/>

            </Route>

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

            <Route path="modify-event/:id"
              element={
                <Suspense fallback={<>...</>}>
                  <div className="default-body"><ModifyEvent/></div>
                </Suspense>}/>

            <Route path="event-settings"
              element={
                <Suspense fallback={<>...</>}>
                  <EventSettingsPage/>
                </Suspense>}/>


            {/* Using path="*"" means "match anything", so this route
                  acts like a catch-all for URLs that we don't have explicit
                  routes for. */}
            <Route path="notifications"
                   element={
                     <Suspense fallback={<>...</>}>
                       <Notifications/>
                     </Suspense>}/>

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
