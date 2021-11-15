// import logo from './logo.svg';
import './App.css';
import Header from './PermanentComponents/Header';
import SidebarComponent from './PermanentComponents/SidebarComponent';
// import PasswordChange from './PasswordChange';
import PasswordReset from './PasswordReset/PasswordReset';
import Footer from './PermanentComponents/Footer';
 
 

function App() {
  return (
    <div>
      <Header />
      <SidebarComponent />
      <PasswordReset />
      <Footer />
    </div>
  );
}

export default App;
