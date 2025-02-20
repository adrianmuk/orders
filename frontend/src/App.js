// import logo from './logo.svg';
import './App.css';
import {Routes, Route} from 'react-router-dom';
import Home from './components/Home';
import Cart from './components/Cart';
import Application from './components/Application';
import NavBar from './components/NavBar';

function App() {
  return (
    <div className="App">
      <NavBar />
      <Routes>
        <Route path = "" element = {<Home />} />
        <Route path = "/cart" element = {<Cart />} />
        <Route path = "/application" element = {<Application />} />
      </Routes>
    </div>
  );
}

export default App;
