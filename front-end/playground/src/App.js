import {Fragment, useEffect} from 'react'
import './App.css';
import Header from './PermanentComponents/Header';
import SidebarComponent from './PermanentComponents/SidebarComponent';
import Footer from './PermanentComponents/Footer';
import {Row, Col} from 'react-bootstrap'
 
 

function App() {
  useEffect(() => {
    document.title = 'Giriş - Squad Game'
    return () => {
      document.title = 'Squad Game'
    }
  }, [])
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
                <h1>
                  Main Content
                </h1>
              </div>
            </div>
          {/* </Col> */}
        </Row>
      </div>
      <Row>
        <Footer />
      </Row>
    </Fragment>
  );
}

export default App;
