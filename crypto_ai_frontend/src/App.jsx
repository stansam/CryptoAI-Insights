import logo from './logo.svg';
import './App.css';
import Sidebar from './components/Sidebar';
import Header from './components/Header';
import MainContent from './components/MainContent';

function App() {
  return (
    <div>
      <Header />
      <div>
        <Sidebar />
        <MainContent />
      </div>
    </div>
  );
}

export default App;
