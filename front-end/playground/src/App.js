import logo from './logo.svg';
import './App.css';
import Header from './PermanentComponents/Header';
import SidebarComponent from './PermanentComponents/SidebarComponent';
import Footer from './PermanentComponents/Footer';
 
 

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
      <Footer />
    </div>
  );
}

export default App;
