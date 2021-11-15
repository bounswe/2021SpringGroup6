import {React, Fragment, useEffect, lazy, Suspense} from 'react'
import './App.css';
import {Row} from 'react-bootstrap'
import { Routes, Route, Outlet, Link } from 'react-router-dom';
import Header from './PermanentComponents/Header';
import SidebarComponent from './PermanentComponents/SidebarComponent';
import Footer from './PermanentComponents/Footer';

//import PasswordChange from './PasswordChange';
// import PasswordReset from './PasswordReset';
// import Profile from './profile/Profile';

//import PasswordChange from './PasswordChange';
const PasswordReset = lazy(() => import('./PasswordReset'));
const Profile = lazy(() => import('./profile/Profile'));
 
 

function App() {
  useEffect(() => {
    document.title = 'Squad Game'
    return () => {
      document.title = 'Squad Game'
    }
  }, [])

  function Framework() {
    return (
    <Fragment>
      <div style={{minHeight: '98vh'}}>
        <Row style={{maxHeight: '8vh'}}>
          <Header />
        </Row>
        <Row style={{minHeight: '92vh',  alignItems: 'stretch'}}>
          <div style={{display: 'flex', flexDirection: 'row', flexWrap: 'wrap', alignContent: 'stretch'}}>
            <SidebarComponent />
            <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', flexGrow: 5}}>
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

  return (
    <Routes>
      <Route path="/" element={<Framework/>}>
      
        <Route index element={<>Welcome</>} />

        <Route path="profile" 
          element={
            <Suspense fallback={<>...</>}>
              <Profile/>
            </Suspense>}/>

        <Route path="forgot-password" 
          element={
            <Suspense fallback={<>...</>}>
              <PasswordReset/>
            </Suspense>}/>

        {/* Using path="*"" means "match anything", so this route
              acts like a catch-all for URLs that we don't have explicit
              routes for. */}
        <Route path="*" element={<>Welcome</>} />
      </Route>
    </Routes>
  );
}

export default App;
