import './App.css';
import Sidebar from './components/Sidebar';
import Header from './components/Header';
import MainContent from './components/MainContent';

function App() {
  return (
    <div className='flex'>
      <Sidebar />
      <div className='w-full'>
        <Header />
        <MainContent />
      </div>
    </div>

  );
}

export default App;
