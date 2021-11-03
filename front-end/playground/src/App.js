import logo from './logo.svg';
import './App.css';
import Header from './PermanentComponents/Header';
import SidebarComponent from './PermanentComponents/SidebarComponent';
 

function App() {
  return (
    <div>
      <Header />
      <SidebarComponent />
      <h1>Main Content</h1>
    </div>
  );
}

export default App;
