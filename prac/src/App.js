// import logo from './logo.svg';
import './App.css';
import Hello from './prac1/Hello';
import Prac1 from './prac1/Prac1';
import CardMain from './prac1/CardMain';

import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'; //라우팅

function App() {
  return (
    <BrowserRouter>
      <div className="App-header">
      <main className='flex flex-col justify-center items-center
                      w-full md:w-4/5
                      h-full'>
        <header className='w-full h-16 bg-blue-200
                          flex justify-between items-center
                          p-5 text-gray-700'>
          <h1 className='font-bold'>React Practice</h1>
          </header>
            <div className="w-full grow overflow-y-auto
                    flex flex-col justify-center items-center">
              <CardMain />
            </div>

          {/* 상단바 선택란 */}
          {/* <ul className='text-lg font-bold flex justify-center items-center'>
            <li className='px-5 hover:text-amber-400 rounded-sm'>
              <Link to='/'>Hello</Link>
            </li>
            <li className='px-5 hover:text-amber-400 rounded-sm'>
              <Link to='/Prac1'>Photo</Link>
            </li>
          </ul> */}
        

        {/* <div className="w-full grow overflow-y-auto
                    flex flex-col justify-center items-center">
          <Routes>
            <Route path='/' element={<Hello />} />
            <Route path='/Prac1' element={<Prac1 />} />
          </Routes> 
        </div> */}
      </main>
      </div>
    </BrowserRouter>
  );
}

export default App;
