import './App.css';
import Header from './PermanentComponents/Header';
import SidebarComponent from './PermanentComponents/SidebarComponent';
import Footer from './PermanentComponents/Footer';
import Login from './pages/Login/Login';
 
 

function App() {
  return (
    <div>
      <Header />
      <SidebarComponent />
      <h1>
        Main Content 
        <br /> <br /> <br /> <br /><br /> <br /> <br /> <br /><br /> <br /> <br /> <br /><br /> <br /> <br /> <br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        Main Content <br />
      </h1>
      <Login/>
      <Footer />
    </div>
  );
}

export default App;
