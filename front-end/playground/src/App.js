import {Fragment, useEffect} from 'react'
import './App.css';
import Header from './PermanentComponents/Header';
import SidebarComponent from './PermanentComponents/SidebarComponent';
import PasswordChange from './PasswordChange';
import PasswordReset from './PasswordReset';
import Footer from './PermanentComponents/Footer';
import {Row, Col} from 'react-bootstrap'
import { Routes, Route, Outlet, Link } from 'react-router-dom';
 
 

function App() {
  useEffect(() => {
    document.title = 'Giriş - Squad Game'
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
          {/* <Col  style={{}}> */}
            <div style={{display: 'flex', flexDirection: 'row', flexWrap: 'wrap', alignContent: 'stretch'}}>
              <SidebarComponent />
              <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', flexGrow: 5}}>
                <Outlet />
              </div>
            </div>
          {/* </Col> */}
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
        <Route index element={<div>Welcome</div>} />
        {/* <Route path="about" element={<About />} />
        <Route path="dashboard" element={<Dashboard />} /> */}

        {/* Using path="*"" means "match anything", so this route
              acts like a catch-all for URLs that we don't have explicit
              routes for. */}
        {/* <Route path="*" element={<NoMatch />} /> */}
      </Route>
    </Routes>
  );
}

export default App;
