import Fetch from './components/fetch';
import {Routes,Route} from 'react-router-dom'

export default function App(){
    return(
        <div className='App'>
            <header>
                <a href="index.html">Austin New App</a>
            </header>
            <div id='secwrapper'>
                <section>
                <Routes>
                    <Route path="/" element={<Fetch/>}/>
                </Routes>
                </section>
            </div>
        </div>
    )
}