// import logo from './logo.svg';
import './App.css';
import Prac1 from './prac1/Prac1';

import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'; //라우팅

function App() {
  return (
    <BrowserRouter>
      <main className="App-header">
        <header className='w-full h-16 bg-blue-200
                          flex justify-between items-center
                          p-5 text-gray-700'>
          <h1 className='font-bold'>React Practice</h1>

          {/* 상단바 선택란 */}
          <ul className='text-lg font-bold flex justify-center items-center'>
            <li className='px-5 hover:text-amber-400 rounded-sm'>
              <Link to='/Prac1'>Photo</Link>
            </li>
          </ul>
        </header>

        <div>
          <Routes>
            <Route path='/Prac1' element={<Prac1 />} />
          </Routes>
        </div>
      </main>
    </BrowserRouter>
  );
}

export default App;
